class Livro:
    def __init__(self, titulo):
        self.titulo = titulo


class Emprestimo:
    def __init__(self, livro, aluno):
        self.livro = livro
        self.aluno = aluno

    def gerarResumo(self):
        return "Aluno: " + self.aluno + " | Livro: " + self.livro.titulo


livro = Livro("Introdução à programação")
emprestimo = Emprestimo(livro, "João")

print(emprestimo.gerarResumo())