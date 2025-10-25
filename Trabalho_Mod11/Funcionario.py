from Pessoas import Pessoa

class Funcionario(Pessoa):
    def __init__(self,nome,idade,id_func,salario):
        super().__init__(nome,idade)
        self._id_func = id_func
        self._salario = salario
    
    #Nome
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor
        
    #Idade
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        self._idade = valor
    
    #ID
    @property
    def id(self):
         return self._id_func
    
    @id.setter
    def id(self, valor):
        self._id_func = valor

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        if valor <= 0:
            print("Salario nao pode ser negativo")
        else:
            self._salario = valor

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, ID: {self._id_func}, Salario: {self._salario}")