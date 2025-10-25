from Quarto import Quarto

class QuartoLuxo(Quarto):
    def __init__(self, numero, tipo="Simples", preco_diaria=80, ocupado = False, minibar = True, jacuzzi = True):
        super().__init__(numero,tipo,preco_diaria)
        self._ocupado = ocupado
        self.minibar = minibar
        self.jacuzzi = jacuzzi
        self.lista_quartos = [201,202,203,204,205]

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
        print("Extras incluídos:")
        print(f"  • Minibar: {'✅' if self.minibar else '❌'}")
        print(f"  • Jacuzzi: {'✅' if self.jacuzzi else '❌'}")

ql1 = QuartoLuxo(201)
ql2 = QuartoLuxo(202)
ql3 = QuartoLuxo(203)
ql4 = QuartoLuxo(204)
ql5 = QuartoLuxo(205)

lista_quartos_luxo = [ql1,ql2,ql3,ql4,ql5]