from Pessoas import Pessoa
from Recepcionista import Recepcionista

class Hospede(Pessoa):
    def __init__(self, nome, idade, estadia, quarto=None,):
        super().__init__(nome, idade)
        self.estadia = estadia
        self._quarto = quarto
    
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

    #Quarto    
    @property
    def quarto(self):
        return self._quarto
    
    @quarto.setter
    def quarto(self, quarto):
        if self._quarto==None:
            self._quarto = quarto
        else:
            print("O hóspede ja tem um quarto atribuido")

    def atribuir_quarto(self, quarto):
        if quarto is None:
            print("Quarto Inválido")
            return
        
        elif self._quarto is not None:
            print(f"O hospede já tem um quarto atribuido")
            return
        
        elif quarto.ocupado:
            print("O quarto está ocupado.")
            return

        self._quarto = quarto
        quarto.ocupado = True
        print("Quarto Atribuido!")
    
    def calcular_conta(self):
        if self.quarto == None:
            print("Nao é um hospede.")
            return
        
        total = self.estadia * self.quarto.preco_diaria
        return total
    
    def checkout(self):
        if self._quarto is not None:
            print(f"Checkout realizado. Quarto {self._quarto.numero} liberado.")
            self._quarto.ocupado = False
            self._quarto = None
        else:
            print("O hóspede não possui quarto atribuído.")

    
        
    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Dias de estadia: {self.estadia}")
        print(f"Quarto: {self.quarto.numero}")

    


    