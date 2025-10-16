import apiCountries

with open('paises_dataset.csv', "w", encoding="utf-8") as file: 
    try:
        file.write("pais, poblacion, superficie, continente\n")
        objetos = apiCountries.getCountries()

        for objeto in objetos: 
            file.write(f"{objeto['nombre']},{objeto['poblacion']},{objeto['superficie']},{objeto['continente']}\n")
    
    except Exception as e:
        print("Ocurrio un error: ", e) 
