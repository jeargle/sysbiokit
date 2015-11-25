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

    def __init__(self, name, const_rate=0.0, self_rate=0.0,
                 initial_val=0.0, product_type='protein'):
        self.name = name
        self.const_rate = const_rate
        self.self_rate = self_rate
        self.initial_val = initial_val
        self.product_type = product_type
        self.parents = []
        self.children = []
        self.switches = []
        self.solved = False
        self.breaks = []

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

        for s in self.switches:
            self.breaks = s.get_breaks()
        if len(self.breaks) == 0:
            self.breaks = [(0.0, True)]
        
    def report(self):
        """
        Print information about the current state of SimpleProduct.
        """
        print '%s %s' % (self.product_type, self.name)
        print '  initial value: %.2f' % (self.initial_val)
        if self.self_rate > -0.00001 and self.self_rate < 0.00001:
            print '  dX(t)/dt = %.2f' % (self.const_rate)
        else:
            if self.self_rate > 0.0:
                print '  dX(t)/dt = %.2f + %.2fX' % (self.const_rate, self.self_rate)
            else:
                print '  dX(t)/dt = %.2f - %.2fX' % (self.const_rate, -self.self_rate)
            print '  steady state = %.2f' % (-self.const_rate/self.self_rate)
            print '  reaction time = %.2f' % (-np.log(2.0)/self.self_rate)
            
    def plot(self, start, end, step):
        """
        Plot the concentration of LogicProduct over time.
        """
        if not self.solved:
            self.solve()
        if self.self_rate > -0.00001 and self.self_rate < 0.00001:
            t = np.arange(start, end, step)
            y = self.const_rate * t
        else:
            steady_rate = -self.const_rate/self.self_rate
            rx_t = -np.log(2.0)/self.self_rate
            t = np.arange(start, end, step)
            on_func = lambda y, z: lambda x: steady_rate + (y - steady_rate) * np.exp(self.self_rate*(x-z))
            off_func = lambda y, z: lambda x: y * np.exp(self.self_rate*(x-z))

            # Build ranges
            ranges = [t<self.breaks[0][0]]
            for i in range(1, len(self.breaks)):
                ranges.append((t>=self.breaks[i-1][0]) * (t<self.breaks[i][0]))
            ranges.append(t>=self.breaks[-1][0])

            # Build lambdas
            active = self.breaks[0][1]
            vals = [self.initial_val]
            last_val = self.initial_val
            for i in range(len(self.breaks)-1):
                print 'i:', i
                print 'break:', self.breaks[i][0]
                if active:
                    vals.append(on_func(last_val, self.breaks[i][0]))
                    last_val = on_func(last_val, self.breaks[i][0])(self.breaks[i+1][0])
                else:
                    vals.append(off_func(last_val, self.breaks[i][0]))
                    last_val = off_func(last_val, self.breaks[i][0])(self.breaks[i+1][0])
                active = not active
                print 'last_val:', last_val
            if active:
                vals.append(on_func(last_val, self.breaks[-1][0]))
            else:
                vals.append(off_func(last_val, self.breaks[-1][0]))
            y = np.piecewise(t, ranges, vals)
            
        plt.plot(t, y)
        plt.show()



class Switch():
    """
    Switch that turns a LogicProduct on or off depending on the
    concentration of some parent LogicProduct.
    """
    
    def __init__(self, parent=None, child=None, threshold=0.0,
                 activate=True, times=[0.0]):
        self.parent = parent
        self.child = child
        self.threshold = threshold
        self.activate = activate
        self.time = []
        self.solved = False

        if parent is None:
            self.times = times
            self.solved = True

    def solve(self):
        pass

    def get_breaks(self):
        breaks = []
        flip = self.activate
        for t in self.times:
            breaks.append((t, flip))
            flip = not flip
        return breaks

    def __str__(self):
        
        str1 = 'Switch\n'
        str1 += 'activate: ' + str(self.activate) + '\n'
        str1 += '  solved: ' + str(self.solved) + '\n'
        str1 += '  breaks:\n'
        str1 += '  ' +  str(self.get_breaks()) + '\n'
        return str1
