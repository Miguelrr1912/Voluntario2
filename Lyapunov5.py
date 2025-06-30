import matplotlib.pyplot as plt

energias = [1, 3, 5, 10, 15]


def leer_lyapunov_bloques(nombre_archivo):
    bloques = []
    bloque = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                if bloque:  # Si ya hay datos, guarda bloque y empieza uno nuevo
                    bloques.append(bloque)
                    bloque = []
                continue
            try:
                valor = float(linea)
                bloque.append(valor)
            except ValueError:
                continue
    if bloque:  # Añadir el último bloque si existe
        bloques.append(bloque)
    return bloques

def graficar_lyapunov_bloques(nombre_archivo, paso_tiempo=0.05):
    try:
        bloques = leer_lyapunov_bloques(nombre_archivo)

        if not bloques:
            print("No se encontraron datos.")
            return

        colores = ['blue', 'red', 'green', 'orange', 'purple']

        plt.figure(figsize=(10, 6))

        for i, bloque in enumerate(bloques):
            tiempos = [j * paso_tiempo for j in range(len(bloque))]
            plt.plot(tiempos, bloque, label=f'Energía = {energias[i]}',
         color=colores[i % len(colores)], linewidth=1.2)

        plt.xlabel('Tiempo (s)')
        plt.ylabel('Coeficiente de Lyapunov')
        plt.title('Evolución del coeficiente de Lyapunov')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
       
        plt.savefig("C:/Users/User/Documents/Fisica_compu/Compu/Voluntario 2 (Pendulo doble)/Ploteos/lyapunov_plot_multiE.png")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

# Llamada
graficar_lyapunov_bloques(
    'C:/Users/User/Documents/Fisica_compu/Compu/Voluntario 2 (Pendulo doble)/Lyupanov.txt'
)
