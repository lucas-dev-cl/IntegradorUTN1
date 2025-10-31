# Usamos una imagen base de Python ligera (slim)
FROM python:3.13.6-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /proyectoIntegrador1

# Copiamos solo el archivo de dependencias al contenedor
# Esto permite que Docker use la cache si no cambian las dependencias
COPY requirements.txt .

# Instalamos las dependencias de Python
# --no-cache-dir evita que pip guarde archivos temporales innecesarios
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el resto del proyecto al contenedor
# Esto incluye tu código fuente y otros archivos necesarios
COPY . .

# Comando que se ejecuta al iniciar el contenedor
# Aquí se ejecuta el script principal de tu proyecto
CMD ["python", "main.py"]
