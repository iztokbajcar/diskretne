# Program za računanje z binarnimi relacijami
# Iztok Bajcar, 2020

"""
PRIMER RELACIJE:

def rel(a, b):  # def. relacije
    return (a % 2 == 0 and b % 2 == 1)
"""
def impl(a, b):  # implikacija; ali iz a sledi b?
    return not a or b

class Relacija:
    def __init__(self, r, dfn):
        self.r = r
        self.dfn = dfn

    # LASTNOSTI RELACIJ
    def ref(self):  # refleksivna  xRx
        for i in self.dfn:
            if not self.r(i, i):
                return False
        return True

    def iref(self):  # irefleksivna  !(xRx)
        for i in self.dfn:
            if self.r(i, i):
                return False
        return True

    def sim(self):  # simetrična  xRy => yRx
        for x in self.dfn:
            for y in self.dfn:
                if not (impl(self.r(x, y), self.r(y, x))):
                    return False
        return True

    def asim(self):  # asimetrična  xRy => !(yRx)
        for x in self.dfn:
            for y in self.dfn:
                if not (impl(self.r(x, y), not self.r(y, x))):
                    return False
        return True

    def antisim(self):  # antisimetrična  xRy ^ yRx => x = y
        for x in self.dfn:
            for y in self.dfn:
                if not (impl(self.r(x, y) and self.r(y, x), x == y)):
                    return False
        return True

    def tranz(self):  # tranzitivna  xRy ^ yRz => xRz
        for x in self.dfn:
            for y in self.dfn:
                for z in self.dfn:
                    if not (impl(self.r(x, y) and self.r(y, z), self.r(x, z))):
                        return False
        return True

    def itranz(self):  # itranzitivna  xRy ^ yRz => !(xRz)
        for x in self.dfn:
            for y in self.dfn:
                for z in self.dfn:
                    if not (impl(self.r(x, y) and self.r(y, x), not self.r(x, z))):
                        return False
        return True

    def sovis(self):  # sovisna  x != y => xRy v yRx
        for x in self.dfn:
            for y in self.dfn:
                if not (impl(x != y, self.r(x, y) or self.r(y, x))):
                    return False
        return True

    def st_sovis(self):  # strogo sovisna  xRy v yRx
        for x in self.dfn:
            for y in self.dfn:
                if not (self.r(x, y) or self.r(y, x)):
                    return False
        return True

    def enol(self):
        for x in self.dfn:
            for y in self.dfn:
                for z in self.dfn:
                    if not (impl(self.r(x, y) and self.r(x, z), y == z)):
                        return False
        return True

    def seznam(self):  # vrne seznam parov z dfn, ki so v medsebojni relaciji
        rez = []
        #print(self.dfn)
        for x in self.dfn:
            for y in self.dfn:
                if (self.r(x, y)):
                    rez.append([x, y])
                    #print([x, y])
        return rez

    def lastnosti(self):  # izpiše lastnosi relacije na def. območju
        print("Refleksivna:    " + str(self.ref()))
        print("Irefleksivna:   " + str(self.iref()))
        print("Simetrična:     " + str(self.sim()))
        print("Asimetrična:    " + str(self.asim()))
        print("Antisimetrična: " + str(self.antisim()))
        print("Tranzitivna:    " + str(self.tranz()))
        print("Itranzitivna:   " + str(self.itranz()))
        print("Sovisna:        " + str(self.sovis()))
        print("Strogo sovisna: " + str(self.st_sovis()))
        print("Enolična:       " + str(self.enol()))

    # OPERACIJE
    def produkt(self, rel):
        pravilo = []
        for x in self.dfn:
            for y in self.dfn:
                if y in rel.dfn:
                    for z in rel.dfn:
                        if self.r(x, y) and rel.r(y, z) and not [x, z] in pravilo:
                            pravilo.append([x, z])
        def r(x, y):
            if ([x, y] in pravilo):
                return True
            return False
        
        return Relacija(r, self.dfn)

    def inverzna(self):
        pravilo = self.seznam()
        def r(x, y):
            if [y, x] in pravilo:
                return True
            return False
        return Relacija(r, self.dfn)

    def potenca(self, n):  # R^n
        pravilo = []
        for i in self.dfn:
            pravilo.append([i, i])

        def r(x, y):
            if [x, y] in pravilo:
                return True
            return False

        rez = Relacija(r, self.dfn)  # relacija identitete
        if n < 0:
            rel = self.inverzna()
        else:
            rel = self

        for i in range(abs(n)):
            rez = rez.produkt(rel)
        return rez



# Test
"""def r(x, y):
    if (x * 3 - y) % (x + y + 1) == 0:
        return True
    return False

rel = Relacija(r, [1, 2, 3, 4, 5, 6, 7, 8])
rel.lastnosti()
print(rel.seznam())
print(rel.produkt(rel).seznam())
print(rel.potenca(3).seznam())

print(rel.inverzna().seznam())
print(rel.potenca(-1).seznam())
print(rel.potenca(-2).seznam())
"""
