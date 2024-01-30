from datetime import datetime

class Movimentacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.data = datetime.now()

    def __str__(self):
        return f"{self.tipo} de R$ {self.valor:.2f} em {self.data.strftime('%d/%m/%Y %H:%M:%S')}"

class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0.0
        self.movimentacoes = []

    def realizar_saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            movimentacao = Movimentacao('Saque', valor)
            self.movimentacoes.append(movimentacao)
            return True
        else:
            print('ERRO: Valor de saque indisponível')
            return False

    def realizar_deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            movimentacao = Movimentacao('Depósito', valor)
            self.movimentacoes.append(movimentacao)
            return True
        else:
            print('ERRO: Valor de depósito inválido')
            return False

    def consultar_extrato(self):
        print(f'\nExtrato da conta {self.agencia}-{self.numero_conta} ({self.usuario.nome}):\n')
        if len(self.movimentacoes) == 0:
            print('Nenhuma movimentação realizada.')
        else:
            for movimentacao in self.movimentacoes:
                print(movimentacao)
            print(f'Saldo atual: R$ {self.saldo:.2f}')

    def __str__(self):
        return f"Agência: {self.agencia}\nNúmero da Conta: {self.numero_conta}\nSaldo: R$ {self.saldo:.2f}"

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

def acessar_conta():
    cpf = input("Digite o CPF do usuário para acessar a conta: ")
    usuario = next((u for u in usuarios if u.cpf == cpf), None)

    if usuario:
        conta_existente = input("Digite o número da conta existente no formato AGENCIA-NUMERO: ")
        conta = next((c for c in usuario.contas if f"{c.agencia}-{c.numero_conta}" == conta_existente), None)

        if conta:
            return conta
        else:
            print("Conta não encontrada.")
            return None
    else:
        print("Usuário não encontrado.")
        return None

def exibir_menu_inicial():
    return '''         Seja bem-vindo ao DNB!
[A] Acessar uma conta existente
[C] Criar uma nova conta
[L] Listar dados completos das contas por CPF
[T] Listar todas as contas (dados bancários detalhados)
[M] Adicionar conta associada a CPF existente
[Q] Sair

Selecione uma opção: '''

def listar_dados_completos_contas():
    cpf = input("Digite o CPF do usuário para listar todas as contas: ")

    # Procurar o usuário pelo CPF
    usuario = next((u for u in usuarios if u.cpf == cpf), None)

    if usuario:
        print(f"\nDados completos das contas do usuário {usuario.nome} ({usuario.cpf}):\n")
        for conta in usuario.contas:
            print(conta)
            print('-' * 30)
    else:
        print("\nUsuário não encontrado.\n")

def exibir_menu_operacoes():
    return '''         Operações da Conta
[S] Sacar
[D] Depositar
[E] Consultar Extrato
[V] Voltar para o Menu Inicial

Selecione uma operação: '''

def adicionar_conta_existente():
    cpf = input("Digite o CPF do usuário para associar a conta existente: ")

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
        print("\nConta associada com sucesso!\n")
    else:
        print("\nUsuário não encontrado. Por favor, crie um usuário primeiro.\n")


def listar_todas_contas():
    print("\nTodas as contas com dados bancários detalhados:\n")
    for usuario in usuarios:
        print(f"Usuário: {usuario.nome} ({usuario.cpf})")
        for conta in usuario.contas:
            print(f"\n{conta}")
            print('-' * 30)

def realizar_operacoes_conta(banco, conta):
    while True:
        print('-' * 41)
        print(f'{banco:^41}'.upper())
        print('-' * 41)
        opcao = str(input(exibir_menu_operacoes())).upper()
        print('-' * 41)

        if opcao == 'S':
            valor_saque = float(input('Digite o valor do saque: R$ '))
            if conta.realizar_saque(valor_saque):
                print('Saque realizado com sucesso!')

        elif opcao == 'D':
            valor_deposito = float(input('Digite o valor do depósito: R$ '))
            if conta.realizar_deposito(valor_deposito):
                print('Depósito realizado com sucesso!')

        elif opcao == 'E':
            conta.consultar_extrato()

        elif opcao == 'V':
            print('Retornando ao Menu Inicial...')
            break

        else:
            print('Operação inválida. Tente novamente.')
            print()

def main(banco):
    while True:
        print("-" * 41)
        print(f"{banco:^41}".upper())
        print("-" * 41)
        opcao_inicial = str(input(exibir_menu_inicial())).upper()
        print("-" * 41)

        if opcao_inicial == 'A':
            conta = acessar_conta()
            if conta:
                realizar_operacoes_conta(banco, conta)
        elif opcao_inicial == 'C':
            criar_usuario()
            criar_conta()
        elif opcao_inicial == 'L':
            listar_dados_completos_contas()

        elif opcao_inicial == 'T':
            listar_todas_contas()

        elif opcao_inicial == 'M':
            adicionar_conta_existente()

        elif opcao_inicial == 'Q':
            print("O DNB agradece a preferência!")
            print()
            break
        else:
            print("Opção inválida. Tente novamente.")
            print()

if __name__ == "__main__":
    banco = 'Diniz National Bank (DNB)'
    main(banco)
