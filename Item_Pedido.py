class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcularSubtotal(self):
        return self.produto.preco * self.quantidade

    def consultarNomeProduto(self):
        return self.produto.nome


produto = Produto("Livro", 40)
item = ItemPedido(produto, 10)

print("Produto:", item.consultarNomeProduto())
print("Subtotal: R$", item.calcularSubtotal())