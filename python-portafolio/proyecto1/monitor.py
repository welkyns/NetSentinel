import subprocess
import json
import platform
from datetime import datetime

# dispositivos a monitorear (IPs o dominios)
dispositivos = [
    {"nombre": "Google DNS", "ip": "8.8.8.8"},
    {"nombre": "Gateway Local", "ip": "192.168.1.1"}, # Cambia según tu red
    {"nombre": "Servidor Web", "ip": "github.com"}
]

def verificar_latencia(host):
    # parámetro según el SO
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = ['ping', param, '1', host]
    
    try:
        resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if resultado.returncode == 0:
            # cual es la latencia básica
            return "Online"
        else:
            return "Offline"
    except Exception:
        return "Error"

def ejecutar_diagnostico():
    reporte = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "resultados": []
    }

    for disp in dispositivos:
        estado = verificar_latencia(disp["ip"])
        reporte["resultados"].append({
            "dispositivo": disp["nombre"],
            "ip": disp["ip"],
            "estado": estado
        })
    
    # save en archivo json
    with open('estado_red.json', 'w') as f:
        json.dump(reporte, f, indent=4)
    
    print(f"Diagnóstico completado. Reporte generado en 'estado_red.json'")

if __name__ == "__main__":
    ejecutar_diagnostico()