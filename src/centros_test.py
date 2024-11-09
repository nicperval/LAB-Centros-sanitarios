from centros import *

def test_leer_centros(ruta):
    res = leer_centros(ruta)
    print(res)

def test_calcular_total_camas_centros_accesibles(lista):
    res = calcular_total_camas_centros_accesibles(lista)
    print(res)

def test_obtener_centros_con_uci_cercanos_a(lista, coord, k):
    res = obtener_centros_con_uci_cercanos_a(lista, coord, k)
    print(res)

def test_generar_mapa(lista, ruta_a_guardar):
    lis = []
    for name, local, coord, est, camas, disc, uci in lista:
        tupla = (name, local, coord)
        lis.append(tupla)
    generar_mapa(lis,ruta_a_guardar)


if __name__ == '__main__':
    test_leer_centros('data/centrosSanitarios.csv')
    lista = leer_centros('data/centrosSanitarios.csv')
    test_calcular_total_camas_centros_accesibles(lista)
    test_obtener_centros_con_uci_cercanos_a(lista, (6482,8726), 5)
    test_generar_mapa(lista, 'data/mapa_centros.html')


