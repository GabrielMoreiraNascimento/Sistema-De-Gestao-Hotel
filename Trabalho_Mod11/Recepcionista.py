from Funcionario import Funcionario
from Quarto import Quarto

class Recepcionista(Funcionario):
   def __init__(self, nome, idade, id_func, salario, turno):
      Funcionario.__init__(self, nome, idade, id_func, salario)
      self._turno=turno
      self.lista_hospede = []
     
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

   @property
   def turno(self):
      return self._turno
     
   @turno.setter
   def turno(self, valor):
      self._turno = valor

   def mostrar_informacoes(self):
      print(self.nome)
      print(self.idade)
      print(self._id_func)
      print(self.salario)
      print(self.turno)

   def registrar_hospede(self, hospede):
      if hospede in self.lista_hospede:
         print("O hospede ja esta registrado.")
      else:   
         self.lista_hospede.append(hospede)
         print("O Hospede foi registrado!")

   def ver_lista_hospede(self):
      if not self.lista_hospede:
         print("Nenhum Hospede registrado.")
         return
      
      print("LISTA DE HOSPEDES")
      for hospede in self.lista_hospede:
         print("-" * 30)
         print(f"Nome: {hospede.nome}\nDias de estadia: {hospede.estadia}\nQuarto: {hospede.quarto.numero}")
    