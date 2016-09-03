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

    def __init__(self, name, composition, charge=0, abbr=None):
        """
        The chemical composition is a list of (Element, number) tuples.
        The formula is a string built from the composition.
        """
        self.name = name
        if abbr is not None:
            self.abbr = abbr
        else:
            self.abbr = self.name
        self.composition = [(elements[c[0]], c[1]) for c in composition]
        self.charge = charge
        self.formula = ''.join(['%s%d' % (c[0].symbol, c[1]) for c in self.composition])

    def __str__(self):
        return str(self.name)

    @property
    def charge_str(self):
        s = ''
        if self.charge == 0:
            pass
        elif self.charge > 0:
            s = '%d+' % (self.charge)
        else:
            s = '%d-' % (-self.charge)
        return s


molecules = {
    m.name: m
    for m in [
            Molecule('hydrogen', [('H', 1)], charge=1),
            Molecule('water', [('H', 2), ('O', 1)]),
            Molecule('carbon dioxide', [('C', 1), ('O', 2)]),
            Molecule('ammonia', [('N', 1), ('H', 3)]),
            Molecule('ammonium', [('N', 1), ('H', 4)], charge=1),
            Molecule('phosphate', [('H', 1), ('P', 1), ('O', 4)], charge=1, abbr='Pi'),
            # Small-molecule metabolites
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
            # Amino acids
            Molecule('alanine',
                     [('C', 3), ('H', 7), ('N', 1), ('O', 2)]),
            Molecule('arginine',
                     [('C', 6), ('H', 14), ('N', 4), ('O', 2)]),
            Molecule('asparagine',
                     [('C', 4), ('H', 8), ('N', 2), ('O', 3)]),
            Molecule('aspartic acid',
                     [('C', 4), ('H', 7), ('N', 1), ('O', 4)]),
            Molecule('cysteine',
                     [('C', 3), ('H', 7), ('N', 1), ('O', 2), ('S', 1)]),
            Molecule('glutamic acid',
                     [('C', 5), ('H', 9), ('N', 1), ('O', 4)]),
            Molecule('glutamine',
                     [('C', 5), ('H', 10), ('N', 2), ('O', 3)]),
            Molecule('glycine',
                     [('C', 2), ('H', 5), ('N', 1), ('O', 2)]),
            Molecule('histidine',
                     [('C', 6), ('H', 9), ('N', 3), ('O', 2)]),
            Molecule('isoleucine',
                     [('C', 6), ('H', 13), ('N', 1), ('O', 2)]),
            Molecule('leucine',
                     [('C', 6), ('H', 13), ('N', 1), ('O', 2)]),
            Molecule('lysine',
                     [('C', 6), ('H', 14), ('N', 2), ('O', 2)]),
            Molecule('methionine',
                     [('C', 5), ('H', 11), ('N', 1), ('O', 2)], ('S', 1)),
            Molecule('phenylalanine',
                     [('C', 9), ('H', 11), ('N', 1), ('O', 2)]),
            Molecule('proline',
                     [('C', 5), ('H', 9), ('N', 1), ('O', 2)]),
            Molecule('serine',
                     [('C', 3), ('H', 7), ('N', 1), ('O', 3)]),
            Molecule('threonine',
                     [('C', 4), ('H', 9), ('N', 1), ('O', 3)]),
            Molecule('tryptophan',
                     [('C', 11), ('H', 12), ('N', 2), ('O', 2)]),
            Molecule('tyrosine',
                     [('C', 9), ('H', 11), ('N', 1), ('O', 3)]),
            Molecule('valine',
                     [('C', 5), ('H', 11), ('N', 1), ('O', 2)]),
            Molecule('selenocysteine',
                     [('C', 3), ('H', 7), ('N', 1), ('O', 2), ('Se', 1)]),
            # Nucleic acids
            Molecule('adenine',
                     [('C', 5), ('H', 5), ('N', 5)]),
            Molecule('cytosine',
                     [('C', 4), ('H', 5), ('N', 3), ('O', 1)]),
            Molecule('guanine',
                     [('C', 5), ('H', 5), ('N', 5), ('O', 1)]),
            Molecule('thymine',
                     [('C', 5), ('H', 6), ('N', 2), ('O', 2)]),
            Molecule('uracil',
                     [('C', 4), ('H', 4), ('N', 2), ('O', 2)]),
            Molecule('adenosine',
                     [('C', 10), ('H', 13), ('N', 5), ('O', 4)]),
            Molecule('cytidine',
                     [('C', 9), ('H', 13), ('N', 3), ('O', 5)]),
            Molecule('guanosine',
                     [('C', 10), ('H', 13), ('N', 5), ('O', 5)]),
            Molecule('thymidine',
                     [('C', 10), ('H', 14), ('N', 2), ('O', 6)]),
            Molecule('uridine',
                     [('C', 9), ('H', 12), ('N', 2), ('O', 6)]),
            Molecule('adenosine monophosphate',
                     [('C', 10), ('H', 12), ('N', 5), ('O', 7), ('P', 1)],
                     charge=-2, abbr='AMP'),
            Molecule('cytosine monophosphate',
                     [('C', 9), ('H', 12), ('N', 3), ('O', 8), ('P', 1)],
                     charge=-2, abbr='CMP'),
            Molecule('guanine monophosphate',
                     [('C', 10), ('H', 12), ('N', 5), ('O', 8), ('P', 1)],
                     charge=-2, abbr='GMP'),
            Molecule('thymine monophosphate',
                     [('C', 10), ('H', 13), ('N', 2), ('O', 9), ('P', 1)],
                     charge=-2, abbr='TMP'),
            Molecule('uracil monophosphate',
                     [('C', 9), ('H', 11), ('N', 2), ('O', 9), ('P', 1)],
                     charge=-2, abbr='UMP'),
            Molecule('adenosine diphosphate',
                     [('C', 10), ('H', 12), ('N', 5), ('O', 10), ('P', 2)],
                     charge=-3, abbr='ADP'),
            Molecule('cytosine diphosphate',
                     [('C', 9), ('H', 12), ('N', 3), ('O', 11), ('P', 2)],
                     charge=-3, abbr='CDP'),
            Molecule('guanine diphosphate',
                     [('C', 10), ('H', 12), ('N', 5), ('O', 11), ('P', 2)],
                     charge=-3, abbr='GDP'),
            Molecule('thymine diphosphate',
                     [('C', 10), ('H', 13), ('N', 2), ('O', 12), ('P', 2)],
                     charge=-3, abbr='TDP'),
            Molecule('uracil diphosphate',
                     [('C', 9), ('H', 11), ('N', 2), ('O', 12), ('P', 2)],
                     charge=-3, abbr='UDP'),
            Molecule('adenosine triphosphate',
                     [('C', 10), ('H', 12), ('N', 5), ('O', 13), ('P', 3)],
                     charge=-4, abbr='ATP'),
            Molecule('cytosine triphosphate',
                     [('C', 9), ('H', 12), ('N', 3), ('O', 14), ('P', 3)],
                     charge=-4, abbr='CTP'),
            Molecule('guanine triphosphate',
                     [('C', 10), ('H', 12), ('N', 5), ('O', 14), ('P', 3)],
                     charge=-4, abbr='GTP'),
            Molecule('thymine triphosphate',
                     [('C', 10), ('H', 13), ('N', 2), ('O', 15), ('P', 3)],
                     charge=-4, abbr='CTP'),
            Molecule('uracil triphosphate',
                     [('C', 9), ('H', 11), ('N', 2), ('O', 15), ('P', 3)],
                     charge=-4, abbr='UTP'),
            Molecule('nicotinamide adenine dinucleotide',
                     [('C', 21), ('H', 27), ('N', 7), ('O', 14), ('P', 2)],
                     abbr='NAD'),
            Molecule('nicotinamide adenine dinucleotide H',
                     [('C', 21), ('H', 28), ('N', 7), ('O', 14), ('P', 2)],
                     abbr='NADH'),
            Molecule('nicotinamide adenine dinucleotide phosphate',
                     [('C', 21), ('H', 27), ('N', 7), ('O', 17), ('P', 3)],
                     abbr='NADP'),
            Molecule('nicotinamide adenine dinucleotide phosphate H',
                     [('C', 21), ('H', 28), ('N', 7), ('O', 17), ('P', 3)],
                     abbr='NADPH'),
    ]
}
