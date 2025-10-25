from Hospede import Hospede
from Recepcionista import Recepcionista
from Gerente import Gerente
from TecnRecepcao import TecnicoRecepcao
from QuartoSimples import lista_quartos_simples
from QuartoLuxo import lista_quartos_luxo

def mostrar_quartos():
    print("\n--- QUARTOS SIMPLES ---")
    for q in lista_quartos_simples:
        q.mostrar_informacoes()
        print("-" * 30)

    print("\n--- QUARTOS LUXO ---")
    for q in lista_quartos_luxo:
        q.mostrar_informacoes()
        print("-" * 30)


def escolher_quarto():
    tipo = input("Tipo de quarto (simples/luxo): ").strip().lower()
    if tipo == "simples":
        quartos = lista_quartos_simples
    elif tipo == "luxo":
        quartos = lista_quartos_luxo
    else:
        print("Tipo inválido!")
        return None

    disponiveis = []
    for q in quartos:
        if not q.ocupado:
            disponiveis.append(q)

    if len(disponiveis) == 0:
        print("❌ Nenhum quarto disponível.")
        return None

    print("Quartos disponíveis:")
    for q in disponiveis:
        print(f"- {q.numero}")

    try:
        numero = int(input("Escolha o número do quarto: "))
    except ValueError:
        print("Número inválido.")
        return None

    for q in disponiveis:
        if q.numero == numero:
            return q

    print("Número não encontrado.")
    return None


def encontrar_hospede(lista, nome):
    for h in lista:
        if h.nome.lower() == nome.lower():
            return h
    return None


def main():
    recepcionista = Recepcionista("Maria", 1, 30, 1200, "Diurno")
    gerente = Gerente("João", 45, 2, 3000)
    tecnico_recepcao = TecnicoRecepcao("Carlos", 28, 3, 1500, "Noturno", "Elétrica")

    funcionarios = [recepcionista, gerente, tecnico_recepcao]

    while True:
        print("\n===== HOTEL TRIVAGO =====")
        print("1 - Registrar hóspede")
        print("2 - Atribuir quarto")
        print("3 - Ver lista de hóspedes")
        print("4 - Mostrar quartos")
        print("5 - Calcular conta")
        print("6 - Fazer checkout")
        print("7 - Mostrar funcionários")
        print("8 - Gerar relatório (Gerente)")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome do hóspede: ")
            idade = int(input("Idade: "))
            dias = int(input("Dias de estadia: "))
            h = Hospede(nome, idade, dias)
            recepcionista.registrar_hospede(h)

        elif opcao == "2":
            if len(recepcionista.lista_hospede) == 0:
                print("Nenhum hóspede registrado.")
            else:
                nome = input("Nome do hóspede: ")
                h = encontrar_hospede(recepcionista.lista_hospede, nome)
                if h is None:
                    print("Hóspede não encontrado.")
                else:
                    quarto = escolher_quarto()
                    if quarto:
                        h.atribuir_quarto(quarto)

        elif opcao == "3":
            recepcionista.ver_lista_hospede()

        elif opcao == "4":
            mostrar_quartos()

        elif opcao == "5":
            nome = input("Nome do hóspede: ")
            h = encontrar_hospede(recepcionista.lista_hospede, nome)
            if h is not None:
                total = h.calcular_conta()
                if total:
                    print(f"💰 Total a pagar: €{total:.2f}")
            else:
                print("Hóspede não encontrado.")

        elif opcao == "6":
            nome = input("Nome do hóspede: ")
            h = encontrar_hospede(recepcionista.lista_hospede, nome)
            if h is not None:
                h.checkout()
            else:
                print("Hóspede não encontrado.")

        elif opcao == "7":
            print("\n--- FUNCIONÁRIOS ---")
            for f in funcionarios:
                print("-" * 30)
                if hasattr(f, "mostrar_info"):
                    f.mostrar_info()
                else:
                    f.mostrar_informacoes()

        elif opcao == "8":
            gerente.gerar_relatorio(funcionarios)

        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

main()
