class Tamagushi:
    def __init__(self, Nome, Fome = 10, Saude = 0, Idade = 1):
        self.alt_Nome(Nome)
        self.alt_Fome(Fome)
        self.alt_Saude(Saude)
        self.alt_Idade(Idade)

    def alt_Nome(self, Nome):
        self.Nome = Nome

    def get_Nome(self):
        return self.Nome

    def alt_Fome(self, Fome):
        self.Fome = Fome

    def get_Fome(self):
        return self.Fome

    def alt_Saude(self, Saude):
        self.Saude = Saude

    def get_Saude(self):
        return self.Saude
        
    def alt_Idade(self, Idade):
        self.Idade = Idade

    def get_Idade(self):
        return self.Idade

    def CheckHumor(self):
        if self.Fome > 7 or self.Saude <= 3:
            return 'está mal-humorado'
        else:
            return 'está de bom humor'
    #tambem é possivel inserir um valor de pontuação no nivel do humor como no enunciado

    def get_Humor(self):
        return self.get_Fome() * self.get_Saude()
            
    def DarComida(self, Quantidade):
        if (Quantidade >= 0) and (Quantidade <= 100):
            self.Fome -= self.Fome * (Quantidade / 100.0)

    def brincar(self, Quantidade):
        if (Quantidade >= 0) and (Quantidade <= 100):
            self.Saude += self.Saude * (Quantidade / 100.0)

    def str(self):
        print('\n--STATUS--')
        print('Nome:', self.get_Nome())
        print('Idade:', self.get_Idade())
        print('Fome:', self.get_Fome())
        print('Saude:', self.get_Saude())
        print('Humor:', self.get_Humor())
            

gato = Tamagushi('Tobias')
gato.alt_Nome('Jojo')
gato.alt_Fome(9)
gato.alt_Saude(5)
gato.alt_Idade(10)
gato.DarComida(50)
gato.brincar(8)

print('Nome:',gato.Nome)
print(gato.Fome,'de fome')
print(gato.Saude,'de saúde')
print(gato.Idade,'anos')
print('O bichinho',gato.CheckHumor())
gato.str()