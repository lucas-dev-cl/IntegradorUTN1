# precios = {
#     "banana": 2.0,
#     "naranja": 4.0,
#     "manzana": 3.5
# }

# precios2 = [
#     {"banana": 2.0},
#     {"manzanas": 3.0}
# ]

# precios["mango"] = 1000
# precios["sandia"] = 9090

# for fruta in precios2: 
#     for clave in fruta.keys(): 
#         print(clave)

# print(precios2[0]["banana"])

# while True: 

#     a = 0
#     b = 10

#     for i in range(a, b): 
#         print(i)

#     continuar = input("continuar?")

#     if(continuar == "no"):
#         print("terminamos")
#         break
    
#     a += 10
#     b += 10

# inicio = 0
# pasos = 3

# while inicio < 10: 
#     print(inicio)
#     inicio += 5

# paises = ["Colombia", "Argentina", "Brasil", "Chile", "Perú", "México", "Uruguay", "Paraguay", "Bolivia", "Ecuador"]

# paso = 3
# inicio = 0

# while inicio < len(paises):
#     fin = inicio + paso
#     print(paises[inicio:fin])
    
#     continuar = input("Continuar? (sí/no): ").lower()
#     if continuar == "no":
#         break
    
#     inicio += paso

# while inicio <= 10: 
#     inicio += 1
#     print(inicio)

import requests

def getCountries(): 
    try: 
        response = requests.get("https://restcountries.com/v3.1/all?fields=name,population,area,region")
        
        # Verificamos el estatus de la request
        if response.status_code != 200:
            print(f"Error HTTP {response.status_code}")
            return
        
        # Guardamos la lista de diccionarios
        paisesJson = response.json()
        inicio = 0
        pasos = 10
        listaDePaises = []  # 🔹 Movido fuera del while

        while inicio < len(paisesJson): 
            fin = inicio + pasos
            paises = paisesJson[inicio:fin]

            for pais in paises:
                paisDic = {
                    "nombre": pais["name"]["common"],
                    "poblacion": pais["population"],
                    "area": pais["area"],
                    "continente": pais["region"]
                }
                print(paisDic)
                listaDePaises.append(paisDic)

            continuar = input("Continuar? ")

            if continuar.lower() == "no": 
                print("Terminamos")
                break
            
            inicio += pasos

        return listaDePaises  # 🔹 Devuelve todo al final

    except Exception as e:
        print("Error:", e)

print(getCountries())
