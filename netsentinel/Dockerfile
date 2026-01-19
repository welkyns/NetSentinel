# 1. Imagen base de Python
FROM python:3.10-slim

# 2. Instalar dependencias del sistema (útil para herramientas de red)
RUN apt-get update && apt-get install -y net-tools iputils-ping && rm -rf /var/lib/apt/lists/*
RUN pip install flask
# 3. Directorio de trabajo
WORKDIR /app

# 4. Copiar tu script al contenedor
COPY port_scanner.py .

# 5. Comando por defecto (puedes pasar la IP como argumento después)
ENTRYPOINT ["python3", "port_scanner.py"]