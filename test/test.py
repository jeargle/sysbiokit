# John Eargle
# 2015-2016

import numpy as np

from sysbiokit.switch import SimpleProduct, LogicProduct, Switch
from sysbiokit.matrix import StoichioMatrix, StoichioBinMatrix
from sysbiokit.element import elements, molecules


def simple_product_test1():
    """
    Linear, no product degradation
    """
    print '\n*** SimpleProduct ***'
    sp1 = SimpleProduct('Y', 2.0)
    sp1.report()
    sp1.plot()

def simple_product_test2():
    """
    Product degradation (-0.5)
    """
    print '\n*** SimpleProduct ***'
    sp2 = SimpleProduct('Y', 2.0, -0.5)
    sp2.report()
    sp2.plot()

def logic_product_test1():
    # LogicProduct test
    print '\n*** LogicProduct ***'
    lp1 = LogicProduct('Y', 2.0, -0.5)
    lp1.report()
    # lp1.plot(-1.0, 20.0, 0.2)

def switch_test1():
    """
    """
    print '\n*** Switch ***'
    lp1 = LogicProduct('Y', 2.0, -0.5)
    s1 = Switch(child=lp1, times=[0.5, 0.7, 1.3])
    print s1

    s2 = Switch(child=lp1, times=[0.2, 0.4, 0.8], activate=False)
    print s2

    s3 = Switch(child=lp1, times=[2.0, 10.0, 20.0])
    print s3
    lp1.add_switch(s3)
    lp1.report()
    lp1.plot(-1.0, 40.0, 0.2)
    
    lp2 = LogicProduct('Y', 2.0, -0.5)
    lp2.report()
    lp1.add_child(lp2, 3.5)
    lp2.report()
    lp2.plot(-1.0, 40.0, 0.1)

def stoichiomatrix_test1():
    print '\n*** StoichioMatrix ***'
    m1 = np.matrix('1 2; 3 4')
    m2 = np.matrix([[4, 3], [2, 1]])
    print m1
    print m2
    
    sm1 = StoichioMatrix(m1)
    sm2 = StoichioMatrix(m2)
    print sm1
    print sm2

    # SVD decomposition
    # U, s, V = np.linalg.svd(sm1.matrix)
    # S = np.diag(s)
    sm1.svd()
    print sm1.U
    print sm1.S
    print sm1.V
    # print sm1.column_space
    # print sm1.row_space
    # print sm1.left_null_space
    # print sm1.right_null_space
    
    print np.allclose(sm1.matrix, np.dot(sm1.U,np.dot(sm1.S,sm1.V)))


def stoichiobinmatrix_test1():
    print '\n*** StoichioBinMatrix ***'
    m1 = np.matrix('1 0; 0 4')
    m2 = np.matrix([[0, 3], [2, 1]])
    print m1
    print m2
    
    sbm1 = StoichioBinMatrix(m1)
    sbm2 = StoichioBinMatrix(m2)
    print sbm1
    print sbm2

    # SVD decomposition
    U, s, V = np.linalg.svd(sbm1.matrix)
    S = np.diag(s)
    print U
    print S
    print V
    print np.allclose(sbm1.matrix, np.dot(U,np.dot(S,V)))


def print_element(symbol):
    print elements[symbol], elements[symbol].symbol
    
def element_test1():
    print '\n*** Element ***'
    print_element('H')
    print_element('C')
    print_element('N')
    print_element('O')
    print_element('P')
    print_element('S')


def molecule_test1():
    print '\n*** Molecule ***'
    print molecules['water'], ',', molecules['water'].formula
    print molecules['citrate'], ',', molecules['citrate'].formula


if __name__=='__main__':

    print '***********************'
    print '*** SYSBIOKIT TESTS ***'
    print '***********************'
    
    # time_plot(30)

    # ====================
    # Switch tests
    # ====================
    
    # simple_product_test1()
    # simple_product_test2()
    # logic_product_test1()
    # switch_test1()

    # ====================
    # Matrix tests
    # ====================
    
    stoichiomatrix_test1()
    # stoichiobinmatrix_test1()


    # ====================
    # Chemical tests
    # ====================

    # element_test1()
    # molecule_test1()
    
