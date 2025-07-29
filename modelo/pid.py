import config.pid_config as var
import config.horno_config as var_horno
def calcular_pid(error, error_prev, integral):
    """Calcula la señal de control u(t) usando PID discreto."""
    integral += error * var_horno.DT
    derivada = (error - error_prev) / var_horno.DT
    u = var.KP * error + var.KI * integral + var.KD * derivada
    return max(0.00, min(1.0, u)), integral, error  # u limitado entre 0 y 1