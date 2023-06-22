class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

fun1 = Funcionario('Joao', 1000)
print ('Nome: %s') % fun1.getNome()
print ('Salario: %.2f') % fun1.getSalario()