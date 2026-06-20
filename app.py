from flask import Flask, render_template

app = Flask(__name__)

# Simulación de las tramas de coordenadas X e Y provenientes de la APK móvil
coordenadas_apk = [
    {"x": 0, "y": 1},
    {"x": 1, "y": 0},
    {"x": 1, "y": 2},
    {"x": 2, "y": 1},
    {"x": 2, "y": 3},
    {"x": 3, "y": 2}
]

def generar_matriz_procesada(puntos):
    # Inicializamos la matriz de 4x4 en cero
    matriz = [[0 for _ in range(4)] for _ in range(4)]
    
    # Mapeamos los impactos de las variables físicas recibidas
    for punto in puntos:
        x = punto["x"]
        y = punto["y"]
        if 0 <= x < 4 and 0 <= y < 4:
            matriz[x][y] = 1
            
    return matriz

@app.route('/')
def index():
    matriz_final = generar_matriz_procesada(coordenadas_apk)
    return render_template('index.html', matriz=matriz_final)

@app.route('/vista2')
def vista2():
    matriz_final = generar_matriz_procesada(coordenadas_apk)
    return render_template('vista2.html', matriz=matriz_final)

@app.route('/vista3')
def vista3():
    matriz_final = generar_matriz_procesada(coordenadas_apk)
    return render_template('vista3.html', matriz=matriz_final)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
