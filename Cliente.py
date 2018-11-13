class Cliente:

    def __init__(self, unb, codigo, razao_social, nome_fantasia, status, data_exclusao, motivo_bloqueio, exportado_siv,
                 origem, melhor_horario):
        self.unb = unb
        self.codigo = codigo
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.status = status
        self.data_exclusao = data_exclusao
        self.motivo_bloqueio = motivo_bloqueio
        self.exportado_siv = exportado_siv
        self.origem = origem
        self.melhor_horario = melhor_horario

    @staticmethod
    def create_table(conn):
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE client (
            unb INTEGER NOT NULL,
            codigo INTEGER NOT NULL,
            razao_social TEXT
            nome_fantasia TEXT,
            status TEXT,
            data_exclusao TEXT, 
            motivo_bloqueio INTEGER,
            exportado_siv TEXT,
            origem INTEGER,
            melhor_horario TEXT 
            PRIMARY KEY (unb, code)             
        );
        """)
