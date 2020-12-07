# Program za računanje z binarnimi relacijami
# Iztok Bajcar, 2020
import time

def impl(a, b):  # implikacija; ali iz a sledi b?
    return not a or b

class Relacija:
    def __init__(self, r, dfn):
        self.r = r
        self.dfn = dfn
        self.refleksivna    = None
        self.irefleksivna   = None
        self.simetricna     = None
        self.asimetricna    = None
        self.antisimetricna = None
        self.tranzitivna    = None
        self.itranzitivna   = None
        self.sovisna        = None
        self.strogosovisna  = None
        self.enolicna       = None

    # LASTNOSTI RELACIJ
    def ref(self):  # refleksivna  xRx
        if self.refleksivna == None:
            for i in self.dfn:
                if not self.r(i, i):
                    self.refleksivna = False
                    return False
            self.refleksivna = True
            return True
        else:
            return self.refleksivna

    def iref(self):  # irefleksivna  !(xRx)
        if self.irefleksivna == None:
            for i in self.dfn:
                if self.r(i, i):
                    self.irefleksivna = False
                    return False
            self.irefleksivna = True
            return True
        else:
            return self.irefleksivna

    def sim(self):  # simetrična  xRy => yRx
        if self.simetricna == None:
            for x in self.dfn:
                for y in self.dfn:
                    if not (impl(self.r(x, y), self.r(y, x))):
                        self.simetricna = False
                        return False
            self.simetricna = True
            return True
        else:
            return self.simetricna

    def asim(self):  # asimetrična  xRy => !(yRx)
        if self.asimetricna == None:
            for x in self.dfn:
                for y in self.dfn:
                    if not (impl(self.r(x, y), not self.r(y, x))):
                        self.asimetricna = False
                        return False
            self.asimetricna = True
            return True
        else:
            return self.asimetricna

    def antisim(self):  # antisimetrična  xRy ^ yRx => x = y
        if self.antisimetricna == None:
            for x in self.dfn:
                for y in self.dfn:
                    if not (impl(self.r(x, y) and self.r(y, x), x == y)):
                        self.antisimetricna = False
                        return False
            self.antisimetricna = True
            return True
        else:
            return self.antisimetricna

    def tranz(self):  # tranzitivna  xRy ^ yRz => xRz
        if self.tranzitivna == None:
            for x in self.dfn:
                for y in self.dfn:
                    for z in self.dfn:
                        if not (impl(self.r(x, y) and self.r(y, z), self.r(x, z))):
                            self.tranzitivna = False
                            return False
            self.tranzitivna = True
            return True
        else:
            return self.tranzitivna

    def itranz(self):  # itranzitivna  xRy ^ yRz => !(xRz)
        if self.itranzitivna == None:
            for x in self.dfn:
                for y in self.dfn:
                    for z in self.dfn:
                        if not (impl(self.r(x, y) and self.r(y, x), not self.r(x, z))):
                            self.itranzitivna = False
                            return False
            self.itranzitivna = True
            return True
        else:
            return self.itranzitivna

    def sovis(self):  # sovisna  x != y => xRy v yRx
        if self.sovisna == None:
            for x in self.dfn:
                for y in self.dfn:
                    if not (impl(x != y, self.r(x, y) or self.r(y, x))):
                        self.sovisna = False
                        return False
            self.sovisna = True
            return True
        else:
            return self.sovisna

    def st_sovis(self):  # strogo sovisna  xRy v yRx
        if self.strogosovisna == None:
            for x in self.dfn:
                for y in self.dfn:
                    if not (self.r(x, y) or self.r(y, x)):
                        self.strogosovisna = False
                        return False
            self.strogosovisna = True
            return True
        else:
            return self.strogosovisna

    def enol(self):  # enolična  xRy ^ xRz => y == z
        if self.enolicna == None:
            for x in self.dfn:
                for y in self.dfn:
                    for z in self.dfn:
                        if not (impl(self.r(x, y) and self.r(x, z), y == z)):
                            self.enolicna = False
                            return False
            self.enolicna = True
            return True
        else:
            return self.enolicna

    def izracunaj(self):  # Izračuna vse lastnosti relacije vnaprej in vrne čas, ki je bil potreben za izračun, v sekundah
        t = time.time()
        self.ref()
        self.iref()
        self.sim()
        self.asim()
        self.antisim()
        self.tranz()
        self.itranz()
        self.sovis()
        self.st_sovis()
        self.enol()
        return time.time() - t

    def ekviv(self):  # ali je ekvivalenčna relacija
        return self.ref() and self.sim() and self.tranz()

    def delno_ureja(self):  # ali je relacija delna urejenost
        return self.ref() and self.antisim() and self.tranz()

    def linearno_ureja(self):  # ali je relacija linearna urejenost
        return self.delno_ureja() and self.sovis()

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
