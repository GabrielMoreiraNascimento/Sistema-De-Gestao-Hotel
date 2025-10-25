from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, idade,id_func, salario,bonus = 0.15):
        super().__init__(nome, idade,id_func, salario)
        self.bonus = bonus

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self,idade):
        self._idade = idade
    
    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self, salario):
        self._salario = salario


    def mostrar_informacoes(self):
        bonus = self.salario * self.bonus
        print(f"Salário: {self.salario}")
        print(f"Bônus: {bonus}")
        print(f"Salário total: {self.salario + bonus}")

    def gerar_relatorio(self, funcionarios):
        print("Relatório de Funcionários:")
        for funcionario in funcionarios:
            funcionario.mostrar_informacoes() 
            print("-" * 20)
