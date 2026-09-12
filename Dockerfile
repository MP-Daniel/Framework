# Usa una imagen oficial de Python
FROM python:3.11-slim

# Configura las variables de entorno de Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del proyecto
COPY . /app/

# Expone el puerto 8000
EXPOSE 8000

# Comando por defecto para correr la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
