import socket
import sys # Importamos sys para leer argumentos

def scan_common_ports(ip):
    common_ports = [21, 22, 80, 443, 3306, 8080]
    print(f"Escaneando servicios en {ip}...")
    # ... (resto de tu código igual)

if __name__ == "__main__":
    # Verificamos si pasaste una IP como argumento
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        # Si no hay argumento, pedimos input (opcional)
        target = input("Ingresa la IP a escanear: ")
    
    scan_common_ports(target)