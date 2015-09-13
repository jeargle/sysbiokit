# John Eargle
# 2015

import sys
import json

import matplotlib.pyplot as plt
import numpy as np
# import sympy



def heaviside(x, theta, on=True):
    """
    Zero out values of x<theta.
    """
    # return 0.5 * (np.sign(x-theta) + 1.0)
    vals = [0.0, 1.0]
    if not on:
        vals = [1.0, 0.0]
    return np.piecewise(x, [x<theta, x>=theta], vals)


def time_plot(duration):
    x = np.arange(0, duration, 0.1)
    y = heaviside(x, duration/5.0) * np.sin(x) * np.exp(-x/20.0) * 5.0
    plt.plot(x, y)
    plt.show()


class SimpleProduct():
    """
    Product that is simply regulated by an on/off switch.
    """

    def __init__(self, name, const_rate=0.0, self_rate=0.0, product_type='protein'):
        self.name = name
        self.const_rate = const_rate
        self.self_rate = self_rate
        self.product_type = product_type

    def report(self):
        """
        Print information about the current state of SimpleProduct.
        """
        print '%s %s' % (self.product_type, self.name)
        if self.self_rate > -0.00001 and self.self_rate < 0.00001:
            print '  dX(t)/dt = %.2f' % (self.const_rate)
        else:
            if self.self_rate > 0.0:
                print '  dX(t)/dt = %.2f + %.2fX' % (self.const_rate, self.self_rate)
            else:
                print '  dX(t)/dt = %.2f - %.2fX' % (self.const_rate, -self.self_rate)
            print '  steady state = %.2f' % (-self.const_rate/self.self_rate)
            print '  reaction time = %.2f' % (-np.log(2.0)/self.self_rate)
            
    def plot(self):
        """
        Plot the concentration of SimpleProduct over time.
        """
        if self.self_rate > -0.00001 and self.self_rate < 0.00001:
            t = np.arange(0, 10, 0.1)
            y = self.const_rate * t
        else:
            steady_rate = -self.const_rate/self.self_rate
            rx_t = -np.log(2.0)/self.self_rate
            duration = rx_t*4.0
            t = np.arange(0, duration, duration/50.0)
            y = steady_rate * (1.0 - np.exp(self.self_rate*t))
        plt.plot(t, y)
        plt.show()


class LogicProduct():
    """
    Product that is regulated by on/off switches possibly controlled
    by the concentrations of other LogicProducts.
    """

    def __init__(self, name, const_rate=0.0, self_rate=0.0, product_type='protein'):
        self.name = name
        self.const_rate = const_rate
        self.self_rate = self_rate
        self.product_type = product_type
        self.parents = []
        self.children = []
        self.switches = []
        self.solved = False

    def add_child(self, child, threshold, activate=True):
        self.children.append(child)
        child.parents.append(self)
        child.add_switch(Switch(self, child, threshold, activate))

    def add_switch(self, switch):
        self.switches.append(switch)

    def solve(self):
        """
        Check that the parents are solved and then generate needed
        parameters for plotting the trajectory of this product's
        concentration.
        """
        for p in self.parents:
            if not p.solved:
                p.solve()

        for s in self.switches:
            if not s.solved:
                s.solve()
        
        
    def report(self):
        """
        Print information about the current state of SimpleProduct.
        """
        print '%s %s' % (self.product_type, self.name)
        if self.self_rate > -0.00001 and self.self_rate < 0.00001:
            print '  dX(t)/dt = %.2f' % (self.const_rate)
        else:
            if self.self_rate > 0.0:
                print '  dX(t)/dt = %.2f + %.2fX' % (self.const_rate, self.self_rate)
            else:
                print '  dX(t)/dt = %.2f - %.2fX' % (self.const_rate, -self.self_rate)
            print '  steady state = %.2f' % (-self.const_rate/self.self_rate)
            print '  reaction time = %.2f' % (-np.log(2.0)/self.self_rate)
            
    def plot(self):
        """
        Plot the concentration of SimpleProduct over time.
        """
        if self.self_rate > -0.00001 and self.self_rate < 0.00001:
            t = np.arange(0, 10, 0.1)
            y = self.const_rate * t
        else:
            steady_rate = -self.const_rate/self.self_rate
            rx_t = -np.log(2.0)/self.self_rate
            duration = rx_t*8.0
            t = np.arange(0, duration, duration/50.0)
            y = steady_rate * (1.0 - np.exp(self.self_rate*t))
        plt.plot(t, y)
        plt.show()


class Switch():
    """
    Switch that turns a LogicProduct on or off depending on the
    concentration of some parent LogicProduct.
    """
    
    def __init__(self, parent, child, threshold, activate=True, time=0.0):
        self.parent = parent
        self.child = child
        self.threshold = threshold
        self.activate = activate

        if parent is not None:
            self.time = time
        else:
            self.time = None

    def solve(self):
        pass



if __name__=='__main__':

    # time_plot(30)

    # SimpleProduct test
    # sp1 = SimpleProduct('Y', 2.0, -0.5)
    # sp1.report()
    # sp1.plot()

    # LogicProduct test
    lp1 = LogicProduct('Y', 2.0, -0.5)
    lp1.report()
    lp1.plot()
