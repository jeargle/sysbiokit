# John Eargle
# 2015-2016

import numpy as np


# Metabolic networks represented and analyzed as various matrices


class StoichioMatrix():
    """
    Matrix of reactants/products (rows) and reactions (columns).
    Elements S_ij are integers representing how many of the chemical are used
    or produced in a reaction.  Columns must maintain balance for mass, charge,
    element, etc.

    dx/dt = Sv
    where x is the concentration vector and v is the flux vector

    This class wraps numpy's matrix.
    """

    def __init__(self, matrix, molecules=None, reactions=None):
        self.matrix = matrix
        self.molecules = molecules
        if self.molecules is not None:
            self.mol2row = {m: i for i, m in enumerate(self.molecules)}
            self.name2row = {m.name: i for i, m in enumerate(self.molecules)}
        else:
            self.mol2row = None
            self.name2row = None

        self.reactions = reactions
        if self.reactions is not None:
            self.reaction2col = {r: i for i, r in enumerate(self.reactions)}
            self.name2col = {r.name: i for i, r in enumerate(self.reactions)}
        else:
            self.reaction2col = None
            self.name2col = None

        self.U = None
        self.S = None
        self.V = None

    def __str__(self):
        return str(self.matrix)

    def svd(self):
        self.U, s, self.V = np.linalg.svd(self.matrix)
        self.S = np.zeros(self.matrix.shape)
        for i in range(len(s)):
            self.S[i,i] = s[i]

    @property
    def column_space(self):
        if self.U is None:
            self.svd()
        dim = np.count_nonzero(self.S)
        return self.U[:,0:dim]

    @property
    def row_space(self):
        if self.V is None:
            self.svd()
        dim = np.count_nonzero(self.S)
        return self.V[0:dim,:]

    @property
    def left_null_space(self):
        if self.U is None:
            self.svd()
        dim = np.count_nonzero(self.S)
        return self.U[:,dim:]

    @property
    def right_null_space(self):
        if self.V is None:
            self.svd()
        dim = np.count_nonzero(self.S)
        return self.V[dim:,:]
        return self.V


class StoichioBinMatrix():
    """
    Binary matrix of reactants/products (rows) and reactions (columns).
    Elements S_ij are 0 or 1 representing presence or absence of chemicals
    involved in a reaction.  This class wraps numpy's matrix.
    """

    def __init__(self, matrix):
        self.matrix = matrix.copy()
        rows, cols = self.matrix.shape
        for row in range(rows):
            for col in range(cols):
                self.matrix[row,col] = 0 if self.matrix[row,col] == 0 else 1

    def __str__(self):
        return str(self.matrix)


class ReactionMatrix():
    """
    Binary reaction adjacency matrix based on a StoichioBinMatrix.
    """

    def __init__(self, matrix):
        self.matrix = np.dot(matrix.transpose(), matrix)

    def __str__(self):
        return str(self.matrix)

    def molecule_count(self, row1, row2=None):
        """
        The number of Molecule types participating in a single
        Reaction, or the number of Molecule types shared between
        two Reactions.
        """
        count = 0
        if row2 is None:
            count = self.matrix[row1, row1]
        else:
            count = self.matrix[row1, row2]
        return count
    

class MoleculeMatrix():
    """
    Binary molecule adjacency matrix based on a StoichioBinMatrix.
    Palsson refers to this as a "compound matrix".
    """

    def __init__(self, matrix):
        self.matrix = np.dot(matrix, matrix.transpose())

    def __str__(self):
        return str(self.matrix)

    def reaction_count(self, row1, row2=None):
        """
        The number of Reactions in which a Molecule type participates,
        or the number of Reactions shared between two Molecule types.
        """
        count = 0
        if row2 is None:
            count = self.matrix[row1, row1]
        else:
            count = self.matrix[row1, row2]
        return count


class ElementalMatrix():
    """
    Matrix of elements (rows) and the molecules containing them (columns).
    E_ij are positive counts for elements i within molecules j.  This class
    wraps numpy's matrix.
    """

    def __init__(self, smatrix, elements=None):
        """
        Build an ElementalMatrix from the molecules contained in a
        StoichioMatrix.
        """
        if len(smatrix.molecules) == 0:
            print 'Error: empty Molecule list'

        self.elements = elements
        self.molecules = smatrix.molecules
        if self.elements is None:
            self.build_elements()
        self.el2row = {e: i for i, e in enumerate(self.elements)}
        self.name2row = {e.name: i for i, e in enumerate(self.elements)}

        matList = []  # list of lists to construct matrix
        for molecule in self.molecules:
            elementList = [0] * len(self.elements)  # list of element counts
            for element, count in molecule.composition:
                elementList[self.el2row[element]] += count
            matList.append(elementList)

        self.matrix = np.matrix(matList).transpose()

    def build_elements(self):
        self.elements = []
        used_elements = {}
        for molecule in self.molecules:
            for element in molecule.elements:
                if element not in used_elements:
                    used_elements[element] = True
                    self.elements.append(element)

    def __str__(self):
        return str(self.matrix)
