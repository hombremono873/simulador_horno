import config.horno_config as var

def simular_horno(T_actual, u):
    """Simula la evolución térmica del horno (modelo de 1er orden)."""
    dT = (1 / var.TAU) * (var.T_AMB - T_actual) + var.K * u
    return T_actual + var.DT * dT