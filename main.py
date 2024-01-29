banco = 'Diniz National Bank (DNB)'
menu = '''         Seja bem-vindo ao DNB!
[S] Sacar
[D] Depositar
[E] Consultar extrato
[Q] Sair

Selecione uma operação: '''


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
        opcao = str(input(menu)).upper()
        print('-' * 41)

        if opcao == 'S':
            saldo, qtd_limite_saque, historico_saques = realizar_saque(saldo, qtd_limite_saque, VALOR_LIMITE_SAQUE,
                                                                       historico_saques)

        elif opcao == 'D':
            saldo, historico_depositos = realizar_deposito(saldo, historico_depositos)

        elif opcao == 'E':
            consultar_extrato(banco, saldo, historico_saldos, historico_depositos, historico_saques, qtd_limite_saque)

        elif opcao == 'Q':
            print('      O GNB agradece a preferência!')
            print()
            break

        else:
            print('   Operação inválida. Tente novamente')
            print()


if __name__ == "__main__":
    main()
