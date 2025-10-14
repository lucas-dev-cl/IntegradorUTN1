def paises_por_continente(archivo): 
    america = 0
    asia = 0
    europa = 0
    oceania = 0

    for objeto in archivo: 
        if(objeto["continente"] == "America"): 
            america += 1
        elif(objeto["continente"] == "Asia"): 
            asia += 1
        elif(objeto["continente"] == "Europa"): 
            europa += 1
        elif(objeto["continente"] == "Oceania"): 
            oceania += 1

    print(f"""
        Cantidad de paises en America: {america}
        Cantidad de paises en Asia: {asia}
        Cantidad de paises en Europa: {europa}
        Cantidad de paises en Oceania: {oceania}
    """)