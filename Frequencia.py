class Frequencia:

    def __init__(self, unb, cliente, vendedor, perfil_vendas, periodicidade, data_inicial, frequencia_visita):
        self.unb = unb
        self.cliente = cliente
        self.vendedor = vendedor
        self.perfil_vendas = perfil_vendas
        self.periodicidade = periodicidade
        self.data_inicial = data_inicial
        self.frequencia_visita = frequencia_visita

    @staticmethod
    def create_table(conn):
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE frequency (
            unb INTEGER NOT NULL,
            cliente INTEGER NOT NULL,
            vendedor INTEGER NOT NULL
            perfil_vendas INTEGER 
            periodicidade INTEGER
            data_inicial TEXT
            frequencia_visita BLOB,
            PRIMARY KEY (unb, cliente, vendedor)
        );
        """)
