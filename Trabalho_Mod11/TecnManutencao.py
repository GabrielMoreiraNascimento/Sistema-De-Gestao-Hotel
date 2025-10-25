from Funcionario import Funcionario

class TecnicoManutencao(Funcionario):
    def __init__(self, nome, idade, id_func, salario, especialidade):
        super().__init__(nome, idade, id_func, salario)
        self._especialidade = especialidade
        self.reparos = []

    @property
    def especialidade(self):
        return self._especialidade

    def registrar_reparo(self, descricao):
        self.reparos.append(descricao)
        print(f"🛠️ Reparo registrado: {descricao}")

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"ID: {self.id_func}")
        print(f"Salário: {self.salario}€")
        print(f"Especialidade: {self.especialidade}")
        if self.reparos:
            print("Reparos registrados:")
            for r in self.reparos:
                print(f"  - {r}")