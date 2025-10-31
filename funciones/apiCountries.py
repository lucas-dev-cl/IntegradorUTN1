import requests

def getCountries(): 
    try: 
        response = requests.get("https://restcountries.com/v3.1/all?fields=name,population,area,region")
        
        # Verificamos el estatus de la request
        if(response.status_code != 200):
            print(f"Error HTTP {response.status_code}")
            return
        
        # Guardamos en una variable la lista de diccionarios
        paisesJson :list = response.json()
        listaDePaises :list = []

        # Pasamos por cada dic y printeamos propiedades especificas
        for pais in paisesJson:
            paisDic = {
                "nombre": pais["name"]["common"],
                "poblacion": pais["population"],
                "superficie": pais["area"],
                "continente": pais["region"]
            }

            listaDePaises.append(paisDic)

        return listaDePaises
    
    # Punto de acceso para acceder a los errores de la request
    except requests.exceptions.RequestException as e:
        print("Error en el servidor: ", e)          
    # Errores internos o de datos
    except Exception as e:
        print("Error general al procesar los datos:", e)
