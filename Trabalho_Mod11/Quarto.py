from abc import ABC, abstractmethod

class Quarto(ABC):
    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero
        self.tipo = tipo
        self._preco_diaria = preco_diaria

    @property
    @abstractmethod
    def ocupado(self):
        pass

    @property
    @abstractmethod
    def preco_diaria(self):
        pass
 
    @preco_diaria.setter
    def preco_diaria(self, valor):
        pass

    def mostrar_informacoes(self):
        pass