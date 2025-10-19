from rich.console import Console
from rich.table import Table

console = Console()

def paginar(lista):
    inicio = 0
    pasos = 7
    while inicio < len(lista):
        fin = inicio + pasos
        pagina = lista[inicio:fin]
        
        # Crear tabla de esta página
        table = Table(title=f"Paises {inicio+1} - {min(fin, len(lista))}")
        table.add_column("Pais", style="cyan")
        table.add_column("Superficie", justify="right")
        table.add_column("Poblacion", justify="right")
        table.add_column("Continente")
        

        for pais in pagina:
            table.add_row(pais["pais"], str(pais["superficie"]), str(pais["poblacion"]), str(pais["continente"]))
        
        console.print(table)
        
        inicio += pasos
        
        if(inicio >= len(lista)):
            print("No hay mas paises")
            break
        
        continuar = input("Continuar? ")
        if continuar.lower() == "no":
            print("Terminamos")
            break


        