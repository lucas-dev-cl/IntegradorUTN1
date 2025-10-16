# Leemos el archivo csv y lo creamos en un diccionario
# Retorna la lista de objetos, por lo tanto para usarla tenemos que asignarla a una variable o si queremos ver solamente datos, printear 
def csvAdic(ruta): 
    with open(ruta, "w", encoding="utf-8") as file:
        # Leemos el archivo y lo hacemos una lista separado por sus salto de lineas
        contenido: list = file.read().split("\n")

    datos :list = []
    nombre_columnas = contenido[0]
    lista_nombre_columnas = nombre_columnas.split(",")

    # Bucle para leer cada elemento de la lista, saltandonos el primero que van a ser los nombres de las columnas
    for i in range(1, len(contenido)): 
        # Si el contenido no esta vacio entonces dividimos el contenido por comas
        if(contenido[i] != ""): 
            elemento = contenido[i].split(",") 
            objeto = {}
            
            # Ingresamos clave y valor al objeto
            for j in range(len(elemento)):
                objeto[lista_nombre_columnas[j]] = elemento[j]    
            
            datos.append(objeto)
    
    return datos
