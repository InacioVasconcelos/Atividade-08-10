class Ingresso:
    def __init__(self, preco):
        self.preco = preco

    def calcularValor(self):
        return self.preco


class MeiaEntrada(Ingresso):
    def __init__(self, preco):
        super().__init__(preco)

    def calcularValor(self):
        return self.preco / 2


ingresso = Ingresso(20)
meia = MeiaEntrada(20)

print("Ingresso comum: R$", ingresso.calcularValor())
print("Meia entrada: R$", meia.calcularValor())