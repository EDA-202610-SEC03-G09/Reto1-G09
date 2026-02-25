import time
import csv
import os
from DataStructures.List import array_list as lt

csv.field_size_limit(2147483647)
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Data")

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        "computadores": lt.new_list()
    }
    return catalog

def load_data(catalog, filename):

    start_time = get_time()

    load_computadores(catalog, filename)

    total = catalog["computadores"]["size"]

    def comp_menor_precio(catalog):
        precio_menor = None
        indice = None

        for x in range(0, catalog["computadores"]["size"]):
            comp = catalog["computadores"]["elements"][x]
            if comp["price"] != "":
                precio = float(comp["price"])
                if (precio_menor is None) or (precio < precio_menor):
                    precio_menor = precio
                    indice = x

        if indice is None:
            return None

        c = catalog["computadores"]["elements"][indice]
        return (c["device_type"], c["brand"], c["model"], c["release_year"], c["os"])

    def comp_mayor_precio(catalog):
        precio_mayor = None
        indice = None

        for x in range(0, catalog["computadores"]["size"]):
            comp = catalog["computadores"]["elements"][x]
            if comp["price"] != "":
                precio = float(comp["price"])
                if (precio_mayor is None) or (precio > precio_mayor):
                    precio_mayor = precio
                    indice = x

        if indice is None:
            return None

        c = catalog["computadores"]["elements"][indice]
        return (c["device_type"], c["brand"], c["model"], c["release_year"], c["os"])

    menor = comp_menor_precio(catalog)
    mayor = comp_mayor_precio(catalog)

    def primeras_5(catalog):
        resultados = []
        n = catalog["computadores"]["size"]
        limite = 5 if n >= 5 else n

        for i in range(limite):
            comp = catalog["computadores"]["elements"][i]
            resultados.append([
                comp["model"],
                comp["brand"],
                comp["release_year"],
                comp["cpu_model"],
                comp["gpu_model"],
                comp["price"]
            ])
        return resultados

    def ultimas_5(catalog):
        resultados = []
        n = catalog["computadores"]["size"]
        inicio = n - 5
        if inicio < 0:
            inicio = 0

        for i in range(inicio, n):
            comp = catalog["computadores"]["elements"][i]
            resultados.append([
                comp["model"],
                comp["brand"],
                comp["release_year"],
                comp["cpu_model"],
                comp["gpu_model"],
                comp["price"]
            ])
        return resultados

    primeros_tabla = primeras_5(catalog)
    ultimos_tabla = ultimas_5(catalog)

    end_time = get_time()
    d_time = delta_time(start_time, end_time)

    return total, d_time, menor, mayor, primeros_tabla, ultimos_tabla


def load_computadores(catalog, filename):
    file = os.path.join(data_dir, filename)
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for comp in input_file:
        lt.add_last(catalog["computadores"], comp)
    return lt.size(catalog["computadores"])


# -----------------------------------------------------
# Funciones para medir tiempos de ejecucion
# -----------------------------------------------------

def get_time():
    return float(time.perf_counter() * 1000)


def delta_time(start, end):
    return float(end - start)

def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
