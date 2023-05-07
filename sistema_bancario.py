    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


==> """
saldo = 0 
valor = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print ("Operação falhou. O valor informado é invalido. ")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print ("Operação falhou. Saldo insuficiente para retirada.")
        elif excedeu_saques:
            print ("Operação falhou. Limite saques diários alcançado.")
        elif valor > 0:
            numero_saques += 1
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print ("Operação falhou. O valor informado é invalido. ")
    
    elif opcao == "e":
        print ("**************** EXTRATO ********************")
        print ("Não foram realizadas movimentações " if not extrato else extrato)
        extrato += f"Extrato: R$ {valor:.2f}\n"
        print (f"\nSaldo: R$ {saldo:.2f} ")
        print ("*********************************************")   

    elif opcao == "q":
        break

    else:
        print ("Operação inválida. Favor selecionar novamente a operação desejada")

