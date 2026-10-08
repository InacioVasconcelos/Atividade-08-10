class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def consultarSaldo(self):
        return self.__saldo

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False


conta = Conta(100)

print("Saque de R$ 30:", conta.sacar(30))
print("Saldo:", conta.consultarSaldo())

print("Saque de R$ 80:", conta.sacar(80))
print("Saldo:", conta.consultarSaldo())

print("Saque de R$ 0:", conta.sacar(0))
print("Saldo:", conta.consultarSaldo())
