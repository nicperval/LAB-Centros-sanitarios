from collections import namedtuple
import csv
import folium
import folium.map

Coordenadas = namedtuple('Coordenadas', 'latitude, longitude')
CentroSanitario = namedtuple('CentroSanitario', 'nombre, localidad, ubicacion, estado, num_camas, acceso_discapacitados, tiene_uci')

def leer_centros(ruta):
    with open(ruta, encoding='utf-8') as f:
        fichero = csv.reader(f, delimiter=';')
        next(fichero)
        lista = []
        for name, local, lat, lon, est, camas, discapacitados, uci in fichero:
            lat = float(lat)
            lon = float(lon)
            Coordenadas = (lat, lon)
            CentroSanitario = (name, local, Coordenadas, est, camas, discapacitados, uci)
            lista.append(CentroSanitario)
    return lista

def calcular_total_camas_centros_accesibles(lista):
    x = 0
    for nombre, localidad, coordenadas, estado, num_camas, acceso_discapacitados, uci in lista:
        if acceso_discapacitados == True:
            x += num_camas
    return x

def obtener_centros_con_uci_cercanos_a(lista, coord, k):
    lis = []
    for nombre, localidad, coordenadas, estado, num_camas, acceso_discapacitados, uci in lista:
        if uci == True:
            if (coordenadas[0]+k <= coord[0]) and (coord[1]+k <= coord[1]):
                tupla = (nombre, localidad, coordenadas)
                lis.append(tupla)
    return lis

def generar_mapa(lista, ruta_a_guardar):
    lat = []
    lon = []
    for nombre,localidad,coordenadas in lista:
        lat.append(coordenadas[0])
        lon.append(coordenadas[1])
    mlat = sum(lat)/len(lat)
    mlon = sum(lon)/len(lon)
    mapa = folium.Map(location=[mlat,mlon])
    for nombre,localidad,coordenadas in lista:
        etiqueta = nombre
        color = 'green'
        marcador = folium.Marker([coordenadas[0], coordenadas[1]], popup=etiqueta, icon=folium.Icon(color=color, icon='info-sign'))
        marcador.add_to(mapa)
    mapa.save(ruta_a_guardar)


