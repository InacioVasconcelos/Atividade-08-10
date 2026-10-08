class SenhaAtendimento:
    contador = 0

    def __init__(self):
        SenhaAtendimento.contador += 1
        self.__numero = SenhaAtendimento.contador

    def consultarNumero(self):
        return self.__numero


senha1 = SenhaAtendimento()
senha2 = SenhaAtendimento()
senha3 = SenhaAtendimento()

print("Senha 1:", senha1.consultarNumero())
print("Senha 2:", senha2.consultarNumero())
print("Senha 3:", senha3.consultarNumero())
print("Senha 1 novamente:", senha1.consultarNumero())