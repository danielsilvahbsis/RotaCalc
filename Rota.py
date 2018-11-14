class Rota:
    def __init__(self, unb, vendedor, cliente, origem):
        self.unb = unb
        self.vendedor = vendedor
        self.cliente = cliente
        self.origem = origem

    def __str__(self):
        return 'Unb: ' + str(self.unb) + ' Vendedor: ' + str(self.vendedor) + " Cliente: " + str(self.cliente) + " Origem: " + str(self.origem)
