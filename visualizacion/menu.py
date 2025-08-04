"""from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align
from rich.live import Live
import threading
import time

console = Console()

opcion_usuario = None  # Variable compartida para capturar la opción

def construir_layout(opciones: str) -> Layout:
    layout = Layout(name="root")

    panel_menu = Panel(
        opciones,
        title="[bold magenta]Simulador de Temperatura[/bold magenta]",
        border_style="bright_blue",
        padding=(1, 4),
        width=max(40, int(console.size.width * 0.6))
    )

    layout.update(Align.center(panel_menu, vertical="middle"))
    return layout

def leer_opcion():
    global opcion_usuario
    #console.print("\n" * (console.size.height - 8))  # Baja hasta la última línea
    opcion = console.input("[bold cyan]Seleccione una opción ahora:[/bold cyan] ") 
    return opcion

def mostrar_menu():
    global opcion_usuario

    opciones = (
        "[green]"
        "\n1. Configurar PID"
        "\n2. Configurar horno"
        "\n3. Ver parámetros actuales"
        "\n4. Ejecutar simulación"
        "\n5. Para entrada de datos pulse enter"
        "\n6. Salir[/green]"
      
    )

    layout = construir_layout(opciones)
    ancho_anterior = console.size.width

    # Iniciar hilo para capturar input sin bloquear Live
    hilo_entrada = threading.Thread(target=leer_opcion, daemon=True)
    hilo_entrada.start()

    with Live(layout, refresh_per_second=10, screen=True) as live:
        while hilo_entrada.is_alive():
            ancho_actual = console.size.width
            if ancho_actual != ancho_anterior:
                layout = construir_layout(opciones)
                live.update(layout)
                ancho_anterior = ancho_actual
            time.sleep(0.2)  # control de velocidad de actualización
    opcion_usuario=leer_opcion()
    return opcion_usuario"""
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align
from rich.live import Live
import time

console = Console()

def construir_layout(opciones: str) -> Layout:
    layout = Layout(name="root")

    panel_menu = Panel(
        opciones,
        title="[bold magenta]Simulador de Temperatura[/bold magenta]",
        border_style="bright_blue",
        padding=(1, 4),
        width=max(40, int(console.size.width * 0.6))
    )

    layout.update(Align.center(panel_menu, vertical="middle"))
    return layout

def mostrar_menu():
    opciones = (
        "[green]"
        "\n1. Configurar PID"
        "\n2. Configurar horno"
        "\n3. Ver parámetros actuales"
        "\n4. Ejecutar simulación"
        "\n5. Para entrada de datos pulse enter"
        "\n6. Salir[/green]"
    )

    ancho_anterior = console.size.width
    layout = construir_layout(opciones)

    with Live(layout, refresh_per_second=4, screen=True) as live:
        while True:
            ancho_actual = console.size.width
            if ancho_actual != ancho_anterior:
                layout = construir_layout(opciones)
                live.update(layout)
                ancho_anterior = ancho_actual

            #time.sleep(0.1)
            # ✅ Salir del Live al presionar ENTER (como todas tus otras pantallas)
            if console.input("\n[bold yellow]↩ ENTER para seleccionar una opción...[/bold yellow]") == "":
                break
            time.sleep(0.02)

    #console.clear()
    opcion = console.input("[bold cyan]Seleccione una opción ahora:[/bold cyan] ")
    return opcion

