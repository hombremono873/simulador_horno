from rich.table import Table
from rich.align import Align
def generar_tabla(t, T, T_set, u, error):
    """Genera una tabla en consola para visualizar el estado actual."""
    tabla = Table(title="Simulación Térmica del Horno (Modo Consola)", style="bold blue")
    tabla.add_column("Tiempo (s)", justify="right")
    tabla.add_column("Temperatura (°C)", justify="right")
    tabla.add_column("Setpoint (°C)", justify="right")
    tabla.add_column("u(t)", justify="right")
    tabla.add_column("Error", justify="right")
    tabla.add_row(str(t), f"{T:.2f}", f"{T_set:.2f}", f"{u:.3f}", f"{error:.2f}")
    return Align.center(tabla)