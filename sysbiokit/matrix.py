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

    def __str__(self):
        return str(self.matrix)

    
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

