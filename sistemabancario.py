menu = """

Olá, digite a opção desejada:

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido! Operação não permitida.")

    elif opcao == "1":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo Insuficiente! ")

        elif excedeu_limite:
            print("Saldo Insuficiente! ")

        elif excedeu_saques:
            print("Número máximo de saques excedido. Procure a agência.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor inválido! Operação não permitida.")

    elif opcao == "2":
        print("\n================ EXTRATO ================")
        print("Você ainda não fez movimentações." if not extrato else extrato)
        print(f"\nSaldo final: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "3":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")