from rich.panel import Panel
from rich.console import Console, Group
from rich.text import Text
from rich.align import Align
import os

console = Console()

def mostrar_menu():
    terminal_width = os.get_terminal_size().columns
    width = min(terminal_width - 2, 78)  # Margen de seguridad

    titulo = Text(" SIMULADOR DE TEMPERATURA - MENÚ PRINCIPAL ", style="bold cyan")

    opciones = Group(
        Text("[1] Configurar PID"),
        Text("[2] Configurar Horno"),
        Text("[3] Ejecutar Sin Error Inducido En La Simulación ()Gráfica"),
        Text("[4] Ejecutar Simulación (consola) y gráfica PID"),
        Text("[5] Ejecutar Simulación (gráfica termica)"),
        Text("[6] Mostrar gráfica de tendencia"),
        Text("[7] Salir")
    )

    panel = Panel(
        opciones,
        title=titulo,
        border_style="bright_blue",
        padding=(1, 2),
        width=width
    )

    console.clear()
    console.print(panel)




    
