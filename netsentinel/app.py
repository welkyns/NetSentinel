from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def scan_ip(ip):
    results = []
    # Escanearemos solo los más comunes para que sea rápido
    ports = [22, 80, 443, 3306]
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            is_open = s.connect_ex((ip, port)) == 0
            results.append({"port": port, "status": "Abierto" if is_open else "Cerrado"})
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    scan_results = None
    target_ip = ""
    if request.method == 'POST':
        target_ip = request.form.get('ip')
        scan_results = scan_ip(target_ip)
    return f'''
        <h1>NetSentinel Dashboard</h1>
        <form method="post">
            IP a escanear: <input type="text" name="ip" value="{target_ip}">
            <input type="submit" value="Escanear">
        </form>
        {f"<h3>Resultados para {target_ip}:</h3><ul>" + "".join([f"<li>Puerto {r['port']}: {r['status']}</li>" for r in scan_results]) + "</ul>" if scan_results else ""}
    '''

if __name__ == '__main__':
    # '0.0.0.0' abre la escucha a TODAS las interfaces de red
    app.run(host='0.0.0.0', port=5000)