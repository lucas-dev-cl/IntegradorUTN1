from funciones.paginacionConsola import paginar 
from colorama import Fore, Style,init

init()

# Modulo para ordenar el archivos
# Ordenar de manera ascendente por nombre
def ordenar_objetos(lista, propiedad):
    lista_ordenada = lista.copy()

    # Recorremos los archivos para comparar
    for i in range(len(lista_ordenada) - 1): 
        # Recorremos los archivos por pares y lo cambiamos de forma ascendente
        for j in range(len(lista_ordenada) - i - 1): 
            val1 = lista_ordenada[j][propiedad]
            val2 = lista_ordenada[j + 1][propiedad]

            # Intentamos convertir los valores a número
            try:
                val1_num = float(val1)
                val2_num = float(val2)
                if val1_num > val2_num:
                    lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
            except ValueError:
                # Si no son números, los comparamos como texto
                if str(val1).lower() > str(val2).lower():
                    lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    
    paginar(lista_ordenada)
    

def ordenar_objetos_desc(lista, propiedad): 
    lista_ordenada = lista.copy()

    # Recorremos los archivos para comparar
    for i in range(len(lista_ordenada) - 1): 
        # Recorremos los archivos por pares y lo cambiamos de forma ascendente
        for j in range(len(lista_ordenada) - i - 1): 
            val1 = lista_ordenada[j][propiedad]
            val2 = lista_ordenada[j + 1][propiedad]

            # Intentamos convertir los valores a número
            try:
                val1_num = float(val1)
                val2_num = float(val2)
                if val1_num < val2_num:
                    lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
            except ValueError:
                # Si no son números, los comparamos como texto
                if str(val1).lower() < str(val2).lower():
                    lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]

    paginar(lista_ordenada)
    
# Menú para ordenar la lista de países según diferentes criterios
def menu_ordenar(lista): 
    bandera = True
    while bandera:
        # Muestra las opciones de ordenamiento
        print(f"""
        {Fore.YELLOW}--- Opciones de ordenamiento (Opción 3) ---{Style.RESET_ALL}
        a) Ordenar por nombre
        b) Ordenar por poblacion
        c) Ordenar por superficie
        d) Volver al menú principal
        """)

        # Pide al usuario que ingrese una subopción
        subopcion: str = input("Ingrese una subopción de ordenamiento: ").lower()
        
        # Ordena según la opción elegida
        if subopcion == "a":
            ordenar_objetos(lista, "pais")  # Ordena por nombre
        elif subopcion == "b":
            ordenar_objetos(lista, "poblacion")  # Ordena por población
        elif subopcion == "c":
            # Si se elige superficie, pregunta si ascendente o descendente
            print(f"""
            {Fore.YELLOW}Elegir por:
            a) Ascendente
            b) Descendente
            """)
            while True: 
                opcion:str = input("Ingrese opcion: ").lower() 

                if opcion == "a": 
                    print("Paises ordenados por superficie (ascendente): ")
                    ordenar_objetos(lista, "superficie")  # Ascendente
                elif opcion == "b": 
                    print("Paises ordenados por superficie (descendente): ")
                    ordenar_objetos_desc(lista, "superficie")  # Descendente
                else:
                    print(" Opción inválida. Intente de nuevo.")   
        elif subopcion == "d": 
            # Sale del menú
            bandera = False 
        else:
            # Opción inválida
            print(f"{Fore.RED} Opción inválida. Intente de nuevo.")
