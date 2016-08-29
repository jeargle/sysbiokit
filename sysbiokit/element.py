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
    'H': Element('hydrogen', 'H', 1),
    'He': Element('helium', 'He', 2),
    'Li': Element('lithium', 'Li', 3),
    'Be': Element('beryllium', 'Be', 4),
    'B': Element('boron', 'B', 5),
    'C': Element('carbon', 'C', 6),
    'N': Element('nitrogen', 'N', 7),
    'O': Element('oxygen', 'O', 8),
    'F': Element('fluorine', 'F', 9),
    'Ne': Element('neon', 'Ne', 10),
    'Na': Element('sodium', 'Na', 11),
    'Mg': Element('magnesium', 'Mg', 12),
    'Al': Element('aluminum', 'Al', 13),
    'Si': Element('silicon', 'Si', 14),
    'P': Element('phosphorus', 'P', 15),
    'S': Element('sulfur', 'S', 16),
    'Cl': Element('chlorine', 'Cl', 17),
    'Ar': Element('argon', 'Ar', 18),
    'K': Element('potassium', 'K', 19),
    'Ca': Element('calcium', 'Ca', 20),
    'Mn': Element('manganese', 'Mn', 25),
    'Fe': Element('iron', 'Fe', 26),
    'Cu': Element('copper', 'Cu', 29),
    'Zn': Element('zinc', 'Zn', 30),
    'Se': Element('selenium', 'Se', 34),
    'Br': Element('bromine', 'Br', 35),
}


class Molecule():
    """
    Readonly information for a molecule.
    """

    def __init__(self, name, composition):
        """
        The chemical composition is a list of (Element, number) tuples.
        The formula is a string built from the composition.
        """
        self.name = name
        self.composition = composition
        self.formula = ''.join(['%s%d' % (c[0].symbol, c[1]) for c in self.composition])

    def __str__(self):
        return str(self.name)


molecules = {
    'water': Molecule('water', [(elements['H'], 2), (elements['O'], 1)]),
    'citrate': Molecule('citrate', [(elements['C'], 6), (elements['H'], 5), (elements['O'], 7)]),
}
