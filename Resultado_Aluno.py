class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcularMedia(self):
        return (self.nota1 + self.nota2) / 2

    def estaAprovado(self):
        return self.calcularMedia() >= 7


aluno1 = Aluno("João", 8, 6)
aluno2 = Aluno("Maria", 5, 7)

print(aluno1.nome, "- Média:", aluno1.calcularMedia(), "- Aprovado:", aluno1.estaAprovado())
print(aluno2.nome, "- Média:", aluno2.calcularMedia(), "- Aprovado:", aluno2.estaAprovado())