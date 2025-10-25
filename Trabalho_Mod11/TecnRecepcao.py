from Recepcionista import Recepcionista
from TecnManutencao import TecnicoManutencao

class TecnicoRecepcao(Recepcionista, TecnicoManutencao):
    def __init__(self, nome, idade, id_func, salario, turno, especialidade):
        Recepcionista.__init__(self, nome, id_func, idade, salario, turno)
        TecnicoManutencao.__init__(self, nome, idade, id_func, salario, especialidade)

    def registrar_hospede(self, hospede):
        Recepcionista.registrar_hospede(self, hospede)

    def registrar_reparo(self, descricao):
        TecnicoManutencao.registrar_reparo(self, descricao)

    def mostrar_info(self):
        print("\n--- Técnico de Recepção ---")
        print(f"Nome: {self.nome}")
        print(f"ID: {self._id_func}")
        print(f"Idade: {self.idade}")
        print(f"Salário: {self.salario}€")
        print(f"Turno: {self.turno}")
        print(f"Especialidade: {self.especialidade}")
