def paises_por_continente(lista): 
    america = 0
    asia = 0
    europa = 0
    oceania = 0
    africa = 0
    antarctic = 0

    # Recorremos por cada objeto y sumamos las coincidencias
    for objeto in lista: 
        if(objeto["continente"] == "Americas"): 
            america += 1
        elif(objeto["continente"] == "Asia"): 
            asia += 1
        elif(objeto["continente"] == "Europe"): 
            europa += 1
        elif(objeto["continente"] == "Africa"): 
            africa += 1
        elif(objeto["continente"] == "Antarctic"): 
            antarctic += 1
        elif(objeto["continente"] == "Oceania"): 
            oceania += 1

    print(f"""
        Cantidad de paises en America: {america}
        Cantidad de paises en Asia: {asia}
        Cantidad de paises en Europa: {europa}
        Cantidad de paises en Oceania: {oceania}
        Cantidad de paises en Africa: {africa}
        Cantidad de paises en Antártida: {antarctic}
    """)

def pais_mayor_y_menor_poblacion(lista): 
    # Iniciamos con el primer pais
    poblacion_min = int(lista[0]["poblacion"])
    pais_min = lista[0]["pais"]

    poblacion_max = int(lista[0]["poblacion"])
    pais_max = lista[0]["pais"]

    # Recorremos toda la lista
    for pais in lista[1:]:
        poblacion = int(pais["poblacion"])
        
        # Menor poblacion
        if poblacion < poblacion_min:
            poblacion_min = poblacion
            pais_min = pais["pais"]

        # Mayor poblacion
        if poblacion > poblacion_max:
            poblacion_max = poblacion
            pais_max = pais["pais"]

    # Mostramos los resultados
    print(f"Pais con menor poblacion: {pais_min} ({poblacion_min})")
    print(f"Pais con mayor poblacion: {pais_max} ({poblacion_max})")

def promedios(archivo, propiedad): 
    suma = 0

    # Recorremos cada elemento y sumamos las propiedades
    for objeto in archivo: 
        if propiedad in objeto: 
            suma += float(objeto[propiedad])

    promedio = round(suma / len(archivo), 2)

    print(f"promedio de {propiedad}: {promedio}")

def menu_estadisticas(archivo): 
    bandera = True
    while bandera:
        print("""
        --- Opciones de estadisticas (Opción 4) ---
        a) Pais con menor y mayor poblacion
        b) Promedio de poblacion
        c) Promedio de superficie
        d) Cantidad de paises por continente
        e) Volver al menú principal
        """)

        subopcion: str = input("Ingrese una subopción de estadistica: ").lower()
        
        if subopcion == "a":
            pais_mayor_y_menor_poblacion(archivo)
        elif subopcion == "b":
            promedios(archivo, "poblacion")
        elif subopcion == "c":
            promedios(archivo, "superficie")
        elif subopcion == "d":
            paises_por_continente(archivo)
        elif subopcion == "e": 
            bandera = False
        else:
            print(" Opción inválida. Intente de nuevo.")