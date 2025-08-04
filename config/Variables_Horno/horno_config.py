# ================================
# PARÁMETROS FÍSICOS DEL SISTEMA
# ================================
#global flag, fig, ax, linea
#flag = True
#fig, ax, linea = None, None, None
#global flag_imagen, fig_imagen, ax_imagen
#flag_imagen = True
#fig_imagen, ax_imagen = None, None

T_AMB = 30.0           # Temperatura ambiente (°C)
T_SET = 1000.0         # Setpoint de temperatura (°C)  80
K = 0.22                 # Ganancia térmica (°C por unidad de control) (0.22)
TAU = 100              # Constante de tiempo del horno (s)  (3600.0)
DT = 0.1               # Paso de simulación (s)
tiempos = []
temperaturas = []
delta_T =0
