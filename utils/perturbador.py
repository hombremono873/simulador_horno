# perturbador.py
import math
import random

# Esta función genera un impulso térmico si se activa aleatoriamente.
# Mantiene el estado de inicio y duración del impulso sin depender del exterior.
# Parámetros:
# - t: tiempo actual
# - probabilidad: chance de que el impulso ocurra en este instante (valor entre 0 y 1)
# - duracion: duración del impulso si se activa (en segundos)
# - magnitud: valor del impulso (ej: -40 para simular una caída abrupta)
# Devuelve:
# - valor del impulso (float): 0 o magnitud
# - estado del impulso (bool): True si está activo, False si no

def impulso_probabilistico(t, probabilidad, duracion, magnitud):
    if not hasattr(impulso_probabilistico, "activo"):
        impulso_probabilistico.activo = False
        impulso_probabilistico.t_inicio = 0

    if impulso_probabilistico.activo:
        if t < impulso_probabilistico.t_inicio + duracion:
            return magnitud, True
        else:
            impulso_probabilistico.activo = False
            return 0, False

    from random import random
    if random() < probabilidad:
        impulso_probabilistico.activo = True
        impulso_probabilistico.t_inicio = t
        return magnitud, True

    return 0, False


# Esta función devuelve la perturbación total del sistema en un instante t.
# Incluye:
# - ruido aleatorio
# - perturbación senoidal suave
# - impulso térmico probabilístico
# Parámetros:
# - t: tiempo actual
# - probabilidad: probabilidad de impulso
# - duracion: duración del impulso si se activa
# - magnitud: valor del impulso si ocurre
# Retorna:
# - suma de todas las perturbaciones (float)
# - estado del impulso (bool)

def perturbacion_total(t, probabilidad=0.05, duracion=3, magnitud=-40):
    from random import uniform
    from math import sin

    ruido = uniform(-0.5, 1.5)
    senoide = 10 * sin(0.05 * t)
    impulso, activo = impulso_probabilistico(t, probabilidad, duracion, magnitud)

    total = ruido + senoide + impulso
    return total, activo
# ================================
# FUNCIÓN DE RUIDO  leve
# ================================
def get_ruido(t):
    ruido = random.uniform(-0.5, 1.5)
    perturbacion = 10 * math.sin(0.05 * t)
    return perturbacion + ruido