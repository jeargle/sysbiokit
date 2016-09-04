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

    def __init__(self, matrix, rows=None, cols=None):
        self.matrix = matrix
        self.rows = rows
        self.cols = cols
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


class ElementalMatrix():
    """
    Matrix of elements (rows) and the molecules containing them (columns).
    E_ij are positive counts for elements i within molecules j.  This class
    wraps numpy's matrix.
    """

    def __init__(self, matrix):
        """
        Build an ElementalMatrix from the molecules contained in a
        StoichioMatrix.
        """
        self.matrix = matrix.copy()

    def __str__(self):
        return str(self.matrix)
