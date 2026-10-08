class Lampada:
    def __init__(self):
        self.__ligada = False

    def ligar(self):
        self.__ligada = True

    def desligar(self):
        self.__ligada = False

    def consultarConsumo(self):
        if self.__ligada:
            return 10
        return 0


lampada1 = Lampada()
lampada2 = Lampada()

lampada1.ligar()

print("Consumo da lâmpada 1:", lampada1.consultarConsumo(), "W")
print("Consumo da lâmpada 2:", lampada2.consultarConsumo(), "W")

lampada1.desligar()

print("Depois de desligar:")
print("Consumo da lâmpada 1:", lampada1.consultarConsumo(), "W")
print("Consumo da lâmpada 2:", lampada2.consultarConsumo(), "W")