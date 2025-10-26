import csv
import funciones.apiCountries as apiCountries

with open('paises_dataset.csv', "w", encoding="utf-8", newline='') as file: 
    writer = csv.writer(file)
    writer.writerow(["pais","poblacion","superficie","continente"])

    objetos = apiCountries.getCountries()
    
    for objeto in objetos:
        try:
            nombre = objeto.get('nombre', 'Desconocido').replace(',', ';')
            poblacion = int(objeto.get('poblacion', 0))
            superficie = float(objeto.get('superficie', 0))
            continente = objeto.get('continente', 'Desconocido')
            writer.writerow([nombre, poblacion, superficie, continente])
        except Exception as e:
            print("Error en objeto:", objeto, "Error:", e)
