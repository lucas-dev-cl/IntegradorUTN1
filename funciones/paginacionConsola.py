# Importa herramientas para mostrar tablas bonitas en la consola
from rich.console import Console
from rich.table import Table

console = Console()

# Función para mostrar los países en páginas de 7 elementos
def paginar(lista):
    inicio = 0
    pasos = 7  # cantidad de elementos por página
    while inicio < len(lista):
        fin = inicio + pasos
        pagina = lista[inicio:fin]  # extrae la "página" actual

        # Crear tabla para la página
        table = Table(title=f"Paises {inicio+1} - {min(fin, len(lista))}")
        table.add_column("Pais", style="cyan")
        table.add_column("Superficie", justify="right")
        table.add_column("Poblacion", justify="right")
        table.add_column("Continente")
        
        # Agrega cada país de la página a la tabla
        for pais in pagina:
            table.add_row(pais["pais"], str(pais["superficie"]), str(pais["poblacion"]), str(pais["continente"]))
        
        # Muestra la tabla en consola
        console.print(table)
        
        # Avanza al siguiente grupo de países
        inicio += pasos

        # Si ya no hay más países, termina
        if(inicio >= len(lista)):
            print("No hay mas paises")
            break
        
        # Pregunta al usuario si quiere continuar a la siguiente página
        continuar = input("¿Siguiente pagina? (escriba 'no' o 'n' para salir): ").lower()
        if continuar == "no" or continuar == "n":
            print("Terminamos")
            break
