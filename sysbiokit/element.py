# John Eargle
# 2016


# Element and Molecule information


class Element():
    """
    Readonly information for a chemical element.
    """

    def __init__(self, name, symbol, atomic_number):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number

    def __str__(self):
        return str(self.name)


elements = {
    e.symbol: e
    for e in [
            Element('hydrogen', 'H', 1),
            Element('helium', 'He', 2),
            Element('lithium', 'Li', 3),
            Element('beryllium', 'Be', 4),
            Element('boron', 'B', 5),
            Element('carbon', 'C', 6),
            Element('nitrogen', 'N', 7),
            Element('oxygen', 'O', 8),
            Element('fluorine', 'F', 9),
            Element('neon', 'Ne', 10),
            Element('sodium', 'Na', 11),
            Element('magnesium', 'Mg', 12),
            Element('aluminum', 'Al', 13),
            Element('silicon', 'Si', 14),
            Element('phosphorus', 'P', 15),
            Element('sulfur', 'S', 16),
            Element('chlorine', 'Cl', 17),
            Element('argon', 'Ar', 18),
            Element('potassium', 'K', 19),
            Element('calcium', 'Ca', 20),
            Element('manganese', 'Mn', 25),
            Element('iron', 'Fe', 26),
            Element('copper', 'Cu', 29),
            Element('zinc', 'Zn', 30),
            Element('selenium', 'Se', 34),
            Element('bromine', 'Br', 35),
    ]
}


class Molecule():
    """
    Readonly information for a molecule.
    """

    def __init__(self, name, composition, charge=0):
        """
        The chemical composition is a list of (Element, number) tuples.
        The formula is a string built from the composition.
        """
        self.name = name
        self.composition = [(elements[c[0]], c[1]) for c in composition]
        self.charge = charge
        self.formula = ''.join(['%s%d' % (c[0].symbol, c[1]) for c in self.composition])

    def __str__(self):
        return str(self.name)


molecules = {
    m.name: m
    for m in [
            Molecule('water', [('H', 2), ('O', 1)]),
            Molecule('citrate', [('C', 6), ('H', 5), ('O', 7)]),
            Molecule('glucose', [('C', 6), ('H', 12), ('O', 6)]),
            Molecule('glucose-6-phosphate',
                     [('C', 6), ('H', 11), ('O', 9), ('P', 1)]),
            Molecule('fructose-6-phosphate',
                     [('C', 6), ('H', 11), ('O', 9), ('P', 1)]),
            Molecule('fructose-1,6-phosphate',
                     [('C', 6), ('H', 10), ('O', 12), ('P', 2)]),
            Molecule('dihydroxyacetone phosphate',
                     [('C', 3), ('H', 5), ('O', 6), ('P', 1)]),
            Molecule('glyceraldehyde-3-phosphate',
                     [('C', 3), ('H', 5), ('O', 6), ('P', 1)]),
            Molecule('1,3-diphosphoglycerate',
                     [('C', 3), ('H', 4), ('O', 10), ('P', 2)]),
            Molecule('2,3-diphosphoglycerate',
                     [('C', 3), ('H', 3), ('O', 10), ('P', 2)]),
            Molecule('2-phosphoglycerate',
                     [('C', 3), ('H', 4), ('O', 7), ('P', 1)]),
            Molecule('3-phosphoglycerate',
                     [('C', 3), ('H', 4), ('O', 7), ('P', 1)]),
            Molecule('phosphoenolpyruvate',
                     [('C', 3), ('H', 5), ('O', 6), ('P', 1)]),
            Molecule('pyruvate',
                     [('C', 3), ('H', 3), ('O', 3)]),
            Molecule('lactate',
                     [('C', 3), ('H', 5), ('O', 3)]),
            Molecule('6-phosphogluco-lactone',
                     [('C', 6), ('H', 9), ('O', 9), ('P', 1)]),
            Molecule('6-phosphogluconate',
                     [('C', 6), ('H', 10), ('O', 10), ('P', 1)]),
            Molecule('ribulose-5-phosphate',
                     [('C', 5), ('H', 9), ('O', 8), ('P', 1)]),
            Molecule('xylulose-5-phosphate',
                     [('C', 5), ('H', 9), ('O', 8), ('P', 1)]),
            Molecule('ribose-1-phosphate',
                     [('C', 5), ('H', 9), ('O', 8), ('P', 1)]),
            Molecule('ribose-5-phosphate',
                     [('C', 5), ('H', 9), ('O', 8), ('P', 1)]),
            Molecule('5-phosphoribosyl 1-pyrophosphate',
                     [('C', 5), ('H', 8), ('O', 14), ('P', 3)]),
            Molecule('erythrose-4-phosphate',
                     [('C', 4), ('H', 7), ('O', 7), ('P', 1)]),
            Molecule('sedoheptulose-7-phosphate',
                     [('C', 7), ('H', 13), ('O', 10), ('P', 1)]),
            Molecule('inosine',
                     [('C', 10), ('H', 12), ('N', 4), ('O', 5)]),
            Molecule('inosine monophosphate',
                     [('C', 10), ('H', 12), ('N', 4), ('O', 8), ('P', 1)]),
            Molecule('hypoxanthine',
                     [('C', 5), ('H', 4), ('N', 4), ('O', 1)]),
    ]
}
