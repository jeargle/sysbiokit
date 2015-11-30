# John Eargle
# 2015

import sys
import json

import matplotlib.pyplot as plt
import numpy as np
# import sympy


# Regulation
#   negative: repression (gene), inhibition (protein)
#   positive: induction (gene), activation (protein)


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
        Calculate and plot the concentration of SimpleProduct over time.
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
    Acts as a node in a transcription network.
    """

    def __init__(self, name, const_rate=0.0, self_rate=0.0,
                 initial_val=0.0, product_type='protein'):
        """
        name: name for this specific node in the network
        const_rate: 
        self_rate: 
        initial_val: starting concentration (default 0.0)
        product_type: RNA, protein (just a label)
        breaks: array of switch times
        vals: array of functions
        """
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
        self.vals = []

    def add_child(self, child, threshold, activate=True):
        """
        Add a downstream node.  This sets up a Switch that will control the
        child based on the state of the parent.
        """
        self.children.append(child)
        child.parents.append(self)
        child.add_switch(Switch(self, child, threshold, activate))

    def add_switch(self, switch):
        """
        Used to connect to a parent.  Only called by self.add_child().
        """
        self.switches.append(switch)
        self.solved = False

    def solve(self):
        """
        Check that the parents are solved and then generate needed
        parameters for plotting the trajectory of this product's
        concentration.
        """
        # TODO - handle cyclic dependencies (choose starting nodes)
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

        # Get piecewise ranges and function for each piece
        if self.self_rate <= -0.00001 or self.self_rate >= 0.00001:
            steady_rate = -self.const_rate/self.self_rate

            # Functions for turning the product on or off
            on_func = lambda y, z: lambda x: steady_rate + (y - steady_rate) * np.exp(self.self_rate*(x-z))
            off_func = lambda y, z: lambda x: y * np.exp(self.self_rate*(x-z))

            # Build lambdas
            active = self.breaks[0][1]
            self.vals = [self.initial_val]
            last_val = self.initial_val
            for i, brk in enumerate(self.breaks[0:-1]):
                print 'i:', i
                print 'brk:', brk[0]
                if active:
                    self.vals.append(on_func(last_val, brk[0]))
                    last_val = on_func(last_val, brk[0])(self.breaks[i+1][0])
                else:
                    self.vals.append(off_func(last_val, brk[0]))
                    last_val = off_func(last_val, brk[0])(self.breaks[i+1][0])
                active = not active
                # print 'last_val:', last_val
            if active:
                self.vals.append(on_func(last_val, self.breaks[-1][0]))
            else:
                self.vals.append(off_func(last_val, self.breaks[-1][0]))

        print 'len(breaks):', len(self.breaks)
        print 'len(vals):', len(self.vals)
        self.solved = True

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
        
        t = np.arange(start, end, step)
        if self.self_rate > -0.00001 and self.self_rate < 0.00001:
            y = self.const_rate * t
        else:
            # Build ranges
            ranges = [t<self.breaks[0][0]]
            for i in range(1, len(self.breaks)):
                ranges.append((t>=self.breaks[i-1][0]) * (t<self.breaks[i][0]))
            ranges.append(t>=self.breaks[-1][0])
            
            y = np.piecewise(t, ranges, self.vals)
            
        plt.plot(t, y)
        plt.show()


class Switch():
    """
    Switch that turns a LogicProduct on or off depending on the
    concentration of some parent LogicProduct.
    Acts as an edge in a transcription network.
    Essentially, a Switch looks at the time varying concentration of its parent
    node and produces a list of timepoints where the Switch turns on or off.
    This sequence of timepoints can then be passed to the child node so that it
    can determine its own concentration trajectory.
    """
    
    def __init__(self, parent=None, child=None, threshold=0.0,
                 activate=True, times=[0.0]):
        """
        parent: upstream node
        child: downstream noe
        threshold: parent concentration value where Switch switches on/off
        activate: whether the Switch is an activator (on) or inhibitor (off)
        times: set sequence of times when Switch switches (if no parent defined)
        """
        self.parent = parent
        self.child = child
        self.threshold = threshold
        self.activate = activate
        self.solved = False

        if parent is None:
            self.times = times
            self.solved = True

    def solve(self):
        if parent is None:
            return

        if not parent.solved:
            parent.solve()

        # Get switching times based on parent functional form
        
        
        self.solved = True

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
