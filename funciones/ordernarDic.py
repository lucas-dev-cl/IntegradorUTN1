# Modulo para ordenar el archivos
# Ordenar de manera ascendente por nombre
def ordenar_objetos(archivo, propiedad):
    for objeto in range(len(archivo) - 1): 
        for j in range(len(archivo) - objeto - 1): 
            if(archivo[j][propiedad] > archivo[j + 1][propiedad]): 
                aux = archivo[j]
                archivo[j] = archivo[j + 1]
                archivo[j + 1] = aux

    return archivo

def ordenar_objetos_desc(archivo, propiedad): 
    for objeto in range(len(archivo) - 1): 
        for j in range(len(archivo) - objeto - 1): 
            if(archivo[j][propiedad] < archivo[j + 1][propiedad]): 
                aux = archivo[j]
                archivo[j] = archivo[j + 1]
                archivo[j + 1] = aux

    return archivo

