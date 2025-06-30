import matplotlib.pyplot as plt

# Leer los datos desde un archivo
def leer_datos(nombre_archivo):
    x_vals = []
    y_vals = []
    with open(nombre_archivo, 'r') as f:
        for linea in f:
            partes = linea.strip().split(',')
            if len(partes) == 2:
                x, y = map(float, partes)
                x_vals.append(x)
                y_vals.append(y)
    return x_vals, y_vals

# Ruta del archivo
archivo = "C:/Users/User/Documents/Fisica_compu/Compu/Voluntario 2 (Pendulo doble)/Mapa_Poincare_thetha_phi.txt"

# Leer e imprimir
x, y = leer_datos(archivo)

# Graficar
plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Datos', linewidth=0.01, markersize=0.5)
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Gráfico de datos')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
