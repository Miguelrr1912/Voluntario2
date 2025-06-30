import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros
L1 = L2 = 1  # Longitudes

# Cargar datos
df = pd.read_csv("C:/Users/User/Documents/Fisica_compu/Compu/Voluntario 2 (Pendulo doble)/Pendulo_doble.txt", header=None)
theta1 = df[0].values
theta2 = df[1].values

# Posiciones
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# Fig y ejes
fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-', lw=2, label="péndulo")
trace1, = ax.plot([], [], 'r-', lw=0.5, label="trayectoria 1")
trace2, = ax.plot([], [], 'b-', lw=0.5, label="trayectoria 2")

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid()
ax.legend()

# Listas para las trayectorias
trail_x1, trail_y1 = [], []
trail_x2, trail_y2 = [], []

def init():
    line.set_data([], [])
    trace1.set_data([], [])
    trace2.set_data([], [])
    return line, trace1, trace2

def update(i):
    # Puntos actuales
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)
    
    # Acumular trayectorias
    trail_x1.append(x1[i])
    trail_y1.append(y1[i])
    trail_x2.append(x2[i])
    trail_y2.append(y2[i])
    
    trace1.set_data(trail_x1, trail_y1)
    trace2.set_data(trail_x2, trail_y2)
    
    return line, trace1, trace2

ani = animation.FuncAnimation(fig, update, frames=len(x1),
                              init_func=init, blit=True, interval=0.1)

plt.show()
