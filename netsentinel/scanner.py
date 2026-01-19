import socket
import platform
import subprocess
import json
from datetime import datetime

class NetworkScanner:
    def __init__(self, targets):
        """
        :param targets: Lista de diccionarios con 'ip' y 'nombre'
        """
        self.targets = targets

    def ping_device(self, ip):
        """Verifica si un host responde a ICMP (Capa 3)"""
        # Ajustamos el parámetro según el SO
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", "-c", "1", "-W", "1", ip]
        
        try:
            # Ejecuta el comando sin mostrar la salida en consola
            resultado = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return resultado.returncode == 0
        except Exception as e:
            print(f"Error al ejecutar ping: {e}")
            return False

    def check_port(self, ip, port):
        """Verifica si un puerto específico está abierto (Capa 4 - TCP)"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.5) # Tiempo de espera corto
            result = s.connect_ex((ip, port))
            return result == 0

    def run_diagnostic(self):
        print(f"--- Iniciando Escaneo ---")
        resultados_log = [] 

        for device in self.targets:
            ip = device['ip']
            online = self.ping_device(ip)
            
            datos_dispositivo = {
                "nombre": device['nombre'],
                "ip": ip,
                "estado": "Online" if online else "Offline",
                "timestamp": datetime.now().isoformat()
            }
            resultados_log.append(datos_dispositivo)
            print(f"Verificado: {device['nombre']}")

        
        with open('reporte_red.json', 'w') as f:
            json.dump(resultados_log, f, indent=4)
        
        print(f"--- Reporte guardado en reporte_red.json ---")

# --- PRUEBA DEL SCRIPT ---
if __name__ == "__main__":
    mis_dispositivos = [
        {"nombre": "Google DNS", "ip": "8.8.8.8"},
        {"nombre": "Mi router", "ip": "172.28.128.1"},
        {"nombre": "youtube", "ip": "youtube.com"},
        {"nombre": "freesound", "ip": "freesound.org"},
        {"nombre": "Localhost", "ip": "127.0.0.1"}
    ]
    
    scanner = NetworkScanner(mis_dispositivos)
    scanner.run_diagnostic()