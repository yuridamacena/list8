class Tamagushi:
    def __init__(self, Nome, Fome = 10, Saude = 0, Idade = 1):
        self.Nome = Nome
        self.Fome = Fome
        self.Saude = Saude
        self.Idade = Idade

    def alt_Nome(self, Nome):
        self.Nome = Nome

    def alt_Fome(self, Fome):
        self.Fome = Fome

    def alt_Saude(self, Saude):
        self.Saude = Saude
        
    def alt_Idade(self, Idade):
        self.Idade = Idade

    def CheckHumor(self):
        if self.Fome > 7 or self.Saude <= 3:
            return 'está mal-humorado'
        else:
            return 'está de bom humor'
    #tambem é possivel inserir um valor de pontuação no nivel do humor como no enunciado
            
    def DarComida(self):
        if self.Fome <= 10 and self.Fome > 0:
            self.Fome -= 1
            

gato = Tamagushi('Tobias')
gato.alt_Nome('Jojo')
gato.alt_Fome(9)
gato.alt_Saude(5)
gato.alt_Idade(10)
gato.DarComida()
gato.DarComida()
gato.DarComida()

print('Nome:',gato.Nome)
print(gato.Fome,'de fome')
print(gato.Saude,'de saúde')
print(gato.Idade,'anos')
print('O bichinho',gato.CheckHumor())