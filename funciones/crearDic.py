import csv
# Leemos el archivo csv y lo creamos en un diccionario
# Retorna la lista de objetos, por lo tanto para usarla tenemos que asignarla a una variable o si queremos ver solamente datos, printear 
def csvAdic(ruta): 
    try:
        with open(ruta, "r", encoding="utf-8") as file:
            lector = csv.DictReader(file)
            datos = list(lector)
        return datos
    
    except FileNotFoundError:
        print(f"No se encontro el archivo en la ruta especificada: {ruta}")
    except Exception as e:
        print(f"Ocurrio un error al leer el archivo: {e}")
        
