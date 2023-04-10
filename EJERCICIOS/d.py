class Ventana:
    def __init__(self, pared, superficie):
        self.pared = pared
        self.superficie = superficie
        self.pared.ventanas.append(self)

class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion

    def superficie_acristalada(self):  
     return sum([ventana.superficie for ventana in self.ventanas])

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_acristalada(self):
        return sum([pared.superficie_acristalada() for pared in self.paredes])


pared_norte = Pared("NORTE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")
pared_oeste = Pared("OESTE")

ventana_norte = Ventana(pared_norte, 0.5)
ventana_sur = Ventana(pared_sur, 2)
ventana_este = Ventana(pared_este, 1)
ventana_oeste = Ventana(pared_oeste, 1)

casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
