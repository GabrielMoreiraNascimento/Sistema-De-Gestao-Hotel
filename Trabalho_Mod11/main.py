from Hospede import Hospede
from QuartoSimples import QuartoSimples, lista_quartos_simples
from QuartoLuxo import QuartoLuxo, lista_quartos_luxo
from Funcionario import Funcionario
from Recepcionista import Recepcionista
from TecnManutencao import TecnicoManutencao
from TecnRecepcao import TecnicoRecepcao
from Gerente import Gerente

op  = input("HOTEL TRIVAGO\nVocê è um funcionario ou um hospede?\n1-Hospede\n2-Funciónario\n>")

if op == "1":
    print("Faça o Check-in!")
    nome = input("Qual seu nome? ")
    idade = int(input("Qual sua idade? "))
    estadia = int(input("Quantos dias deseja ficar? "))

    nome = Hospede(nome,idade,estadia)
    op2 = input("Deseja ficar num quarto simples ou de luxo?\n1-Simples\n2-Luxo\n>")
    if op2 == "1":
        print("Escolha um quarto")
        for quarto in lista_quartos_simples:
            print(quarto.mostrar_informacoes())
            print("-" * 30)
        quarto_escolhido = int(input("Digite o numero do quarto que deseja: "))
        for q in lista_quartos_simples:
            if q.numero == quarto_escolhido:
                quarto_escolhido = q
                break
        if quarto_escolhido:
            nome.atribuir_quarto(quarto_escolhido)
            nome.mostrar_informacao()
            print(f"Total a pagar: {nome.calcular_conta()}")
        else:
            print("Quarto nao encontrado!")
            
    if op2 == "2":
        print("Escolha um quarto")
        for quarto in lista_quartos_luxo:
            print(quarto.mostrar_informacoes())
            print("-" * 30)
        quarto_escolhido = int(input("Digite o numero do quarto que deseja: "))
        for q in lista_quartos_luxo:
            if q.numero == quarto_escolhido:
                quarto_escolhido = q
                break
        if quarto_escolhido:
            nome.atribuir_quarto(quarto_escolhido)
            nome.mostrar_informacao()
            print(f"Total a pagar: {nome.calcular_conta()}")
        else:
            print("Quarto nao encontrado!")

if op == "2":
    


        

