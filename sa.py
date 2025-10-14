precios = {
    "banana": 2.0,
    "naranja": 4.0,
    "manzana": 3.5
}

precios2 = [
    {"banana": 2.0},
    {"manzanas": 3.0}
]

precios["mango"] = 1000
precios["sandia"] = 9090

for fruta in precios2: 
    for clave in fruta.keys(): 
        print(clave)

print(precios2[0]["banana"])