import config.horno_config as var
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import os

console = Console()

def pedir_valores_horno():
    os.system("cls" if os.name == "nt" else "clear")

    terminal_width = os.get_terminal_size().columns
    width = min(terminal_width - 4, 70)

    # Crear texto multilinea con estilo
    texto = Text()
    texto.append("T_AMB: Ingrese el valor de temperatura ambiente.\n", style="bold")
    texto.append("T_SET: Ingrese el valor de setpoint de temperatura (°C)\n", style="bold")
    texto.append("K: Ingrese el valor de la ganancia térmica (°C por unidad de control)\n", style="bold")
    texto.append("TAU: Ingrese la constante de tiempo del horno (s)\n", style="bold")
    texto.append("DT: Ingrese el paso de tiempo de simulación (s)\n", style="bold")

    panel = Panel(
        Align.left(texto),
        title=Text(" CONFIGURAR HORNO ", style="bold cyan"),
        border_style="blue",
        padding=(1, 2),
        width=width
    )

    console.print(Align.center(panel))

    try:
        var.T_AMB = float(Prompt.ask("[bold yellow]Temperatura ambiente (T_AMB)[/bold yellow]"))
        var.T_SET = float(Prompt.ask("[bold yellow]Setpoint de temperatura (T_SET)[/bold yellow]"))
        var.K = float(Prompt.ask("[bold yellow]Ganancia térmica (K)[/bold yellow]"))
        var.TAU = float(Prompt.ask("[bold yellow]Constante de tiempo (TAU)[/bold yellow]"))
        var.DT = float(Prompt.ask("[bold yellow]Paso de tiempo (DT)[/bold yellow]"))

        console.print(
            f"\n[bold green]✅ Parámetros del horno actualizados:[/bold green]\n"
            f"  T_AMB = {var.T_AMB}, T_SET = {var.T_SET}, K = {var.K}, TAU = {var.TAU}, DT = {var.DT}"
        )

    except ValueError:
        console.print("[bold red]❌ Error: solo se permiten números reales.[/bold red]")
