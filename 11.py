class Carro:

    def __init__(self, quilometrosLitro):
        self.quilometrosLitro = quilometrosLitro
        self.qtdeCombustivel = 0

    def adicionarGasolina(self, quantidade):
        self.qtdeCombustivel += float(quantidade)

    def andar(self, distancia):
        gasto = distancia / self.quilometrosLitro
        self.qtdeCombustivel -= gasto

    def obterGasolina(self):
        print (self.qtdeCombustivel)


fiat = Carro(15)
fiat.adicionarGasolina(20)
fiat.andar(100)
fiat.obterGasolina()