def saudacao(nome):
    return f"Ola, {nome}! Bem-vindo ao MeuCash!"


def calcular_saldo(entradas, saidas):
    return sum(entradas) - sum(saidas)


def main():
    print("=== MeuCash - Controle Financeiro ===")
    nome = input("Digite seu nome: ")
    print(saudacao(nome))

    entradas = [1500.00, 200.00, 50.00]
    saidas = [800.00, 150.00, 75.00]

    saldo = calcular_saldo(entradas, saidas)
    print(f"Saldo atual: R$ {saldo:.2f}")

    if saldo > 0:
        print("Voce esta no positivo!")
    elif saldo == 0:
        print("Saldo zerado. Cuidado!")
    else:
        print("Atencao! Voce esta no negativo.")


if __name__ == "__main__":
    main()
