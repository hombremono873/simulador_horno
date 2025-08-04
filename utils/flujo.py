import matplotlib.pyplot as plt  # type: ignore
import time
from rich.live import Live  # type: ignore
import config.Variables_Horno.horno_config as vhorno
import config.Variables_Pid.pid_config as vpid

import visualizacion.imagen_termica as imag_horno
import visualizacion.grafico_pid as imag_pid
from modelo import pid, horno

from visualizacion.tabla_live import generar_tabla
import utils.perturbador as perturbador
import utils.funciones_auxiliares.alarma as func


# =============================================================================#
#                             BUCLE PRINCIPAL                                  #
# =============================================================================#
def simular():
    print("🔁 Iniciando simulación térmica con PID. Presiona Ctrl+C para detener.\n")
    T = vhorno.T_AMB
    t = 0
    try:
        with Live(screen=True,refresh_per_second=4) as live:
            while True:
                start_time = time.time()
                vhorno.delta_T, hay_impulso = perturbador.perturbacion_total(t, probabilidad=0.02, duracion=3, magnitud=80)
                func.alarma_impulso(hay_impulso)
                error = vhorno.T_SET - T + perturbador.get_ruido(t) + vhorno.delta_T
                u, vpid.integral, vpid.error_prev = pid.calcular_pid(error, vpid.error_prev, vpid.integral)
                
                T = horno.simular_horno(T, u)
                vhorno.tiempos.append(t)
                vhorno.temperaturas.append(T)
                
                tabla = generar_tabla(vpid.integral, T, vhorno.T_SET, u, error)
                live.update(tabla)

                imag_pid.call_grafica_pid(vhorno.tiempos, vhorno.temperaturas)
                imag_horno.call_imagen_termica(T)

                # Control de tiempo
                t += 1
                elapsed = time.time() - start_time
                time.sleep(max(0.0, vhorno.DT - elapsed))

    except KeyboardInterrupt:
        print("\n🛑 Simulación detenida por el usuario.")
        plt.ioff()
        plt.show()
