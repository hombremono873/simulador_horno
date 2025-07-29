import matplotlib                    #Se anexa en este lugar para lograr que el programa main.exe ejecute la instancia
matplotlib.use('TkAgg')              #Lo mismo que anterior
import matplotlib.pyplot as plt
import config.horno_config as var

def actualizar_grafica(fig, ax, linea, tiempos, temperaturas):
    """Actualiza el gráfico en cada iteración."""
    linea.set_data(tiempos, temperaturas)
    ax.set_xlim(0, max(60, tiempos[-1] + 1))
    #ax.set_xlim(max(0, tiempos[-1] - 60), tiempos[-1] + 5)

    ax.set_ylim(var.T_AMB, var.T_SET + 0.5*var.T_SET )
    fig.canvas.draw()
    fig.canvas.flush_events()
    
def configurar_grafica():
    """Configura el gráfico para mostrar la temperatura en tiempo real."""
    plt.ion()
    fig, ax = plt.subplots()
    linea, = ax.plot([], [], label="Temperatura", color='blue')
    ax.axhline(var.T_SET, color='red', linestyle='--', label='Setpoint')
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Temperatura (°C)")
    ax.set_title("Respuesta del Horno con Control PID")
    ax.grid(True)
    ax.legend()
    return fig, ax, linea