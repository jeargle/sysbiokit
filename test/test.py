# John Eargle
# 2015

from sysbiokit.sysbiokit import SimpleProduct, LogicProduct, Switch


if __name__=='__main__':

    print '***********************'
    print '*** SYSBIOKIT TESTS ***'
    print '***********************'
    
    # time_plot(30)

    # SimpleProduct test
    print '\n*** SimpleProduct ***'
    # Linear, no product degradation
    sp1 = SimpleProduct('Y', 2.0)
    sp1.report()
    sp1.plot()

    # Product degradation (-0.5)
    sp2 = SimpleProduct('Y', 2.0, -0.5)
    sp2.report()
    sp2.plot()

    # LogicProduct test
    print '\n*** LogicProduct ***'
    lp1 = LogicProduct('Y', 2.0, -0.5)
    lp1.report()
    lp1.plot(-1.0, 20.0, 0.2)

    # Switch test
    s1 = Switch(child=lp1, times=[0.5, 0.7, 1.3])
    print s1

    s2 = Switch(child=lp1, times=[0.2, 0.4, 0.8], activate=False)
    print s2

    s3 = Switch(child=lp1, times=[2.0, 10.0, 20.0])
    print s3
    lp1.add_switch(s3)
    lp1.report()
    lp1.plot(-1.0, 40.0, 0.2)
    
