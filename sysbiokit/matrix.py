# John Eargle
# 2015-2016

import numpy as np


# Metabolic networks represented and analyzed as various matrices


def bin_matrix(x):
    if x>0:
        return 1
    return 0



class StoichioMatrix():
    """
    Matrix of reactants/products (rows) and reactions (columns).
    Elements S_ij are integers representing how many of the chemical are used
    or produced in a reaction.  Columns must maintain balance for mass, charge,
    element, etc.  This class wraps numpy's matrix.
    """

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str1 = 'StoichioMatrix\n'
        return str1

    
class StoichioBinMatrix():
    """
    Binary matrix of reactants/products (rows) and reactions (columns).
    Elements S_ij are 0 or 1 representing presence or absence of chemicals
    involved in a reaction.  This class wraps numpy's matrix.
    """

    def __init__(self, matrix):
        self.matrix = np.array([[bin_matrix(n) for n in m] for m in matrix])

    def __str__(self):
        str1 = 'StoichioBinMatrix\n'
        return str1

