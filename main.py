# Importa funciones de otros archivos para usar en el menú
from funciones.crearDic import csvAdic
from funciones.ordernarDic import menu_ordenar
from funciones.mostrarEstadisticas import menu_estadisticas
from funciones.buscarPais import buscar
from funciones.filtrarPaises import menu_filtrar_paises
import os
# Importacion para darle color y estilo a algunos textos
from colorama import Fore, Style, init

init()

def limpiar_consola(): 
    os.system("cls")

# Si este archivo se ejecuta directamente, se ejecuta lo siguiente
if(__name__ == "__main__"): 
    # Carga los datos del archivo CSV en una lista de objetos
    lista_objetos = csvAdic("paises_dataset.csv")

    # Bandera para mantener el menú en un bucle hasta que el usuario decida salir
    bandera = True

    # Bucle principal del menú
    while bandera: 
        # limpiar_consola()
        # Opciones del menú
        print(f"""
        {Fore.YELLOW}===== MENÚ DE OPCIONES =====
        {Fore.BLUE}1. {Style.RESET_ALL}Buscar un país por nombre (coincidencia parcial o exacta)

        {Fore.BLUE}2. {Style.RESET_ALL}Filtrar países por:
        a) Continente
        b) Rango de población
        c) Rango de superficie

        {Fore.BLUE}3. {Style.RESET_ALL}Ordenar países por:
        a) Nombre
        b) Población
        c) Superficie (ascendente o descendente)

        {Fore.BLUE}4. {Style.RESET_ALL}Mostrar estadísticas:
        a) País con mayor y menor población
        b) Promedio de población
        c) Promedio de superficie
        d) Cantidad de países por continente

        {Fore.BLUE}0. {Style.RESET_ALL}Salir
        ============================
        """)

        # Pide al usuario que ingrese una opción
        opcion:str = input("Ingrese una opcion: ") 
        
        # Dependiendo de la opción, llama a la función correspondiente
        if opcion == "1":
            buscar(lista_objetos) 

        elif opcion == "2": 
            menu_filtrar_paises(lista_objetos)

        elif opcion == "3": 
            menu_ordenar(lista_objetos)

        elif opcion == "4": 
            menu_estadisticas(lista_objetos) 
        
        elif opcion == "0":
            # Si el usuario elige salir, termina el bucle
            print("Terminamos, gracias por usar la app")
            bandera = False
        else: 
            print(f"{Fore.RED}Opción inválida. Intente nuevamente.")
        