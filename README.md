Link del video explicando el codigo: https://youtu.be/WKo0ZeQQMiM

Descripción del Programa

Este programa permite gestionar y analizar información de países a partir de un archivo CSV (paises_dataset.csv), el cual fue generado utilizando datos obtenidos de la API pública REST Countries.
Convierte los datos en objetos tipo diccionario y proporciona varias funcionalidades, como búsqueda, filtrado, ordenamiento y estadísticas.

El programa está organizado con módulos separados, cada uno con una responsabilidad clara:

    1. crearDic.csvAdic: Convierte el CSV en una lista de diccionarios.

    2. buscarPais.buscar: Permite buscar un país por nombre, con coincidencia exacta o parcial.

    3. filtrarPaises.menu_filtrar_paises: Filtra países por continente, rango de población o rango de superficie.

    4. ordernarDic.menu_ordenar: Ordena la lista de países por nombre, población o superficie (ascendente/descendente).

    5. mostrarEstadisticas.menu_estadisticas: Calcula estadísticas, como país con mayor o menor población, promedio de población, promedio de superficie y cantidad de países por continente

Instrucciones de Uso

Ejecutar el programa:
python main.py
(Asegurarse de que paises_dataset.csv esté en la carpeta correcta y los módulos estén disponibles.)

Menú de Opciones:
Al iniciar, se mostrará un menú numerado con opciones:

1. Buscar un país por nombre
2. Filtrar países
3. Ordenar países
4. Mostrar estadísticas
0. Salir

Usar cada opción:
1: Buscar un país: Ingresa el nombre completo o una parte del nombre para obtener coincidencias.

2: Filtrar países
    a. Por continente
    b. Por rango de población
    c. Por rango de superficie

El programa te pedirá los criterios de filtrado y mostrará los resultados.

3: Ordenar países
    a. Por nombre
    b. Por población
    c. Por superficie

Podés elegir ascendente o descendente según el caso.

4: Mostrar estadísticas
    a. País con mayor y menor población
    b. Promedio de población
    c. Promedio de superficie
    d. Cantidad de países por continente

Los resultados se muestran en pantalla.

0: Salir:  Finaliza el programa.

Validaciones: Si ingresás un número fuera del rango (0–4), el programa mostrará “Opción inválida” y volverá al menú.

Ejemplos: 

Ejemplo 1: Buscar un país por nombre
El usuario selecciona la opción para buscar un país e ingresa “arg” como texto de búsqueda.
El programa muestra todos los países cuyo nombre contiene esa palabra.
Salida esperada: Argentina.

Ejemplo 2: Filtrar países por continente
El usuario elige la opción de filtrar y selecciona el criterio “continente”.
Luego ingresa “Europe” como valor.
El programa muestra una lista con todos los países pertenecientes a ese continente.
Salida esperada: una lista con países como Francia, Alemania, España, Italia, entre otros.

Ejemplo 3: Ordenar países por superficie (descendente)
El usuario elige la opción para ordenar, selecciona el criterio “superficie” y el orden “descendente”.
El programa muestra los países desde el más grande al más pequeño.
Salida esperada:
Rusia, Canadá, China, Estados Unidos, Brasil, entre otros.

Ejemplo 3: Mostrar estadísticas
El usuario selecciona la opción para ver la cantidad de países por continente.
El programa analiza los datos y cuenta cuántos países pertenecen a cada continente, mostrando los resultados de manera ordenada.

Salida esperada:

África: 54 países
América: 35 países
Asia: 49 países
Europa: 44 países
Oceanía: 14 países
Antártida: 5 país (dependiendo de la fuente de datos)

Ejemplo 5: Salir del programa
El usuario selecciona la opción “0” en el menú.
El programa finaliza la ejecución mostrando un mensaje de cierre.
Salida esperada: “Terminamos”.

Participación de los integrantes: 

El desarrollo del proyecto fue realizado de manera colaborativa entre Haise y Tina, distribuyendo las tareas de forma equilibrada para cubrir todas las funcionalidades del programa.

Lucas Gallardo se encargó de:

- Implementar el módulo de ordenamiento, permitiendo organizar los países por nombre, población o superficie en orden ascendente o descendente.

- Desarrollar el buscador de países, con soporte para coincidencias parciales o exactas.

- Crear dos de las funciones del módulo de estadísticas, enfocadas en el cálculo de promedios y la detección del país con mayor y menor población.

- Diseñar el sistema de paginado y visualización en tablas dentro de la consola, mejorando la presentación de los resultados.

Shirley Torres se encargó de:

- Desarrollar todas las funciones de filtrado, incluyendo los filtros por continente, rango de población y rango de superficie.

- Implementar dos funciones adicionales del módulo de estadísticas, relacionadas con el conteo de países por continente y otros cálculos complementarios.
 
- Encargarse de la realización de la request a la API, asegurando la correcta obtención y formato de los datos utilizados en el programa.

- Generar el archivo paises_dataset.csv a partir de la información obtenida de la API REST Countries.