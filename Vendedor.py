class Vendedor:

    def __init__(self, unb, codigo, nome, supervisor, cargo, usuario):
        self.unb = unb
        self.codigo = codigo
        self.nome = nome
        self.supervisor = supervisor
        self.cargo = cargo
        self.usuario = usuario

    @staticmethod
    def create_table(conn):
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE vendor (
            unb INTEGER NOT NULL,
            codigo INTEGER NOT NULL,
            nome TEXT
            supervisor INTEGER,
            cargo INTEGER,
            usuario TEXT,
            PRIMARY KEY (unb, codigo) 
        );
        """)
