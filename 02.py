class Quadrado:

    def __init__(self, lado):
        self.setLado(lado)

    def setLado(self, lado):
        self.lado = lado

    def getLado(self):
        return self.lado

    def calculaArea(self):
        return self.lado * self.lado


quadrado = Quadrado(4)
print (quadrado.calculaArea())

quadrado.setLado(2)
print (quadrado.calculaArea())