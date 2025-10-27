# Importa funciones de otros archivos para usar en el menú
from funciones.crearDic import csvAdic
from funciones.ordernarDic import menu_ordenar
from funciones.mostrarEstadisticas import menu_estadisticas
from funciones.buscarPais import buscar
from funciones.filtrarPaises import menu_filtrar_paises

# Si este archivo se ejecuta directamente, se ejecuta lo siguiente
if(__name__ == "__main__"): 
    # Carga los datos del archivo CSV en una lista de objetos
    lista_objetos = csvAdic("paises_dataset.csv")

    # Bandera para mantener el menú en un bucle hasta que el usuario decida salir
    bandera = True

    # Bucle principal del menú
    while bandera: 
        # Opciones del menú
        print("""
        ===== MENÚ DE OPCIONES =====

        1. Buscar un país por nombre (coincidencia parcial o exacta)

        2. Filtrar países por:
        a) Continente
        b) Rango de población
        c) Rango de superficie

        3. Ordenar países por:
        a) Nombre
        b) Población
        c) Superficie (ascendente o descendente)

        4. Mostrar estadísticas:
        a) País con mayor y menor población
        b) Promedio de población
        c) Promedio de superficie
        d) Cantidad de países por continente

        0. Salir
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
            print("Terminamos")
            bandera = False
        else: 
            print("Opción inválida. Intente nuevamente.")
