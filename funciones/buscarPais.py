from funciones.paginacionConsola import paginar

# Función para buscar países por nombre
def buscar(archivo):
    # Pide al usuario que ingrese el nombre del país y lo convierte a minúsculas
    valor_pais :str= input("Ingrese el nombre del pais: ").strip().lower()
    paises = []  # Lista para guardar los países que coincidan

    # Recorre todos los objetos del archivo
    for objeto in archivo: 
        # Si el nombre del país coincide exactamente o empieza con lo ingresado
        if(objeto["pais"].lower() == valor_pais or objeto["pais"].lower().startswith(valor_pais)): 
            paises.append(objeto)  # Lo agrega a la lista de resultados
        
    # Si no se encontró ningún país
    if not paises:
        print("No se encontró ningún país...")
    else:
        # Si hay resultados, los muestra usando la paginación
        paginar(paises)
