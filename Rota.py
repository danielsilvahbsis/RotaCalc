class Rota:
    def __init__(self, unb, vendedor, cliente, origem):
        self.unb = unb
        self.vendedor = vendedor
        self.cliente = cliente
        self.origem = origem

    def __str__(self):
        return str(self.unb) + str(self.vendedor) + str(self.cliente) + str(self.origem)
