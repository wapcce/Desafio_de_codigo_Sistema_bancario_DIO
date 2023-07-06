menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor_deposito = 0.00
valor_saque = 0.00

while True:
    opcao = input(menu)
    #print(opcao.lower())

    if opcao.lower() == "d":
        print("Depósito")
        valor_deposito = float(input("informe o valor do depósito: "))
        if valor_deposito <=0:
            print("Valor do depósito inválido")
            continue
        else:
            saldo += valor_deposito
            extrato += "Depósito: R$ {:.2f}\n".format(valor_deposito)

    elif opcao.lower() == "s":
        print("Saque")
        valor_saque = float(input("informe o valor do saque: "))
        if (saldo - valor_saque) <=0:
            print("Saldo indisponível para saque")
            continue

        elif valor_saque <=0:
            print("valor de saque inválido")
            continue
            
        elif valor_saque > 500:
            print("Limite de saque excedido")
            continue
            
        elif LIMITE_SAQUES == 0:
            print("Limite máximo de saques")
            continue
            
        else:
            saldo -= valor_saque
            
            extrato += "Saque: R$ {:.2f}\n".format(valor_saque)
            LIMITE_SAQUES -= 1
        

    elif opcao.lower() == "e":
        print(" Extrato ".center(26,"#"))
        print("Não houve movimentações\n" if not extrato else extrato)
        print("Saldo: R$: {:.2f}".format(saldo))
        print("".center(26,"#"))

    elif opcao.lower() == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
