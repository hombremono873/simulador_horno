'''import config.horno_config as var
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


        
# input_horno.py

# utils/var_horno.py'''

'''import os
from rich.console import Console
from rich.prompt import Prompt
import config.horno_config as var

console = Console()

def pedir_valores_horno():
    os.system("cls" if os.name == "nt" else "clear")

    # Mostrar encabezado y descripción con líneas horizontales
    console.rule("[bold cyan]📋 CONFIGURACIÓN DEL HORNO[/bold cyan]")
    console.print("[bold]T_AMB :[/bold] Temperatura ambiente (°C)")
    console.print("[bold]T_SET :[/bold] Temperatura objetivo (°C)")
    console.print("[bold]K     :[/bold] Ganancia térmica (°C/u control)")
    console.print("[bold]TAU   :[/bold] Constante de tiempo (s)")
    console.print("[bold]DT    :[/bold] Paso de simulación (s)")
   

    try:
        var.T_AMB = float(Prompt.ask("[bold yellow]Temperatura ambiente (T_AMB)[/bold yellow]"))
        var.T_SET = float(Prompt.ask("[bold yellow]Setpoint de temperatura (T_SET)[/bold yellow]"))
        var.K     = float(Prompt.ask("[bold yellow]Ganancia térmica (K)[/bold yellow]"))
        var.TAU   = float(Prompt.ask("[bold yellow]Constante de tiempo (TAU)[/bold yellow]"))
        var.DT    = float(Prompt.ask("[bold yellow]Paso de tiempo (DT)[/bold yellow]"))

        console.print("\n[bold green]✅ Parámetros actualizados:[/bold green]")
        console.print(f"[cyan]  T_AMB = {var.T_AMB} °C[/cyan]")
        console.print(f"[cyan]  T_SET = {var.T_SET} °C[/cyan]")
        console.print(f"[cyan]  K     = {var.K} °C/u[/cyan]")
        console.print(f"[cyan]  TAU   = {var.TAU} s[/cyan]")
        console.print(f"[cyan]  DT    = {var.DT} s[/cyan]")
        console.rule()

    except ValueError:
        console.print("\n[bold red]❌ Error: solo se permiten números reales.[/bold red]")
'''

# utils/var_horno.py

import os
import time
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.live import Live
import config.horno_config as var

console = Console()

def pedir_valores_horno():
    os.system("cls" if os.name == "nt" else "clear")

    def construir_panel():
        ancho = max(40, int(console.size.width * 0.9))

        texto = Text()
        texto.append("📋 CONFIGURACIÓN DEL HORNO\n\n", style="bold cyan")
        texto.append("T_AMB : Temperatura ambiente (°C)\n", style="bold")
        texto.append("T_SET : Temperatura objetivo (°C)\n", style="bold")
        texto.append("K     : Ganancia térmica (°C/u control)\n", style="bold")
        texto.append("TAU   : Constante de tiempo (s)\n", style="bold")
        texto.append("DT    : Paso de simulación (s)\n\n", style="bold")
        texto.append("[bold red]↩ Presione ENTER para continuar...[/bold red]")
        

        return Panel(
            Align.left(texto),
            title="[bold cyan] CONFIGURAR HORNO [/bold cyan]",
            border_style="bright_blue",
            padding=(1, 2),
            width=ancho
        )

    ancho_anterior = console.size.width
    panel = construir_panel()

    with Live(panel, screen=True, refresh_per_second=10) as live:
        while True:
            ancho_actual = console.size.width
            if ancho_actual != ancho_anterior:
                panel = construir_panel()
                live.update(panel)
                ancho_anterior = ancho_actual

            # Captura ENTER sin bloquear
            try:
                console.print("\n[bold red]↩ Presione ENTER para continuar...[/bold red]")
                if console.input() == "":
                   break
            except KeyboardInterrupt:
                console.print("[bold red]Cancelado por el usuario.[/bold red]")
                return
            time.sleep(0.2)

    os.system("cls" if os.name == "nt" else "clear")

    # Captura segura de constantes
    try:
        var.T_AMB = float(Prompt.ask("[bold yellow]Temperatura ambiente (T_AMB)[/bold yellow]"))
        var.T_SET = float(Prompt.ask("[bold yellow]Setpoint de temperatura (T_SET)[/bold yellow]"))
        var.K     = float(Prompt.ask("[bold yellow]Ganancia térmica (K)[/bold yellow]"))
        var.TAU   = float(Prompt.ask("[bold yellow]Constante de tiempo (TAU)[/bold yellow]"))
        var.DT    = float(Prompt.ask("[bold yellow]Paso de tiempo (DT)[/bold yellow]"))

        console.print("\n[bold green]✅ Parámetros actualizados:[/bold green]")
        console.print(f"[cyan]  T_AMB = {var.T_AMB} °C[/cyan]")
        console.print(f"[cyan]  T_SET = {var.T_SET} °C[/cyan]")
        console.print(f"[cyan]  K     = {var.K} °C/u[/cyan]")
        console.print(f"[cyan]  TAU   = {var.TAU} s[/cyan]")
        console.print(f"[cyan]  DT    = {var.DT} s[/cyan]")

    except ValueError:
        console.print("\n[bold red]❌ Error: solo se permiten números reales.[/bold red]")



