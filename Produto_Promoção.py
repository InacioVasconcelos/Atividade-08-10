class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcularPrecoPromocional(self):
        return self.preco * 0.90


produto = Produto("Caderno", 100)

print("Produto:", produto.nome)
print("Preço promocional: R$", produto.calcularPrecoPromocional())