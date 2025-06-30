import matplotlib.pyplot as plt

def leer_lyapunov_y_graficar(nombre_archivo, paso_tiempo=0.05):
    try:
        # Leer los coeficientes del archivo
        with open(nombre_archivo, 'r') as archivo:
            valores = [float(linea.strip()) for linea in archivo if linea.strip()]
        
        if not valores:
            print("El archivo está vacío o no contiene valores numéricos válidos.")
            return

        # Crear el eje de tiempo
        tiempos = [i * paso_tiempo for i in range(len(valores))]

        # Graficar
        plt.figure(figsize=(10, 5))
        plt.plot(tiempos, valores, label='Coef. de Lyapunov', linewidth=1.2)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Coeficiente de Lyapunov')
        plt.title('Evolución del coeficiente de Lyapunov')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        # Guardar la imagen
        plt.savefig("lyapunov_plot.png")
        plt.show()

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

# Llamada a la función
leer_lyapunov_y_graficar('C:/Users/User/Documents/Fisica_compu/Compu/Voluntario 2 (Pendulo doble)/Lyupanov.txt')
#holi