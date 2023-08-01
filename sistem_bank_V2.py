import textwrap


def menu():
    menu = """\n
    =================================================================
    ----------------Olá cliente, seja bem-vindo----------------------
    --------------Por favor, selecione a opção desejada--------------
    [D]\tDepósito
    [S]\tSaque
    [E]\tExtrato
    [NU]\tNovo usuário
    [NC]\tNova conta
    [LC]\tListar contas
    [Q]\tSair
    =================================================================
    ==> """
    return input(textwrap.dedent(menu))

def deposito(saldo, dinheiro, extrato, /):
    if dinheiro > 0:
        saldo += dinheiro
        extrato += f"Depósito no valor de:\tR$ {dinheiro:.2f}\n"
        print("Depósito realizado com sucesso!!")
    else:
        print("Operação não concluída!! Valor informado incorreto.")
    return saldo, extrato

def saque(*, saldo, dinheiro, extrato, limite, numero_saques, saques_diario):
    excedeu_saldo = dinheiro > saldo
    excedeu_limite = dinheiro > limite
    excedeu_saque = numero_saques >= saques_diario
        
    if excedeu_limite:
        print("Operação não concluída!! Valor informado maior que o limite de saque, por gentileza, escolha um valor menor!")       
        
    elif excedeu_saldo:
        print("Operação não concluída!! Valor informado maior que seu saldo bancário, por gentileza, escolha outro valor!")
        
    elif excedeu_saque:
        print("Operação não concluída!! Você excedeu a quantidade de saque diário, por gentileza, volte amanhã!")
        
    elif dinheiro > 0:
        saldo -= dinheiro
        extrato += f"Saque no valor de:\t\tR$ {dinheiro: .2f}\n"
        numero_saques += 1
    else:
        print("Operação não concluída!! Valor informado é inválido, por gentileza, escolha outro valor!")
        
    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============")
    print("Não foram realizadas movimentações nessa conta." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=========================================")

def novo_usuario(usuarios):
    cpf = input("Informe o CPF para cadastramento de usuário (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Já existe usuário com esse CPF!!")
        return
        
    nome = input("Por favor, digite seu nome completo: ")
    data_nascimento = input("Por favor, digite sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Por favor, digite seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("========== Usuário criado com sucesso!! ==========")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Por favor, digite o CPF do usuário já cadastrado no nosso banco")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n========== Conta criada com sucesso! ==========")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        
    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência =\t{conta['agencia']}
            Conta Corrente =\t{conta['numero_conta']}
            Titular =\t{conta['usuario']['nome']}
            """
    print("=" * 40)
    print(textwrap.dedent(linha))

def main():
    saques_diario = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = " "
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if (opcao.upper()) == "D":
            dinheiro = float(input("Por favor, digite o valor que deseja depositar em sua conta: "))
        
            saldo, extrato = deposito(saldo, dinheiro, extrato)
            
        elif (opcao.upper()) == "S":
            dinheiro = float(input("Por favor, digite o valor que deseja sacar: "))
            
            saldo, extrato = saque(
                saldo=saldo,
                dinheiro=dinheiro,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                saques_diario=saques_diario,
            )
        elif (opcao.upper()) == "E":
            print(extrato)
        elif opcao == "NU":
            novo_usuario(usuarios)
        elif (opcao.upper()) == "NC":
            numero_conta = len(contas) + 1
            conta = nova_conta (AGENCIA, numero_conta, usuarios)
            if conta:
                conta.append(conta)
        elif (opcao.upper()) == "LC":
            listar_contas(contas)
        elif (opcao.upper()) == "Q":
            print("""
----------------------------------------------------------------------------
------------------- Somos gratos por você ser nosso cliente ----------------
----------------------------------------------------------------------------
-------------------------- Tenha um excelente dia --------------------------
----------------------------------------------------------------------------

""")
            break
        else:
            print("Opção inválida!! Por favor selecione uma opção válida.")

main()