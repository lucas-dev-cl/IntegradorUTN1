from rich.console import Console
from rich.table import Table
from funciones.paginacionConsola import paginar

def buscar(archivo):
    valor_pais :str= input("Ingrese el nombre del pais: ").strip().lower()
    paises = []

    for objeto in archivo: 
        if(objeto["pais"].lower() == valor_pais or objeto["pais"].lower().startswith(valor_pais)): 
            paises.append(objeto)            
        
    if not paises:
        print("No se encontró ningún país...")
    else:
        paginar(paises)