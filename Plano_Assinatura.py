from abc import ABC, abstractmethod


class Plano(ABC):
    @abstractmethod
    def calcularMensalidade(self):
        pass


class PlanoGratuito(Plano):
    def calcularMensalidade(self):
        return 0


class PlanoPremium(Plano):
    def calcularMensalidade(self):
        return 30


gratuito = PlanoGratuito()
premium = PlanoPremium()

print("Plano gratuito: R$", gratuito.calcularMensalidade())
print("Plano premium: R$", premium.calcularMensalidade())