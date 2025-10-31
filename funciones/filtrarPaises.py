from funciones.paginacionConsola import paginar
import re # Usamos 're' para limpiar los continentes en el filtro
# Importacion para darle color y estilo a algunos textos
from colorama import Fore, Style,init

init()

def filtrar_por_continente(lista_paises: list):
    # """
    # Filtra la lista de países por un continente específico ingresado por el usuario.
    # Muestra los resultados paginados.
    # """
    
    # 1. Obtener y mostrar continentes disponibles (limpiando posibles espacios o caracteres)
    continentes_unicos = set()
    for pais in lista_paises:
        # Usamos re.sub para eliminar cualquier caracter no alfanumérico que cause problemas
        continente = re.sub(r'\s+', ' ', pais.get('continente', 'Desconocido')).strip()
        if continente:
            continentes_unicos.add(continente)
            
    continentes_disponibles = sorted(list(continentes_unicos))
    
    print(f"\n{Fore.YELLOW}--- Continentes Disponibles ---{Style.RESET_ALL}")
    for i, cont in enumerate(continentes_disponibles):
        print(f"  - {cont}")
    print("-----------------------------\n")

    continente_a_buscar = input("Ingrese el nombre del continente a filtrar: ").strip().lower()

    if not continente_a_buscar:
        print(f"{Fore.RED} El continente no puede estar vacío.")
        return

    resultados = []
    for pais in lista_paises:
        nombre_continente = pais.get('continente', '').strip().lower()
        if nombre_continente == continente_a_buscar or nombre_continente.startswith(continente_a_buscar):
            resultados.append(pais)
    
    if not resultados:
        print(f" No se encontraron países en el continente '{continente_a_buscar.capitalize()}'.")
    else:
        print(f"\n Resultados del filtro por continente ('{continente_a_buscar.capitalize()}'):")
        paginar(resultados)


def filtrar_por_rango_poblacion(lista_paises: list):
    """
    Filtra la lista de países por un rango de población (mínimo y máximo).
    Muestra los resultados paginados.
    """
    print(f"\n{Fore.YELLOW}--- Filtro por Rango de Población ---{Style.RESET_ALL}")
    try:
        pob_min_str = input("Ingrese la población mínima (ej: 1000000): ").strip()
        pob_max_str = input("Ingrese la población máxima (ej: 100000000): ").strip()
        
        # Validación y conversión a INT (necesaria porque los datos están en string en el dict)
        pob_min = int(pob_min_str)
        pob_max = int(pob_max_str)
        
    except ValueError:
        print(f"{Fore.RED}Error: Por favor, ingrese solo números enteros para la población.")
        return

    if pob_min > pob_max or pob_min < 0 or pob_max < 0:
        print(f"{Fore.RED}Error: El rango no es válido (mínimo debe ser <= máximo, y ambos deben ser positivos).")
        return

    resultados = []
    for pais in lista_paises:
        try:
            poblacion_valor = int(pais.get('poblacion', '0')) # Convertimos a int para comparar
            if pob_min <= poblacion_valor <= pob_max:
                resultados.append(pais)
        except ValueError:
            # Ignoramos países con datos de población inválidos
            continue
    
    if not resultados:
        print("No se encontraron países en ese rango de población.")
    else:
        print(f"\n Resultados del filtro por rango de población ({pob_min:,} - {pob_max:,}):")
        paginar(resultados)


def filtrar_por_rango_superficie(lista_paises: list):
    """
    Filtra la lista de países por un rango de superficie (mínimo y máximo).
    Muestra los resultados paginados.
    """
    print(f"\n{Fore.YELLOW}--- Filtro por Rango de Superficie (km²) ---{Style.RESET_ALL}")
    try:
        sup_min_str = input("Ingrese la superficie mínima (km²): ").strip()
        sup_max_str = input("Ingrese la superficie máxima (km²): ").strip()
        
        # Validación y conversión a INT
        sup_min = int(sup_min_str)
        sup_max = int(sup_max_str)
        
    except ValueError:
        print(f"{Fore.RED} Error: Por favor, ingrese solo números enteros para la superficie.")
        return

    if sup_min > sup_max or sup_min < 0 or sup_max < 0:
        print(f"{Fore.RED} Error: El rango no es válido (mínimo debe ser <= máximo, y ambos deben ser positivos).")
        return

    resultados = []
    for pais in lista_paises:
        try:
            superficie_valor = int(pais.get('superficie', '0')) # Convertimos a int para comparar
            if sup_min <= superficie_valor <= sup_max:
                resultados.append(pais)
        except ValueError:
            # Ignoramos países con datos de superficie inválidos
            continue
    
    if not resultados:
        print(" No se encontraron países en ese rango de superficie.")
    else:
        print(f"\n Resultados del filtro por rango de superficie ({sup_min:,} - {sup_max:,}):")
        paginar(resultados)


def menu_filtrar_paises(lista_paises: list):
    # """Maneja el submenú de filtrado de países (Opción 2)."""
    bandera = True
    while bandera:
        print(f"""
        {Fore.YELLOW}--- Opciones de filtrado (Opción 2) --- {Style.RESET_ALL}
        a) Continente
        b) Rango de población
        c) Rango de superficie
        d) Volver al menú principal
        """)
        
        subopcion: str = input("Ingrese una subopción de filtrado: ").lower()
        
        if subopcion == "a":
            filtrar_por_continente(lista_paises)
        elif subopcion == "b":
            filtrar_por_rango_poblacion(lista_paises)
        elif subopcion == "c":
            filtrar_por_rango_superficie(lista_paises)
        elif subopcion == "d":
            bandera = False
        else:
            print(f"{Fore.RED} Opción inválida. Intente de nuevo.")