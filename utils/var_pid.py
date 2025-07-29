import config.pid_config as var
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import os

console = Console()

def pedir_valores_pid():
    os.system("cls" if os.name == "nt" else "clear")

    terminal_width = os.get_terminal_size().columns
    width = min(terminal_width - 4, 70)

    panel = Panel(
        Align.left(Text(
            "\nIngrese los valores para configurar el controlador PID.\n"
            "\n- Kp: constante proporcional"
            "\n- Ki: constante integral"
            "\n- Kd: constante derivativa\n",
            style="bold"
        )),
        title=Text(" CONFIGURAR PID ", style="bold cyan"),
        border_style="blue",
        padding=(1, 2),
        width=width
    )

    console.print(Align.center(panel))

    try:
        var.KP = float(Prompt.ask("[bold yellow]Ingrese el valor de Kp[/bold yellow]"))
        var.KI = float(Prompt.ask("[bold yellow]Ingrese el valor de Ki[/bold yellow]"))
        var.KD = float(Prompt.ask("[bold yellow]Ingrese el valor de Kd[/bold yellow]"))

        console.print(f"\n[bold green]✅ PID actualizado: Kp={var.KP}, Ki={var.KI}, Kd={var.KD}[/bold green]")

    except ValueError:
        console.print("[bold red]❌ Error: solo se permiten números reales.[/bold red]")
