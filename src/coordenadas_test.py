from coordenadas import *
from centros import *

def test_calcular_distancia(coord1, coord2):
    res = calcular_distancia(coord1, coord2)
    print(res)

def test_calcular_media_coordenadas(lista):
    lis = []
    for name, local, Coordenadas, est, camas, discapacitados, uci in lista:
        lis.append(Coordenadas)
    res = calcular_media_coordenadas(lis)
    print(res)

if __name__ == '__main__':
    test_calcular_distancia((1838,3892), (8203,6329))
    lista = leer_centros('data/centrosSanitarios.csv')
    test_calcular_media_coordenadas(lista)
