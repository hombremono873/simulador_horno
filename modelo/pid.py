import config.Variables_Horno.horno_config as var_horno
import config.Variables_Pid.pid_config as var
import utils.funciones_auxiliares.calculo_windout as windout
def calcular_pid(error, error_prev, integral):
    """Calcula la señal de control u(t) usando PID discreto."""
    integral += error * var_horno.DT
    derivada = (error - error_prev) / var_horno.DT
    integral = windout.minimizar_integral(integral)
    u = var.KP * error + var.KI * integral + var.KD * derivada
    return max(0.00, min(1.0, u)), integral, error  # u limitado entre 0 y 1