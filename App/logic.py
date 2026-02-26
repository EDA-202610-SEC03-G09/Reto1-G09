import time
import csv
import os
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st


csv.field_size_limit(2147483647)
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Data")

def new_logic():
    """
    Crea el catálogo del reto.
    """
    return {"computadores": lt.new_list()}


def load_data(catalog, filename):
    """
    Carga el CSV una sola vez y retorna lo pedido en la Parte 2:
    total, tiempo, menor, mayor, primeros 5, últimos 5
    """
    start_time = get_time()

    file_path = os.path.join(data_dir, filename)

    total = 0
    menor_precio = None
    mayor_precio = None
    comp_menor = None
    comp_mayor = None

    primeros_5 = []
    ultimos_5 = lt.new_list()  

    with open(file_path, encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for comp in reader:
            # Guardar el registro en la lista principal
            lt.add_last(catalog["computadores"], comp)
            total += 1

            fila = [
                comp.get("model"),
                comp.get("brand"),
                comp.get("release_year"),
                comp.get("cpu_model"),
                comp.get("gpu_model"),
                comp.get("price")
            ]

            if total <= 5:
                primeros_5.append(fila)

            lt.add_last(ultimos_5, fila)
            if lt.size(ultimos_5) > 5:
                lt.remove_first(ultimos_5)

            texto_precio = comp.get("price", "")
            texto_precio = texto_precio.strip() if texto_precio is not None else ""
            if texto_precio != "":
                precio = float(texto_precio)

                if (menor_precio is None) or (precio < menor_precio):
                    menor_precio = precio
                    comp_menor = comp

                if (mayor_precio is None) or (precio > mayor_precio):
                    mayor_precio = precio
                    comp_mayor = comp

    ultimos_5_tabla = []
    for i in range(0, lt.size(ultimos_5)):   
        ultimos_5_tabla.append(lt.get_element(ultimos_5, i))

    menor = None
    mayor = None

    if comp_menor is not None:
        menor = (
            comp_menor.get("device_type"),
            comp_menor.get("brand"),
            comp_menor.get("model"),
            comp_menor.get("release_year"),
            comp_menor.get("os")
        )

    if comp_mayor is not None:
        mayor = (
            comp_mayor.get("device_type"),
            comp_mayor.get("brand"),
            comp_mayor.get("model"),
            comp_mayor.get("release_year"),
            comp_mayor.get("os")
        )

    end_time = get_time()
    tiempo = delta_time(start_time, end_time)

    return total, tiempo, menor, mayor, primeros_5, ultimos_5_tabla

def get_time():
    return float(time.perf_counter() * 1000)


def delta_time(start, end):
    return float(end - start)

def req_1(catalog, nombre_marca):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass
    comienzo= time.perf_counter()
    computadores = catalog["computadores"]

   
    #Cantidad de computadores de esa marca
    total_computadores = 0
    
    #Promedios computadores por marca
    prom_precio=0.0
    prom_ram = 0.0
    prom_vram = 0.0
    prom_cpu =0.0
    prom_año=0.0
    
    #Menores y mayores
    min_precio = None
    max_precio = None
    min_ram = None
    max_ram = None
    min_vram = None
    max_vram = None
    min_cpu = None
    max_cpu = None
    min_año = None
    max_año = None
    
    #Mas caro y mas barato
    comp_mas_caro = None
    comp_mas_barato = None
    peso_min = None
    
    largo = lt.size(computadores)
    for i in range (largo):
        comp = lt.get_element(computadores,i)
        if comp["brand"].lower() == nombre_marca.lower():
            total_computadores += 1
            
            #Precio
            if comp["price"] != "":
                precio = float(comp["price"])
                prom_precio += precio
                # Compara para encontrar computador mas barato
                if min_precio is None or precio < min_precio:
                    min_precio = precio
                    comp_mas_barato = comp
                    peso_min = float(comp["weight_kg"]) if comp["weight_kg"] != "" else None
                elif precio == min_precio:
                    # Desempate por menor peso
                    if comp_mas_barato is not None and comp["weight_kg"]<peso_min:
                        comp_mas_barato = comp
                        min_precio = precio
                        peso_min = float(comp["weight_kg"]) if comp["weight_kg"] != "" else None
                # Compara para encontrar computador mas caro
                if max_precio is None or precio > max_precio:
                    max_precio = precio
                    comp_mas_caro = comp
                elif precio == max_precio:
                    # Desempate por menor peso
                    if comp_mas_caro is not None and comp["weight_kg"]<peso_min:
                        comp_mas_caro = comp
                        max_precio = precio
                        peso_min = float(comp["weight_kg"]) if comp["weight_kg"] != "" else None
            
            #RAM
            if comp["ram_gb"] != "":
                ram = float(comp["ram_gb"])
                prom_ram += ram
                if min_ram is None or ram < min_ram:
                    min_ram = ram
                if max_ram is None or ram > max_ram:
                    max_ram = ram
            
            #VRAM
            if comp["vram_gb"] != "":
                vram = float(comp["vram_gb"])
                prom_vram += vram
                if min_vram is None or vram < min_vram:
                    min_vram = vram
                if max_vram is None or vram > max_vram:
                    max_vram = vram
            
            #CPU
            if comp["cpu_cores"] != "":
                cpu = float(comp["cpu_cores"])  
                if min_cpu is None or cpu < min_cpu:
                    min_cpu = cpu
                if max_cpu is None or cpu > max_cpu:
                    max_cpu = cpu
            
            #Año de lanzamiento
            if comp["release_year"] != "":
                año = float(comp["release_year"])
                prom_año += año
                if min_año is None or año < min_año:
                    min_año = año
                if max_año is None or año > max_año:
                    max_año = año
    final = time.perf_counter()
    tiempo = final - comienzo *1000
    # Calcular promedios
    if total_computadores > 0:
        prom_precio /= total_computadores
        prom_ram /= total_computadores
        prom_vram /= total_computadores
        prom_cpu /= total_computadores
        prom_año /= total_computadores
    else:
        prom_precio = 0.0
        prom_ram = 0.0
        prom_vram = 0.0
        prom_cpu = 0.0
        prom_año = 0.0
        min_precio = None
        max_precio = None
        min_ram = None
        max_ram = None
        min_vram = None
        max_vram = None
        min_cpu = None
        max_cpu = None
        min_año = None
        max_año = None
        comp_mas_caro = None
        comp_mas_barato = None
    return {
        "total_computadores": total_computadores,
        "prom_precio": prom_precio,
        "prom_ram": prom_ram,
        "prom_vram": prom_vram,
        "prom_cpu": prom_cpu,
        "prom_año": prom_año,
        "min_precio": min_precio,
        "max_precio": max_precio,
        "min_ram": min_ram,
        "max_ram": max_ram,
        "min_vram": min_vram,
        "max_vram": max_vram,
        "min_cpu": min_cpu,
        "max_cpu": max_cpu,
        "min_año": min_año,
        "max_año": max_año,
        "comp_mas_caro": comp_mas_caro,
        "comp_mas_barato": comp_mas_barato
    }, tiempo

def req_2(control, precio_min, precio_max):
    inicio = get_time()

    filtrados = lt.new_list()

    cantidad = 0
    suma_ram = 0.0
    suma_vram = 0.0
    suma_precio = 0.0

    moderno = None
    anio_moderno = None
    precio_moderno = None

    barato = None
    precio_barato = None

    caro = None
    precio_caro = None

    lista = control["computadores"]
    n = lt.size(lista)

    for i in range(n):
        comp = lt.get_element(lista, i)

        texto_precio = comp.get("price", "")
        texto_precio = texto_precio.strip() if texto_precio is not None else ""

        ok_precio = (texto_precio != "") and texto_precio.replace(".", "", 1).isdigit()

        if ok_precio:
            precio = float(texto_precio)

            if precio_min <= precio <= precio_max:
                lt.add_last(filtrados, comp)

                cantidad += 1
                suma_precio += precio

                texto_ram = comp.get("ram_gb", "")
                texto_ram = texto_ram.strip() if texto_ram is not None else ""
                if texto_ram != "" and texto_ram.replace(".", "", 1).isdigit():
                    suma_ram += float(texto_ram)

                texto_vram = comp.get("vram_gb", "")
                texto_vram = texto_vram.strip() if texto_vram is not None else ""
                if texto_vram != "" and texto_vram.replace(".", "", 1).isdigit():
                    suma_vram += float(texto_vram)

                texto_anio = comp.get("release_year", "")
                texto_anio = texto_anio.strip() if texto_anio is not None else ""
                if texto_anio.isdigit():
                    anio = int(texto_anio)

                    if (anio_moderno is None) or (anio > anio_moderno) or (anio == anio_moderno and (precio_moderno is None or precio > precio_moderno)):
                        anio_moderno = anio
                        moderno = comp
                        precio_moderno = precio

                if (precio_barato is None) or (precio < precio_barato):
                    precio_barato = precio
                    barato = comp

                if (precio_caro is None) or (precio > precio_caro):
                    precio_caro = precio
                    caro = comp

    if cantidad == 0:
        prom_ram = None
        prom_vram = None
        prom_precio = None
    else:
        prom_ram = suma_ram / cantidad
        prom_vram = suma_vram / cantidad
        prom_precio = suma_precio / cantidad

    computador_moderno = None
    computador_barato = None
    computador_caro = None

    if moderno is not None:
        computador_moderno = {
            "model": moderno.get("model"),
            "brand": moderno.get("brand"),
            "year": moderno.get("release_year"),
            "cpu": moderno.get("cpu_model"),
            "gpu": moderno.get("gpu_model"),
            "price": moderno.get("price")
        }

    if barato is not None:
        computador_barato = {
            "model": barato.get("model"),
            "brand": barato.get("brand"),
            "year": barato.get("release_year"),
            "cpu": barato.get("cpu_model"),
            "gpu": barato.get("gpu_model"),
            "price": barato.get("price")
        }

    if caro is not None:
        computador_caro = {
            "model": caro.get("model"),
            "brand": caro.get("brand"),
            "year": caro.get("release_year"),
            "cpu": caro.get("cpu_model"),
            "gpu": caro.get("gpu_model"),
            "price": caro.get("price")
        }

    fin = get_time()
    tiempo = delta_time(inicio, fin)

    return tiempo, cantidad, prom_ram, prom_vram, prom_precio, computador_moderno, computador_barato, computador_caro, filtrados

def req_3(catalog, cpu_brand, cpu_tier):
        tiempo_inicio = get_time()

        marca_cpu_buscada = cpu_brand.strip().lower()
        tier_cpu_buscado = cpu_tier.strip().lower()

        suma_precio = 0.0
        suma_ram_gb = 0.0
        suma_vram_gb = 0.0
        suma_hilos_cpu = 0.0
        cantidad_computadores = 0

        frecuencias_por_anio = {}
        frecuencias_por_gpu = {}

        lista_computadores = catalog["computadores"]
        cantidad_registros = lt.size(lista_computadores)

        for posicion in range(cantidad_registros):

            computador = lt.get_element(lista_computadores, posicion)

            texto_marca_cpu = computador.get("cpu_brand")
            texto_tier_cpu = computador.get("cpu_tier")

            texto_marca_cpu = texto_marca_cpu.strip().lower() if texto_marca_cpu is not None else ""
            texto_tier_cpu = str(texto_tier_cpu).strip().lower() if texto_tier_cpu is not None else ""

            coincide_marca_cpu = (texto_marca_cpu == marca_cpu_buscada)
            coincide_tier_cpu = (texto_tier_cpu == tier_cpu_buscado)

            if coincide_marca_cpu and coincide_tier_cpu:

                texto_precio = computador.get("price")
                texto_ram = computador.get("ram_gb")
                texto_vram = computador.get("vram_gb")
                texto_hilos = computador.get("cpu_threads")

                texto_precio = texto_precio.strip() if texto_precio is not None else ""
                texto_ram = texto_ram.strip() if texto_ram is not None else ""
                texto_vram = texto_vram.strip() if texto_vram is not None else ""
                texto_hilos = texto_hilos.strip() if texto_hilos is not None else ""

                valor_precio = float(texto_precio) if texto_precio != "" else 0.0
                valor_ram = float(texto_ram) if texto_ram != "" else 0.0
                valor_vram = float(texto_vram) if texto_vram != "" else 0.0
                valor_hilos = float(texto_hilos) if texto_hilos != "" else 0.0

                suma_precio += valor_precio
                suma_ram_gb += valor_ram
                suma_vram_gb += valor_vram
                suma_hilos_cpu += valor_hilos

                cantidad_computadores += 1

                texto_anio = computador.get("release_year")
                texto_gpu = computador.get("gpu_brand")

                texto_anio = str(texto_anio).strip() if texto_anio is not None else ""
                texto_gpu = str(texto_gpu).strip() if texto_gpu is not None else ""

                if texto_anio in frecuencias_por_anio:
                    frecuencias_por_anio[texto_anio] += 1
                else:
                    frecuencias_por_anio[texto_anio] = 1

                if texto_gpu in frecuencias_por_gpu:
                    frecuencias_por_gpu[texto_gpu] += 1
                else:
                    frecuencias_por_gpu[texto_gpu] = 1

        if cantidad_computadores == 0:
            return [["Mensaje", "No se encontraron computadores para la marca: " + cpu_brand + " y el tier: " + cpu_tier]]

        precio_promedio = suma_precio / cantidad_computadores
        ram_promedio = suma_ram_gb / cantidad_computadores
        vram_promedio = suma_vram_gb / cantidad_computadores
        hilos_promedio = suma_hilos_cpu / cantidad_computadores

        anio_mas_frecuente = ""
        frecuencia_maxima_anio = -1
        for anio_actual in frecuencias_por_anio:
            frecuencia_anio_actual = frecuencias_por_anio[anio_actual]
            if frecuencia_anio_actual > frecuencia_maxima_anio:
                frecuencia_maxima_anio = frecuencia_anio_actual
                anio_mas_frecuente = anio_actual

        gpu_mas_frecuente = ""
        frecuencia_maxima_gpu = -1
        for gpu_actual in frecuencias_por_gpu:
            frecuencia_gpu_actual = frecuencias_por_gpu[gpu_actual]
            if frecuencia_gpu_actual > frecuencia_maxima_gpu:
                frecuencia_maxima_gpu = frecuencia_gpu_actual
                gpu_mas_frecuente = gpu_actual

        tiempo_final = get_time()
        tiempo_ejecucion = delta_time(tiempo_inicio, tiempo_final)

        resultado = [
            ["Computadores encontrados", cantidad_computadores],
            ["Precio promedio", round(precio_promedio, 2)],
            ["RAM promedio (GB)", round(ram_promedio, 2)],
            ["VRAM promedio (GB)", round(vram_promedio, 2)],
            ["Hilos promedio CPU", round(hilos_promedio, 2)],
            ["Año más frecuente", anio_mas_frecuente],
            ["GPU más frecuente", gpu_mas_frecuente],
            ["Tiempo de ejecución (ms)", round(tiempo_ejecucion, 2)]
        ]

        return resultado

def req_4(catalog,cpu_brand,gpu_model):
    
    inicio =   time.perf_counter()
    cumplen = 0
    #Promedios
    precio_prom = 0.0
    ram_prom = 0.0  
    vram_prom = 0.0
    cpuboost_prom = 0.0
    #mayores
    mayor_1 = None
    mayor_2 = None
    
    computadores = catalog["computadores"]
    largo = lt.size(computadores)
    for i in range (largo):
        comp = lt.get_element(computadores,i)
        if comp["cpu_brand"].lower() == cpu_brand.lower() and comp["gpu_model"].lower() == gpu_model.lower():
            cumplen += 1
            
            #Precio
            if comp["price"] != "":
                precio = float(comp["price"])
                precio_prom += precio
                if mayor_1 is None or precio > float(mayor_1["price"]):
                    mayor_1 = comp
                elif mayor_2 is None or precio > float(mayor_2["price"]):
                    mayor_2 = comp
                elif precio == mayor_1["price"]:
                    if mayor_1 is not None and comp["weight_kg"]<float(mayor_1["weight_kg"]):
                        mayor_1 = comp
                elif precio == mayor_2["price"]:
                    if mayor_2 is not None and comp["weight_kg"]<float(mayor_2["weight_kg"]):
                        mayor_2 = comp
            #RAM
            if comp["ram_gb"] != "":
                ram = float(comp["ram_gb"])
                ram_prom += ram
                
            
            #VRAM
            if comp["vram_gb"] != "":
                vram = float(comp["vram_gb"])
                vram_prom += vram
            
            #CPU Boost
            if comp["cpu_boost_ghz"] != "":
                cpuboost = float(comp["cpu_boost_ghz"])
                cpuboost_prom += cpuboost
    final = time.perf_counter()
    tiempo = final - inicio *1000
    if cumplen > 0:
        precio_prom /= cumplen
        ram_prom /= cumplen
        vram_prom /= cumplen
        cpuboost_prom /= cumplen
    else:
        precio_prom = 0.0
        ram_prom = 0.0  
        vram_prom = 0.0
        cpuboost_prom = 0.0
        mayor_1 = None
        mayor_2 = None
    return {
        "cumplen": cumplen,
        "precio_prom": precio_prom,
        "ram_prom": ram_prom,
        "vram_prom": vram_prom,
        "cpuboost_prom": cpuboost_prom,
        "mayor_1": [mayor_1["brand"], mayor_1["model"],mayor_1["release_year"],mayor_1["cpu_model"],mayor_1["price"]] if mayor_1 else None,
        "mayor_2": [mayor_2["brand"], mayor_2["model"],mayor_2["release_year"],mayor_2["cpu_model"],mayor_2["price"]] if mayor_2 else None
    }, tiempo
    
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog,filtro,resolucion,año_min, año_max):
    
    inicio = time.perf_counter()
    cumplen = 0
    
    #Promedios 
    ancho_promo= 0.0
    alto_prom = 0.0
    precio_prom = 0.0
    gpu_prom =0.0
    
    comp_requerimiento = None
    peso_requerimiento = None
    
    computadores = catalog["computadores"]
    largo = lt.size(computadores)
    
    if filtro == "mayor":
        for i in range (largo):
            comp = lt.get_element(computadores,i)
            if comp["display_resolution"] == resolucion and comp["release_year"] != "" and año_min <= float(comp["release_year"]) <= año_max:
                cumplen += 1
                
                #Ancho y alto
                if comp["display_resolution"] != "":
                    resol = comp["display_resolution"].lower().split("x")
                    if len(resol) == 2:
                        ancho = float(resol[0].strip())
                        alto = float(resol[1].strip())
                        ancho_promo += ancho
                        alto_prom += alto
                
                #Precio
                if comp["price"] != "":
                    precio = float(comp["price"])
                    precio_prom += precio
                    
                #GPU
                if comp["gpu_tier"] != "":
                    gpu = float(comp["gpu_tier"])
                    gpu_prom += gpu
                
                #Computador mas caro con menor peso
                if comp_requerimiento is None or (precio > float(comp_requerimiento["price"])) or (precio == float(comp_requerimiento["price"]) and float(comp["weight_kg"]) < float(peso_requerimiento)):
                    comp_requerimiento = comp
                    peso_requerimiento = comp["weight_kg"]
    elif filtro == "menor":
        for i in range (largo):
            comp = lt.get_element(computadores,i)
            if comp["display_resolution"] == resolucion and comp["release_year"] != "" and año_min <= float(comp["release_year"]) <= año_max:
                cumplen += 1
                
                #Ancho y alto
                if comp["display_resolution"] != "":
                    resol = comp["display_resolution"].lower().split("x")
                    if len(resol) == 2:
                        ancho = float(resol[0].strip())
                        alto = float(resol[1].strip())
                        ancho_promo += ancho
                        alto_prom += alto
                
                #Precio
                if comp["price"] != "":
                    precio = float(comp["price"])
                    precio_prom += precio
                    
                #GPU
                if comp["gpu_tier"] != "":
                    gpu = float(comp["gpu_tier"])
                    gpu_prom += gpu
                
                #Computador mas barato con menor peso
                if comp_requerimiento is None or (precio < float(comp_requerimiento["price"])) or (precio == float(comp_requerimiento["price"]) and float(comp["weight_kg"]) < float(peso_requerimiento)):
                    comp_requerimiento = comp
                    peso_requerimiento = comp["weight_kg"]
    final = time.perf_counter()
    tiempo = final - inicio *1000
    if cumplen > 0:
        ancho_promo /= cumplen
        alto_prom /= cumplen
        precio_prom /= cumplen
        gpu_prom /= cumplen
    else:
        ancho_promo = 0.0
        alto_prom = 0.0
        precio_prom = 0.0
        gpu_prom = 0.0
        comp_requerimiento = None
        peso_requerimiento = None
    return {
        "filtro": filtro,
        "cumplen": cumplen,
        "Tamaño_prom": str(ancho_promo)+"x"+str(alto_prom),
        "precio_prom": precio_prom,
        "gpu_prom": gpu_prom,
        "comp_requerimiento": [comp_requerimiento["price"], comp_requerimiento["resolution"],comp_requerimiento["gpu_tier"],comp_requerimiento["display_type"],comp_requerimiento["weight_kg"],comp_requerimiento["release_year"]] if comp_requerimiento else None,
    }, tiempo
    
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog, año_inicial, año_final):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass
    inicio = get_time()

    lista_nueva = sl.new_list()
    registros = 0 
    os_usado = None
    cantidad = 0 
    os_mas_recauda = None
    max_recaudo = 0

    tamaño = lt.size(catalog["computadores"])
    for i in range(tamaño):
        elemento = lt.getElement(catalog["computadores"], i)
        if elemento["release_year"] >= año_inicial and elemento["release_year"] <= año_final:
            sl.add_last(lista_nueva, elemento)
            registros += 1 
        
        
    tamaño_nueva = sl.size(lista_nueva)
    resultados_por_os = sl.newList()
    for i in range (1, sl.size(lista_nueva)+1):
        elemento = sl.get_element(lista_nueva, i)
        os_actual = elemento["os"]
    
        cantidad_os = 0
        recaudo_os = 0
        suma_peso = 0 
    
        precio_min = 99999999
        precio_max = 0 
    
        barato = None 
        caro = None
        for j in range(1, tamaño_nueva + 1):
            elementoj = sl.get_element(lista_nueva, j)

            if elementoj["os"] == os_actual:
                cantidad_os += 1
                precio = float(elementoj["price"])
                
                peso = float(elementoj["weight"])
            
                recaudo_os += precio
                
                suma_peso += peso
            
                if precio < precio_min:
                    precio_min = precio
                    barato = elementoj

                if precio > precio_max:
                    precio_max = precio
                    caro = elementoj
                
        if cantidad_os > cantidad:
            cantidad = cantidad_os
            os_mas_usado = os_actual

        if recaudo_os > max_recaudo:
            max_recaudo = recaudo_os
            os_mas_recauda = os_actual
        
        precio_promedio = recaudo_os / cantidad_os
        peso_promedio = suma_peso / cantidad_os
    
        info_os = {
            "os": os_actual,
            "cantidad": cantidad_os,
            "recaudo": recaudo_os,
            "precio_promedio": precio_promedio,
            "peso_promedio": peso_promedio,
            "mas_caro": caro,
            "mas_barato": barato
            }

        sl.addLast(resultados_por_os, info_os)
    
    final = get_time()
    tiempo = final - inicio
    
    
    info = [
    ["Tiempo de ejecución ", round(tiempo, 2)],
    ["registros en rango", registros],
    ["os más usado", os_mas_usado],
    ["Cantidad del OS más usado", cantidad],
    ["OS con mayor recaudo", os_mas_recauda],
    ["Recaudo máximo", (max_recaudo, 2)]
]

    return info , resultados_por_os

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
