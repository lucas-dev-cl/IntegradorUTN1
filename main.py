from funciones.crearDic import csvAdic
from funciones.ordernarDic import ordenar_objetos
from funciones.ordernarDic import ordenar_objetos_desc
from funciones.promedioDic import promedioDic
from funciones.mostrarEstadisticas import paises_por_continente
from funciones.buscarPais import buscar

if(__name__ == "__main__"): 
    lista_objetos = csvAdic("paises_dataset.csv")

    bandera = True

    while bandera: 
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

        opcion :str = input("Ingrese una opcion: ")

        if opcion not in ["0", "1", "2", "3", "4"]:
            print("Opción inválida. Intente nuevamente.") 
        
        elif opcion == "1":
            buscar(lista_objetos) 
        
        else:
            if opcion == "0":
                print("Terminamos")
                bandera = False
                




