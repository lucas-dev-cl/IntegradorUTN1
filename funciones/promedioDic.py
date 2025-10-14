def promedioDic(archivo): 
    suma = 0

    # Recorremos cada elemento y sumamos las propiedades
    for objeto in archivo: 
        suma += int(objeto["superficie"])

    promedio = round(suma / len(archivo), 2)

    return promedio