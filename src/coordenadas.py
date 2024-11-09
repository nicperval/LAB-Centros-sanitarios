from collections import namedtuple
import math

Coordenadas = namedtuple('Coordenadas', 'latitude, longitude')
def calcular_distancia(coord1, coord2):
    dist = math.sqrt((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2)
    return dist

def calcular_media_coordenadas(lista):
    lat = []
    lon = []
    for latitude, longitude in lista:
        lat.append(latitude)
        lon.append(longitude)
    mlat = sum(lat)/len(lat)
    mlon = sum(lon)/len(lon)
    Coordenadas = (mlat, mlon)
    return Coordenadas