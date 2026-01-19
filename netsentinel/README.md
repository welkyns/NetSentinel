herramienta de diagnóstico de red desarrollada en **Python** y **Docker**.

### Características:
* **Monitoreo Híbrido:** utiliza ICMP (Ping) y TCP Sockets para verificar hosts disponibles.
* **Reportes Automatizados:** generacion de reportes en json para hacer más sencilla la integración con otras herramientas.
* **Contenerizado:** listo para desplegar en cualquier entorno Linux mediante Docker.

### Cómo ejecutar:
1. Construir imagen: `docker build -t net-scanner .`
2. Correr: `docker run --network host net-scanner`