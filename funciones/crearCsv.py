import csv
import funciones.apiCountries as apiCountries

# Abre (o crea) un archivo CSV para escribir datos de países
with open('paises_dataset.csv', "w", encoding="utf-8", newline='') as file: 
    writer = csv.writer(file)
    # Escribe la primera fila con los nombres de las columnas
    writer.writerow(["pais","poblacion","superficie","continente"])

    # Obtiene los datos de países desde la API
    objetos = apiCountries.getCountries()
    
    # Recorre cada país y escribe sus datos en el CSV
    for objeto in objetos:
        try:
            # Toma los valores de cada campo, con valores por defecto si no existen
            nombre = objeto.get('nombre', 'Desconocido').replace(',', ';')  # evita problemas con comas
            poblacion = int(objeto.get('poblacion', 0))
            superficie = float(objeto.get('superficie', 0))
            continente = objeto.get('continente', 'Desconocido')
            # Escribe la fila en el CSV
            writer.writerow([nombre, poblacion, superficie, continente])
        except Exception as e:
            # Muestra un mensaje si hay algún error con ese país
            print("Error en objeto:", objeto, "Error:", e)
