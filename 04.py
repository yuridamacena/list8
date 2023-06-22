
class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        if (peso > self.peso):
            self.peso = 0
        else:
            self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def envelhecer(self, anos):
        anosAntes = self.idade
        self.idade += anos
        if (anosAntes < 25):
            if (self.idade < 25):
                self.crescer(anos * 0.5)
            else:
                self.crescer((25 - anosAntes) * 0.5)



yuri= Pessoa('yuri', 20, 87.0, 190)
print(vars(yuri))
yuri.engordar(1)
print(vars(yuri))
yuri.emagrecer(2)
print(vars(yuri))
yuri.crescer(3)
print(vars(yuri))
yuri.envelhecer(7)
print(vars(yuri))