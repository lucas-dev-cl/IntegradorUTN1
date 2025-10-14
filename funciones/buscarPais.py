def buscar(archivo):
    valor_pais :str= input("Ingrese el nombre del pais: ").strip()
    encontrado: bool = False

    for objeto in archivo: 
        if(objeto["nombre"] == valor_pais.capitalize() or objeto["nombre"].startswith(valor_pais.capitalize())): 
            print(objeto)
            encontrado = True
    
    if not encontrado: 
        print("No se encotro ningun pais...")
 