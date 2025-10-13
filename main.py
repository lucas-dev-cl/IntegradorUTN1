from funciones.crearDic import csvAdic
from funciones.ordernarDic import ordenar_objetos
from funciones.ordernarDic import ordenar_objetos_desc

if(__name__ == "__main__"): 
    lista_objetos = csvAdic("paises_dataset.csv")

    ordenar_poblacion = ordenar_objetos_desc(lista_objetos, "poblacion")

    for i in ordenar_poblacion: 
        print(i)
