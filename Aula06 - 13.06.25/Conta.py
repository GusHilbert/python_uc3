class ContaCorrente:
    def __init__(self,nome_cliente,num_conta,senha,saldo=0.0):
        self.nome_cliente = nome_cliente
        self.num_conta = num_conta
        # self.agencia = agencia
        self.senha = senha
        # self.cartao_credito = cartao_credito
        # self.financiamento = financiamento
        self.saldo = saldo
        # self.cheque_especial = cheque_especial

    def ler_saldo(self):
        print(f"O saldo de {self.nome_cliente} disponível é R$ {self.saldo}")


    def saque(self,valor):
        if self.saldo<valor:
            print("Você não tem saldo para o saque!")
        else:
            self.saldo -= valor
            print(f"Seu saque de R$ {valor:.2f} foi realizado! \nSeu novo saldo é de R$ {self.saldo:.2f}")

    def deposito(self,valor):
            if valor<0:
                print("Você não pode depositar valores negativos!")
            else:
                self.saldo += valor
                print(f"Seu deposito de R$ {valor:.2f} foi realizado! \nSeu novo saldo é de R$ {self.saldo:.2f}")

    def transferencia(self,valor, destinatario):
        if destinatario.num_conta != self.num_conta:
            ContaCorrente.sacar(self,valor)
            ContaCorrente.deposito(destinatario,valor)
        else:
            print(f"Não é possível realizar transferências com a mesma conta corrente ({self.num_conta})")

