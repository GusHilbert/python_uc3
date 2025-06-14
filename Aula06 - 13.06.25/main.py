from Conta import ContaCorrente

contas = {
    '123':ContaCorrente('Gustav Hilbert','123','teste123',1234.23),
    '456':ContaCorrente('Monique Cordebello','456','teste123',23411321.22),
    '789':ContaCorrente('Luis Gladulich','789','teste123',10000000000.11)
}

etapa01 = str(input("Informe o nome da conta que você quer verificar: "))

ContaCorrente.ler_saldo(contas[etapa01])
print("1 - Fazer um saque \n2 - Fazer uma transferencia \nEscolha uma opção acima? ")