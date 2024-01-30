from datetime import datetime

banco = 'Diniz National Bank (DNB)'

def realizar_saque(saldo, qtd_limite_saque, VALOR_LIMITE_SAQUE, historico_saques):
    valor_saque = int(input('Valor do saque: R$ '))

    if qtd_limite_saque > 0 and valor_saque <= VALOR_LIMITE_SAQUE and valor_saque <= saldo:
        qtd_limite_saque -= 1
        saldo -= valor_saque
        print('                SUCESSO!')
        print(f'       Saque de R$ {valor_saque:.2f} realizado')

        historico_saques.append(valor_saque)
    else:
        print('                  ERRO!')
        if qtd_limite_saque == 0:
            print('        Limite de saques atingido')
        elif valor_saque > VALOR_LIMITE_SAQUE:
            print('       Valor de saque indisponível')
        else:
            print('      Valor indisponível para saque')

    print('\nRetornando ao menu...')
    return saldo, qtd_limite_saque, historico_saques

def realizar_deposito(saldo, historico_depositos):
    valor_deposito = int(input('Valor do depósito: R$ '))

    if valor_deposito > 0:
        saldo += valor_deposito
        print('\n                SUCESSO!')
        print(f'      Depósito de R$ {valor_deposito:.2f} realizado')
        historico_depositos.append(valor_deposito)
    else:
        print('\nValor de depósito inválido')

    print('\nRetornando ao menu...')
    return saldo, historico_depositos

def consultar_extrato(banco, saldo, historico_saldos, historico_depositos, historico_saques, qtd_limite_saque):
    print(f'\n{banco:^41}'.upper())
    print('-' * 41)
    print('\n            Extrato da conta\n')

    if len(historico_depositos) == 0 and len(historico_saques) == 0:
        print('       Nenhuma operação realizada')
        print('-' * 41)
    else:
        print(f'Saldo inicial: R$ {historico_saldos[0]:.2f}\n')

    if len(historico_depositos) > 0:
        print('depósitos'.upper())
        for deposito in historico_depositos:
            print(f'R$ {deposito:.2f}')
        print('-' * 41)

    if len(historico_saques) > 0:
        print('saques'.upper())
        for saque in historico_saques:
            print(f'R$ {saque:.2f}')
        print('-' * 41)

    print(f'Saldo atual da conta: R$ {saldo:.2f}')
    print(f'Saques diários restantes: {qtd_limite_saque}\n')

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, agencia, numero_conta):
        conta = Conta(agencia, numero_conta, self)
        self.contas.append(conta)

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nData de Nascimento: {self.data_nascimento}\nEndereço: {self.endereco}"

class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0.0

    def __str__(self):
        return f"Agência: {self.agencia}\nNúmero da Conta: {self.numero_conta}\nSaldo: R$ {self.saldo:.2f}\n{str(self.usuario)}"

usuarios = []

def criar_usuario():
    nome = input("Nome: ")
    cpf = input("CPF: ")

    # Verificar se o CPF já está cadastrado
    while any(usuario.cpf == cpf for usuario in usuarios):
        print("CPF já cadastrado. Tente novamente.")
        cpf = input("CPF: ")

    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
    endereco = input("Endereço: ")

    # Converter a string da data de nascimento para um objeto datetime
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

    usuario = Usuario(nome, cpf, data_nascimento, endereco)
    usuarios.append(usuario)

    print("\nUsuário criado com sucesso!\n")

def criar_conta():
    cpf = input("Digite o CPF do usuário para associar a conta: ")

    # Procurar o usuário pelo CPF
    usuario = next((u for u in usuarios if u.cpf == cpf), None)

    if usuario:
        agencia = input("Agência: ")
        numero_conta = input("Número da Conta: ")

        # Verificar se o número da conta já está em uso
        while any(conta.numero_conta == numero_conta for conta in usuario.contas):
            print("Número da conta já em uso. Tente novamente.")
            numero_conta = input("Número da Conta: ")

        usuario.adicionar_conta(agencia, numero_conta)
        print("\nConta criada com sucesso!\n")
    else:
        print("\nUsuário não encontrado. Por favor, crie um usuário primeiro.\n")

def listar_contas():
    cpf = input("Digite o CPF do usuário para listar suas contas: ")

    # Procurar o usuário pelo CPF
    usuario = next((u for u in usuarios if u.cpf == cpf), None)

    if usuario:
        print(f"\nContas do usuário {usuario.nome} ({usuario.cpf}):\n")
        for conta in usuario.contas:
            print(conta)
            print('-' * 30)
    else:
        print("\nUsuário não encontrado.\n")

def exibir_menu():
    return '''         Seja bem-vindo ao DNB!
[S] Sacar
[D] Depositar
[E] Consultar extrato
[C] Criar Usuário
[CC] Criar Conta
[LC] Listar Contas
[Q] Sair

Selecione uma operação: '''

def main():
    opcao = 'Início'
    qtd_limite_saque = 3
    VALOR_LIMITE_SAQUE = 500.0
    saldo = 1500.0
    valor_saque = valor_deposito = 0
    historico_depositos = []
    historico_saques = []
    historico_saldos = [saldo]

    while True:
        print('-' * 41)
        print(f'{banco:^41}'.upper())
        print('-' * 41)
        opcao = str(input(exibir_menu())).upper()
        print('-' * 41)

        if opcao == 'S':
            saldo, qtd_limite_saque, historico_saques = realizar_saque(saldo, qtd_limite_saque, VALOR_LIMITE_SAQUE,
                                                                       historico_saques)

        elif opcao == 'D':
            saldo, historico_depositos = realizar_deposito(saldo, historico_depositos)

        elif opcao == 'E':
            consultar_extrato(banco, saldo, historico_saldos, historico_depositos, historico_saques, qtd_limite_saque)

        elif opcao == 'C':
            criar_usuario()

        elif opcao == 'CC':
            criar_conta()

        elif opcao == 'LC':
            listar_contas()

        elif opcao == 'Q':
            print('      O GNB agradece a preferência!')
            print()
            break

        else:
            print('   Operação inválida. Tente novamente')
            print()

if __name__ == "__main__":
    main()
