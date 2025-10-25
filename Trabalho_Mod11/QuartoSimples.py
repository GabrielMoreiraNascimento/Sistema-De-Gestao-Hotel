from Quarto import Quarto

class QuartoSimples(Quarto):
    def __init__(self, numero, tipo="Simples", preco_diaria=40, ocupado = False):
        super().__init__(numero,tipo,preco_diaria)
        self._ocupado = ocupado
        self.lista_quartos = [101,102,103,104,105]

    @property
    def ocupado(self):
        return self._ocupado
    
    @ocupado.setter
    def ocupado(self, valor):
        if valor == True or valor == False:
            self._ocupado = valor
            return

        else:
            print("O estado ocupado deve ser true ou false")
            return

    @property
    def preco_diaria(self):
        return self._preco_diaria
 
    @preco_diaria.setter
    def preco_diaria(self, valor):
        if valor > 0:
            self._quarto = valor
            return
        else:
            print("O preço nao pode ser negativo")
            return

    def mostrar_informacoes(self):
        estado = "🟥 Ocupado" if self.ocupado else "🟩 Disponível"
        print(f"Numero do Quarto: {self.numero}")
        print(f"Tipo do Quarto: {self.tipo}")
        print(f"Preço da Diária: {self.preco_diaria}€")
        print(f"Estado: {estado}")

q1 = QuartoSimples(101)
q2 = QuartoSimples(102)
q3 = QuartoSimples(103)
q4 = QuartoSimples(104)
q5 = QuartoSimples(105)

lista_quartos_simples = [q1,q2,q3,q4,q5]