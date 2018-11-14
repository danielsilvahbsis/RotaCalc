from flask import Flask
from Cliente import Cliente
from Vendedor import Vendedor
from Frequencia import Frequencia
from Projeto import Projeto
from Rota import Rota

app = Flask(__name__)
lista_rota = []


@app.route('/')
def main():
    lista_frequencia = get_lista_frequencia()
    calcula_rota(lista_frequencia)


def calcula_rota(lista_frequencia):
    for frequencia in lista_frequencia:
        vendedor = ler_vendedor(frequencia.vendedor)
        cliente = ler_cliente(frequencia.cliente)
        if is_vendedor_interno(vendedor) and is_cliente_elegivel(cliente) and is_dia_rota(frequencia):
            insert_rota(frequencia)

    for rota in lista_rota:
        print(str(rota))


def get_lista_frequencia():
    visita_semanal = [['S', 'N', 'N', 'S', 'N', 'N', 'N'], ['S', 'N', 'N', 'S', 'N', 'N', 'N'],
              ['S', 'N', 'N', 'S', 'N', 'N', 'N'], ['S', 'N', 'N', 'S', 'N', 'N', 'N']]

    visita_mensal = [['N', 'N', 'N', 'N', 'N', 'N', 'N'], ['N', 'N', 'N', 'N', 'N', 'N', 'N'],
              ['N', 'N', 'S', 'N', 'N', 'N', 'N'], ['N', 'N', 'N', 'N', 'N', 'N', 'N']]

    visita_quizenal = [['N', 'N', 'N', 'N', 'N', 'N', 'N'], ['N', 'N', 'N', 'N', 'N', 'N', 'N'],
              ['N', 'N', 'N', 'N', 'N', 'N', 'N'], ['N', 'N', 'N', 'N', 'S', 'N', 'N']]

    lista_frequencia = []

    # Cliente 1
    frequencia1 = Frequencia(204, 1, 700, 9, 'S', '', visita_semanal)
    lista_frequencia.append(frequencia1)

    # Cliente 2
    frequencia2 = Frequencia(204, 2, 700, 9, 'Q', '', visita_quizenal)
    lista_frequencia.append(frequencia2)

    # Cliente 3
    frequencia3 = Frequencia(204, 3, 701, 9, 'M', '', visita_mensal)
    lista_frequencia.append(frequencia3)

    # Cliente 4
    frequencia4 = Frequencia(204, 4, 701, 9, 'S', '', visita_semanal)
    lista_frequencia.append(frequencia4)

    return lista_frequencia


def ler_vendedor(codigo):
    if codigo == 700:
        return Vendedor(204, codigo, "Bruna Venceslau", 70, 8, "BRTEI0070")
    if codigo == 701:
        return Vendedor(204, codigo, "Karynn Naara", 70, 8, "BRTEI0071")


def ler_cliente(codigo):
    if codigo == 1:
        return Cliente(204, codigo, "Daniel Silva", "Careado", "A", "", 0, "S", 1, "10:30")

    if codigo == 2:
        return Cliente(204, codigo, "Deise Rech", "Teisse", "A", "", 0, "S", 1, "11:30")

    if codigo == 3:
        return Cliente(204, codigo, "Otávio Coelho", "Otavião de Consumo", "A", "", 0, "S", 1, "09:30")

    if codigo == 4:
        return Cliente(204, codigo, "Vinícius de Borba", "Vini", "A", "", 0, "S", 1, "09:30")


def insert_rota(frequencia):
    rota = Rota(frequencia.unb, frequencia.vendedor, frequencia.cliente, 'R')
    lista_rota.append(rota)


def is_vendedor_interno(vendedor):
    if vendedor.cargo == 8:
        return True


def is_cliente_elegivel(cliente):
    if cliente.status == 'I' or cliente.data_exclusao != '':
        return False
    if cliente.status == 'B':
        if cliente.motivo_bloqueio == 70 or cliente.motivo_bloqueio == 70:
            return False
        if cliente.motivo_bloqueio == 69 and is_projeto_habilitado(cliente.unb, 238):
            return False
    if cliente.status == 'C':
        if cliente.exportado_siv == 'S':
            return False
        if cliente.motivo_bloqueio == 47 and is_projeto_habilitado(cliente.unb, 85):
            return False
        if cliente.exportado_siv != 'S' and cliente.origem == 'P':
            return False
    return True


def is_dia_rota(frequencia):
    dia_semana = get_dia_semana()
    total_dias = get_total_dias_frequencia(frequencia.data_inicial)

    if frequencia.periodicidade == 'S':
        if dia_semana == get_dia_semana_semanal(frequencia.frequencia_visita):
            return True

    if frequencia.periodicidade == 'Q':
        if total_dias % 14 == 0:
            return True

    if frequencia.periodicidade == 'M':
        if total_dias % 28 == 0:
            return True

    return False


def is_projeto_habilitado(unb, codigo):
    projeto = Projeto(unb, codigo)
    return True


def get_frequencia_cliente(cliente):
    return Frequencia(204, 100, 700, 8, 'S', 20170801, 0, 3)


def get_dia_semana():
    # (1-segunda à 7-domingo)
    return 1


def get_dia_semana_semanal(frequencia_visita):
    return 1


def get_total_dias_frequencia(data_inicial):
    # quantidade de dias corridos desde a primeira visita
    return 56


if __name__ == '__main__':
    main()
