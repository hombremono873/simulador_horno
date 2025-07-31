'''from rich.table import Table
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
    return Align.center(tabla)'''

    # generar_tabla.py (o donde quieras colocarlo)
# generar_tabla.py (o donde quieras colocarlo)

# tabla_estado.py
# tabla_estado.py
from rich.console import Console, Group
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

console = Console()

def generar_tabla(t, T, T_set, u, error):
    """Genera un panel con una tabla centrada y un mensaje inferior."""
    tabla = Table(expand=True)
    
    tabla.add_column("Tiempo (s)", justify="right")
    tabla.add_column("Temperatura (°C)", justify="right")
    tabla.add_column("Setpoint (°C)", justify="right")
    tabla.add_column("u(t)", justify="right")
    tabla.add_column("Error", justify="right")

    tabla.add_row(
        str(t),
        f"{T:.2f}",
        f"{T_set:.2f}",
        f"{u:.3f}",
        f"{error:.2f}"
    )

    # Mensaje inferior dentro del panel
    mensaje = Text("🔴 Para parar, cierra la ventana de la gráfica antes de presionar Ctrl+C", style="bold red")
    grupo = Group(
        Align.center(tabla),
        Align.center(mensaje)
    )

    ancho_terminal = console.size.width
    ancho_deseado = max(40, int(ancho_terminal * 0.9))

    return Panel(
        grupo,
        title="[italic cyan]Simulación Térmica del Horno (Modo Consola)[/italic cyan]",
        width=ancho_deseado,
        padding=(1, 2),
        border_style="bright_blue"
    )


    

