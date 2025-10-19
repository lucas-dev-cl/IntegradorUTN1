from funciones.paginacionConsola import paginar 

# Modulo para ordenar el archivos
# Ordenar de manera ascendente por nombre
def ordenar_objetos(archivo, propiedad):
    lista_ordenada = archivo.copy()

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
    

def ordenar_objetos_desc(archivo, propiedad): 
    lista_ordenada = archivo.copy()

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