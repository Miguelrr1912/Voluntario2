import matplotlib.pyplot as plt

def leer_lyapunov_bloques(nombre_archivo):
    bloques = []
    condiciones = []
    bloque = []
    esperando_coeficientes = False

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()

            if not linea:
                # Fin de un bloque de coeficientes
                if bloque:
                    bloques.append(bloque)
                    bloque = []
                esperando_coeficientes = False
                continue

            if ',' in linea:
                # Línea con condiciones iniciales
                cond = linea.split(',')
                thetha = float(cond[0].strip())
                phi = float(cond[1].strip())
                condiciones.append((thetha, phi))
                esperando_coeficientes = True
                continue

            if esperando_coeficientes:
                try:
                    valor = float(linea)
                    bloque.append(valor)
                except ValueError:
                    continue

    # Añadir el último bloque si existe
    if bloque:
        bloques.append(bloque)

    print(f"Condiciones encontradas: {condiciones}")
    print(f"Bloques encontrados: {len(bloques)}")

    return condiciones, bloques

def graficar_lyapunov_bloques(nombre_archivo, paso_tiempo=0.05):
    try:
        condiciones, bloques = leer_lyapunov_bloques(nombre_archivo)

        if not bloques:
            print("No se encontraron datos.")
            return

        colores = ['blue', 'red', 'green', 'orange', 'purple', 'cyan', 'magenta']

        plt.figure(figsize=(10, 6))

        for i, bloque in enumerate(bloques):
            tiempos = [j * paso_tiempo for j in range(len(bloque))]
            thetha, phi = condiciones[i]
            plt.plot(tiempos, bloque,
                     label=f'Theta={thetha:.3f}, Phi={phi:.3f}',
                     color=colores[i % len(colores)],
                     linewidth=1.5)

        plt.xlabel('Tiempo (s)')
        plt.ylabel('Coeficiente de Lyapunov')
        plt.title('Evolución del coeficiente de Lyapunov para diferentes condiciones iniciales')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        # Cambia la ruta a la que prefieras
        plt.savefig("C:/Users/User/Documents/Fisica_compu/Compu/Voluntario 2 (Pendulo doble)/Ploteos/lyapunov_plot_multiCond.png")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

# Llamada principal
graficar_lyapunov_bloques(
    'C:/Users/User/Documents/Fisica_compu/Compu/Voluntario 2 (Pendulo doble)/Lyupanov5condinicdif.txt'
)
