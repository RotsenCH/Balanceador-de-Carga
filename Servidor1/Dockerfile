# Utiliza una imagen de Python como base
FROM python:3.9

# Establece el directorio de trabajo en la carpeta de la aplicación
WORKDIR /servidor1

# Copia el archivo de la aplicación y los requisitos al directorio de trabajo
COPY servidor1.py .

# Instala las dependencias necesarias
RUN pip install flask 

# Define el comando por defecto para ejecutar la aplicación
CMD [ "python", "servidor1.py" ]

EXPOSE 5001