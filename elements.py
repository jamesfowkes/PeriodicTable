symbols = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Ni", "Co", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "I", "Te", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Pa", "Th", "Np", "U", "Am", "Pu", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Rf", "Lr", "Db", "Bh", "Sg", "Mt", "Rg", "Hs", "Ds", "Uub", "Uut", "Uuq", "Uup", "Uuh", "Uus", "Uuo"]

masses = [1.0079, 4.0026, 6.941, 9.0122, 10.811, 12.0107, 14.0067, 15.9994, 18.9984, 20.1797, 22.9897, 24.305, 26.9815, 28.0855, 30.9738, 32.065, 35.453, 39.0983, 39.948, 40.078, 44.9559, 47.867, 50.9415, 51.9961, 54.938, 55.845, 58.6934, 58.9332, 63.546, 65.39, 69.723, 72.64, 74.9216, 78.96, 79.904, 83.8, 85.4678, 87.62, 88.9059, 91.224, 92.9064, 95.94, 98, 101.07, 102.9055, 106.42, 107.8682, 112.411, 114.818, 118.71, 121.76, 126.9045, 127.6, 131.293, 132.9055, 137.327, 138.9055, 140.116, 140.9077, 144.24, 145, 150.36, 151.964, 157.25, 158.9253, 162.5, 164.9303, 167.259, 168.9342, 173.04, 174.967, 178.49, 180.9479, 183.84, 186.207, 190.23, 192.217, 195.078, 196.9665, 200.59, 204.3833, 207.2, 208.9804, 209, 210, 222, 223, 226, 227, 231.0359, 232.0381, 237, 238.0289, 243, 244, 247, 247, 251, 252, 257, 258, 259, 261, 262, 262, 264, 266, 268, 272, 277, 0, 0, 0, 0, 0, 0, 0, 0]

blanks = {1:16, 4:10, 12:10, 56:1, 88:1}

types = {
    "alkalis" : [3, 11, 19, 37, 55, 87],
    "alkaline_earths" : [4, 12, 20, 38, 56, 88],
    "transistion_metals" : range(21, 31) + range(39, 49) + range(72, 81) + range(104, 113),
    "basic_metals" : [13, 31, 49, 50, 81, 82, 83, 113, 114, 115, 116],
    "semimetals" : [5, 14, 32, 33, 51, 52, 84],
    "nonmetals" : [1, 6, 7, 8, 15, 16, 34],
    "halogens" : [9, 17, 35, 53, 85, 117],
    "noble_gases" : [2, 10, 18, 36, 54, 86, 118],
    "actinides" : range(89, 104),
    "lanthanides" : range(57, 72)
}
endofrow = [2, 10, 18, 36, 54, 86, 118]

MaxAtomicNumber = 118

class Element:
    def __init__(self, a):
        self.a = a
        self.symbol = symbols[a-1]
        self.raw_mass = masses[a-1]
        try:
            self.following_blanks = blanks[a]
        except KeyError:
            self.following_blanks = 0
        self.endofrow = a in endofrow
    
    @property
    def mass(self):
        if (self.raw_mass > 0):
            return "%.2f" % self.raw_mass
        else:
            return "?"
    
    @property        
    def is_actinide(self):
        return self.a in types['actinides']
        
    @property        
    def is_lanthanide(self):
        return self.a in types['lanthanides']
    
    @property
    def is_normal(self):
        return (not self.is_actinide and not self.is_lanthanide)
    
    @property
    def is_metal(self):
        return self.a in metals

    @property
    def type(self):
        for type, weights in types.iteritems():
            if self.a in weights:
                return type
        
def GetTypes():
    return types.keys()
    
def GetNormalElements():
    return [ele for ele in AllElements() if ele.is_normal]

def GetActinides():
    return [ele for ele in AllElements() if ele.is_actinide]

def GetLanthanides():
    return [ele for ele in AllElements() if ele.is_lanthanide]

def AllElements():    
    return [Element(i) for i in range(1, MaxAtomicNumber+1)]