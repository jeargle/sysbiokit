# John Eargle
# 2015-2016

import numpy as np

from sysbiokit.switch import SimpleProduct, LogicProduct, Switch
from sysbiokit.matrix import StoichioMatrix, StoichioBinMatrix
from sysbiokit.matrix import ReactionMatrix, MoleculeMatrix
from sysbiokit.element import elements, molecules, reactions


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
    m1 = np.matrix([[1, -1,  0,  0, -1,  0],
                    [0,  1, -1,  0,  0,  0],
                    [0,  0,  1, -1,  0,  1],
                    [0,  0,  0,  0,  1, -1]])
    m2 = np.matrix('1 2; 3 4')
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
    print 'U:'
    print sm1.U
    print 'S:'
    print sm1.S
    print 'V:'
    print sm1.V
    
    print 'column space:'
    print sm1.column_space
    print 'left null space:'
    print sm1.left_null_space
    print 'row space:'
    print sm1.row_space
    print 'right null space:'
    print sm1.right_null_space
    
    print np.allclose(sm1.matrix, np.dot(sm1.U,np.dot(sm1.S,sm1.V)))


def stoichiobinmatrix_test1():
    print '\n*** StoichioBinMatrix ***'
    m1 = np.matrix([[1, -1,  0,  0, -1,  0],
                    [0,  1, -1,  0,  0,  0],
                    [0,  0,  1, -1,  0,  1],
                    [0,  0,  0,  0,  1, -1]])
    m2 = np.matrix([[-1, 1], [1, -1]])
    print m1
    print m2
    
    sbm1 = StoichioBinMatrix(m1)
    sbm2 = StoichioBinMatrix(m2)
    print sbm1
    print sbm2

    rm1 = ReactionMatrix(sbm1.matrix)
    cm1 = MoleculeMatrix(sbm1.matrix)
    print 'Reaction Matrix:'
    print rm1
    print 'Molecule Matrix:'
    print cm1

    rm2 = ReactionMatrix(sbm2.matrix)
    cm2 = MoleculeMatrix(sbm2.matrix)
    print 'Reaction Matrix:'
    print rm2
    print 'Molecule Matrix:'
    print cm2


def print_element(symbol):
    e = elements[symbol]
    print '%s %s' % (e, e.symbol)
    
def element_test1():
    print '\n*** Element ***'
    print_element('H')
    print_element('C')
    print_element('N')
    print_element('O')
    print_element('P')
    print_element('S')


def print_molecule(name):
    m = molecules[name]
    print '%s %s %s' % (m, m.formula, m.charge_str)

def molecule_test1():
    print '\n*** Molecule ***'
    print_molecule('water')
    print_molecule('citrate')
    print_molecule('glucose')
    print_molecule('dihydroxyacetone phosphate')
    print_molecule('pyruvate')
    print_molecule('ribulose-5-phosphate')
    print_molecule('inosine monophosphate')
    print_molecule('hypoxanthine')
    print_molecule('cysteine')
    print_molecule('tryptophan')
    print_molecule('adenine')
    print_molecule('adenosine triphosphate')

def print_reaction(name):
    m = reactions[name]
    print '%s: %s' % (m, m.equation_str)

def reaction_test1():
    print '\n*** Reaction ***'
    print_reaction('reaction1')
    print_reaction('reaction2')
    print_reaction('reaction3')
    print_reaction('reaction4')



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
    stoichiobinmatrix_test1()


    # ====================
    # Chemical tests
    # ====================

    element_test1()
    molecule_test1()
    reaction_test1()
    
