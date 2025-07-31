import matplotlib.pyplot as plt  # type: ignore
import time
from rich.live import Live  # type: ignore
import config.horno_config as var
from visualizacion.grafico_pid import configurar_grafica, actualizar_grafica
from visualizacion.imagen_termica import (
    configurar_imagen_termica,
    actualizar_imagen_termica
)
from modelo import pid, horno
from visualizacion.tabla_live import generar_tabla
import math
import random

# ================================
# VARIABLES GLOBALES
# ================================
flag = True
fig, ax, linea = None, None, None

flag_imagen = True
fig_imagen, ax_imagen = None, None

# ================================
# FUNCIÓN DE RUIDO
# ================================
def get_ruido(t):
    ruido = random.uniform(-0.5, 1.5)
    perturbacion = 10 * math.sin(0.05 * t)
    return perturbacion + ruido

# ================================
# CONTROL GRÁFICA PID
# ================================
def call_grafica_pid(tiempos, temperaturas):
    global flag, fig, ax, linea

    # Verificar si la figura fue cerrada al intentar usar el canvas
    try:
        if fig is not None:
            fig.canvas.get_renderer()  # fuerza verificación
    except Exception:
        fig, ax, linea = None, None, None
        flag = True
        print("📊 Gráfica PID cerrada manualmente.")

    # Crear figura si es necesario
    if flag:
        fig, ax, linea = configurar_grafica()
        flag = False

    # Actualizar solo si existe
    if fig is not None:
        actualizar_grafica(fig, ax, linea, tiempos, temperaturas)


# ================================
# CONTROL IMAGEN TÉRMICA
# ================================
def call_imagen_termica(T):
    global flag_imagen, fig_imagen, ax_imagen

    # Verificar si la figura fue cerrada manualmente
    try:
        if fig_imagen is not None:
            fig_imagen.canvas.get_renderer()  # lanza error si fue cerrada
    except Exception:
        fig_imagen, ax_imagen = None, None
        flag_imagen = True
        print("📷 Imagen térmica cerrada manualmente.")

    # Crear figura si es necesario
    if flag_imagen:
        fig_imagen, ax_imagen = configurar_imagen_termica()
        flag_imagen = False

    # Actualizar si figura aún existe
    if fig_imagen is not None:
        actualizar_imagen_termica(fig_imagen, ax_imagen, T)

# ================================
# BUCLE PRINCIPAL
# ================================
def simular():
    global flag, fig, ax, linea
    flag = True
    fig, ax, linea = None, None, None

    global flag_imagen, fig_imagen, ax_imagen
    flag_imagen = True
    fig_imagen, ax_imagen = None, None

    print("🔁 Iniciando simulación térmica con PID. Presiona Ctrl+C para detener.\n")

    T = var.T_AMB
    error_prev = 0.0
    integral = 0.0
    t = 0
    tiempos = []
    temperaturas = []

    try:
        with Live(screen=True,refresh_per_second=4) as live:
            while True:
                start_time = time.time()

                # ░▒▓ PID ▓▒░
                error = var.T_SET - T + get_ruido(t)
                u, integral, error_prev = pid.calcular_pid(error, error_prev, integral)
                
                T = horno.simular_horno(T, u)
                tiempos.append(t)
                temperaturas.append(T)

                # 🖥️ Consola Rich
                tabla = generar_tabla(t, T, var.T_SET, u, error)
                live.update(tabla)

                # 📉 Gráfica PID
                call_grafica_pid(tiempos, temperaturas)

                # 📷 Imagen térmica
                #call_imagen_termica(T)

                # ⏱️ Control de tiempo
                t += 1
                elapsed = time.time() - start_time
                time.sleep(max(0.0, var.DT - elapsed))

    except KeyboardInterrupt:
        print("\n🛑 Simulación detenida por el usuario.")
        plt.ioff()
        plt.show()
