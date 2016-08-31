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

    def __init__(self, matrix):
        self.matrix = matrix
        self.U = None
        self.S = None
        self.V = None

    def __str__(self):
        return str(self.matrix)

    def svd(self):
        self.U, s, self.V = np.linalg.svd(self.matrix)
        self.S = np.diag(s)

    @property
    def column_space(self):
        if self.S is None:
            self.svd()
        return self.S

    @property
    def row_space(self):
        return self.column_space

    @property
    def left_null_space(self):
        if self.U is None:
            self.svd()
        return self.U

    @property
    def right_null_space(self):
        if self.V is None:
            self.svd()
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
        # self.matrix = np.array([[bin_matrix(n) for n in m] for m in matrix])

    def __str__(self):
        return str(self.matrix)

