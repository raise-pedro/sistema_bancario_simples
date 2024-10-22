# Criação de um menu para melhor visualização das operações.
menu = """
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0         # Saldo inicial.
limite = 500      # Valor limite por saque.
extrato = ""      # Extrato inicial, representado por uma string vazia.
numero_saques = 0 # Contador de saques.
                  # LIMITE DE SAQUES = 3

# Criação de estrutura de repetição, para validação da escolha do usuário no menu.
while True:
    opcao = input(menu)
# Operação de depósito:
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: ")) # Recebe o valor digitado pelo usuário.
        if valor > 0:                                         # Só aceita valores positivos.
            saldo += valor                                    # Adiciona o valor no saldo.
            extrato += f"Depósito: R$ {valor:.2f}\n"          # Registra a movimentação no extrato.
        
        else:
            print("Operação falhou! O valor informado é inválido.") # Caso o valor recebido seja inválido, retorna ao menu.
# Operação de saque:
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: ")) # Recebe o valor digitado pelo usuário.

        if valor > saldo: # Condição que impede o usuário de realizar um saque maior que seu saldo.
            print("Operação falhou! Você não tem saldo suficiente.") 

        elif valor > limite: # Condição que impede o usuário de realizar um saque maior que o valor limite (500).
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= 3: # Condição que impede o usuário de realizar um saque, caso ele tenha atingido o limite de saques diários (3).
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:                           # Só aceita valores positivos.
            saldo -= valor                        # Subtrai o valor do saldo.
            extrato += f"Saque: R$ {valor:.2f}\n" # Registra a movimentação no extrato.
            numero_saques += 1                    # Incrementa +1 ao contador de saques, para a verificação do limite diário.

        else:
            print("Operação falhou! O valor informado é inválido.") # Caso o valor recebido seja inválido, retorna ao menu.
# Operação de extrato:
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if extrato == '':   # Condição para informar que não houve movimentação.
            print("Não foram realizadas movimentações.") 
        
        else: 
            print(extrato)                  # Exibe o extrato.
            print(f"Saldo: R$ {saldo:.2f}") # Exibe o saldo.
            print("==========================================")

    elif opcao == "q":  # Condição para o usuário interromper o programa.
        break 

    else: # Caso a opção selecionada no menu seja inválida, retorna ao menu.
        print("Operação inválida, por favor selecione novamente a operação desejada.") 
