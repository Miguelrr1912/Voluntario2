import matplotlib.pyplot as plt
import os

def leer_datos(nombre_archivo):
    x_vals = []
    y_vals = []
    with open(nombre_archivo, 'r') as f:
        for linea in f:
            partes = linea.strip().split(',')
            if len(partes) == 2:
                try:
                    x, y = map(float, partes)
                    x_vals.append(x)
                    y_vals.append(y)
                except ValueError:
                    continue  # Ignora líneas mal formateadas
    return x_vals, y_vals

# Archivos de entrada
archivos = [
    "C:/Users/User/Documents/Fisica_compu/Compu/Voluntario 2 (Pendulo doble)/Mapa_Poincare_phi_phip.txt",
    "C:/Users/User/Documents/Fisica_compu/Compu/Voluntario 2 (Pendulo doble)/Mapa_Poincare_thetha_phi.txt",
    "C:/Users/User/Documents/Fisica_compu/Compu/Voluntario 2 (Pendulo doble)/Mapa_Poincare_thethap_thetha.txt"
]

# Colores
colores = ['blue', 'red', 'green']

# Carpeta de salida
carpeta_salida = "C:/Users/User/Documents/Fisica_compu/Compu/Voluntario 2 (Pendulo doble)/Ploteos"

for i, archivo in enumerate(archivos):
    x, y = leer_datos(archivo)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, linestyle='none', marker='o',
             markersize=0.5, color=colores[i],
             label=f'Mapa Poincaré {i+1}')

    nombre_base = os.path.splitext(os.path.basename(archivo))[0]

    # Configurar títulos y etiquetas según el tipo
    if "phi_phip" in nombre_base:
        plt.title('Mapa de Poincaré φ - φ′')
        plt.xlabel(r'$\varphi$')
        plt.ylabel(r"$\varphi'$")
    elif "thetha_phi" in nombre_base:
        plt.title('Mapa de Poincaré θ - φ')
        plt.xlabel(r'$\theta$')
        plt.ylabel(r'$\varphi$')
    elif "thethap_thetha" in nombre_base:
        plt.title('Mapa de Poincaré θ′ - θ')
        plt.xlabel(r"$\theta'$")
        plt.ylabel(r'$\theta$')
    else:
        plt.title(f'Mapa de Poincaré {i+1}')
        plt.xlabel('Variable X')
        plt.ylabel('Variable Y')

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    carpeta_salida = "C:/Users/User/Documents/Fisica_compu/Compu/Voluntario 2 (Pendulo doble)/Ploteos"

    nombre_imagen = os.path.join(carpeta_salida, f"{nombre_base} E=1.png")
    plt.savefig(nombre_imagen, dpi=300)
    plt.close()

    print(f"Guardado: {nombre_imagen}")

print("¡Todos los mapas guardados con nombres y etiquetas personalizadas!")


 