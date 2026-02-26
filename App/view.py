import sys
import App.logic as logic
from tabulate import tabulate

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    return logic.new_logic()

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    archivo = input("Nombre del archivo (ej: computers-small.csv): ").strip()

    total, tiempo, menor, mayor, primeros, ultimos = logic.load_data(control, archivo)

    print("\nTiempo de carga (ms):", round(tiempo, 3))
    print("Total computadores cargados:", total)

    print("\nComputador con MENOR precio:")
    if menor is None:
        print("No hay computadores con precio válido.")
    else:
        tipo, marca, modelo, anio, so = menor
        print("Tipo:", tipo, "| Marca:", marca, "| Modelo:", modelo, "| Año:", anio, "| OS:", so)

    print("\nComputador con MAYOR precio:")
    if mayor is None:
        print("No hay computadores con precio válido.")
    else:
        tipo, marca, modelo, anio, so = mayor
        print("Tipo:", tipo, "| Marca:", marca, "| Modelo:", modelo, "| Año:", anio, "| OS:", so)

    print("\nPrimeros 5 computadores (model, brand, year, cpu, gpu, price):")
    for fila in primeros:
        print(fila)

    print("\nÚltimos 5 computadores (model, brand, year, cpu, gpu, price):")
    for fila in ultimos:
        print(fila)

    return control

def print_data(control, id):
    n = control["computadores"]["size"]
    if id < 0 or id >= n:
        print("ID fuera de rango. Rango válido: 0 a", n - 1)
        return

    comp = control["computadores"]["elements"][id]
    print("\nComputador en posición", id, ":")
    print(comp)

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    nombre_marca = input("Ingrese el nombre de la marca: ").strip()
    resultado, tiempo = logic.req_1(control, nombre_marca)

    print(f"\nResultados para la marca: {nombre_marca}")
    print("Tiempo de ejecución (ms):", round(tiempo, 3))

    print("\nTotal computadores:", resultado.get("total_computadores", 0))

    print("\nPromedios:")
    print(" \n- Precio promedio:", round(resultado.get("prom_precio", 0), 3))
    print(" \n- RAM promedio (GB):", round(resultado.get("prom_ram", 0), 3))
    print(" \n- VRAM promedio (GB):", round(resultado.get("prom_vram", 0), 3))
    print(" \n- Núcleos CPU promedio:", round(resultado.get("prom_cpu", 0), 3))
    print(" \n- Año promedio:", round(resultado.get("prom_año", 0), 3))

    print("\nRangos (min / max):")
    print(" \n- Precio:", resultado.get("min_precio"), "/", resultado.get("max_precio"))
    print(" \n- RAM (GB):", resultado.get("min_ram"), "/", resultado.get("max_ram"))
    print(" \n- VRAM (GB):", resultado.get("min_vram"), "/", resultado.get("max_vram"))
    print(" \n- Núcleos CPU:", resultado.get("min_cpu"), "/", resultado.get("max_cpu"))
    print(" \n- Año:", resultado.get("min_año"), "/", resultado.get("max_año"))

    print("\nComputador MÁS CARO (desempate por menor peso si aplica):")
    caro = resultado.get("comp_mas_caro")
    if caro:
        print(" - Modelo:", caro.get("model"))
    else:
        print(" - Ninguno")

    print("\nModelo MÁS BARATO (desempate por menor peso si aplica):")
    barato = resultado.get("comp_mas_barato")
    if barato:
        print(" - Modelo:", barato.get("model"))
    else:
        print(" - Ninguno")

    return control
    


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    
    cpu_brand= input("Ingrese el nombre de la marca de CPU: ").strip()
    gpu_model= input("Ingrese el modelo de GPU: ").strip()
    resultado, tiempo = logic.req_4(control, cpu_brand, gpu_model)
    print(f"\nResultados para CPU marca: {cpu_brand} y GPU modelo: {gpu_model}")
    print("Tiempo de ejecución (ms):", round(tiempo, 3))
    print("\nTotal computadores encontrados:", resultado.get("cumplen", 0))
    mayor_1 = resultado.get("mayor_1")
    mayor_2 = resultado.get("mayor_2")
    if mayor_1 and mayor_2:
     print("\nLos dos computadores mas costosos que cumplen con los criterios son:","\n1",mayor_1,"\n2",mayor_2)
    else:
        print("\nNo se encontraron computadores que cumplan con los criterios.")
    print("\nPromedios:")
    print(" \n- Precio promedio:", round(resultado.get("precio_prom", 0), 3))
    print(" \n- RAM promedio (GB):", round(resultado.get("ram_prom", 0), 3))
    print(" \n- VRAM promedio (GB):", round(resultado.get("vram_prom", 0), 3))
    print(" \n- Promedio en modo boost del procesador:", round(resultado.get("cpuboost_prom", 0), 3))
    
    return control

    
    
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    
    filtro = input("Ingrese el filtro de busqueda (ej: 'Mayor', 'Menor'): ").strip().lower()
    resolucion = input("Ingrese la resolución deseada (ej: '1920x1080'): ").strip()
    año_min = int(input("Ingrese el año mínimo de búsqueda: "))
    año_max= int(input("Ingrese el año máximo de búsqueda: "))
    resultado, tiempo = logic.req_5(control, filtro, resolucion, año_min, año_max)
    print(f"\nResultados para filtro: {filtro}, resolución: {resolucion}, año mínimo: {año_min}, año máximo: {año_max}")
    print("Tiempo de ejecución (ms):", round(tiempo, 3))
    print("\nTotal computadores encontrados:", resultado.get("cumplen", 0))
    comp_requerido = resultado.get("comp_requerimiento")
    if comp_requerido:
        print("\nComputador más", "caro que cumple condiciones" if filtro == "mayor" else "barato que cumple condiciones", ":")
        print(comp_requerido)
    else:
        print("\nNo se encontraron computadores que cumplan con las condiciones.")
    print("\nPromedios:")
    print(" \n- Precio promedio:", round(resultado.get("precio_prom", 0), 3))
    print(" \n- Tamaño Prom:", round(resultado.get("Tamaño_prom", 0), 3))
    print(" \n- GPU tier promedio",round(resultado.get("gpu_prom", 0), 3))
    print("\n Gracias:)")
    
    
    return control
        
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
