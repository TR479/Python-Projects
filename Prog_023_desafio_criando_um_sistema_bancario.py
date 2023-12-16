menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        
        print("Depositar\n")
        deposito = int(input("Quanto vai depositar? "))
        if deposito <= 0 :
            print("Operação invalida. Valor de deposito invalido!")
           
        else :
            saldo += deposito
            print(f"Deposito no valor de R$ {deposito:.2f} feito com sucesso!")
            extrato += f"Deposito no valor de R$ {deposito:.2f} feito com sucesso!\n"

    elif opcao == "s":
         print("Saque\n")
         saque = int(input("Quanto vai sacar? "))

         if numero_saques >= LIMITE_SAQUES:
             print("Operação invalida. Limite de saques diários alcançados")

         elif (saque <= limite):
              print ("Operação invalida. Valor de saque supera o limite de saque!")

         elif (0 < saque <= saldo):
             saldo -= saque
             print(f"Saque no valor de R$ {saque:.2f} feito com sucesso!")
             extrato += f"Saque no valor de R$ {saque:.2f} feito com sucesso!\n"
             numero_saques += 1
    
         else :
            print ("Operação invalida. Valor de saque invalido!")

    elif opcao == "e":
        print("Extrato\n")
        print("Nenhuma movimentção realizada.\n" if not extrato else extrato)
        print(f"Numero de saques realizados: {numero_saques}\n")
        print(f"Saldo = R$ {saldo:.2f}")
      
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")