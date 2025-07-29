
from utils.flujo import simular
from visualizacion.menu import mostrar_menu
from rich.console import Console
from utils.flujo import simular
from rich.prompt import Prompt
from utils.var_pid import pedir_valores_pid
from utils.var_horno import pedir_valores_horno
#from utils.menu_eventos import menu_solo_opciones_4_y_7  # si lo pones aparte
# ================================
# EJECUCIÓN DEL PROGRAMA
# ================================

console = Console()

def main():
    console.clear()
    while True:
        mostrar_menu()
        opcion = Prompt.ask("\nSeleccione una opción", choices=["1", "2", "3", "4", "5", "6", "7"])

        if opcion == "1":
             console.print("🔧 [cyan]Configurar PID (pendiente de implementación)[/cyan]")
             pedir_valores_pid()
        elif opcion == "2":
            pedir_valores_horno()
            console.print("🔥 [cyan]Configurar Horno (pendiente de implementación)[/cyan]")
        elif opcion == "3":
            console.print("📋 [cyan]Ver parámetros actuales del horno (opcional futuro)[/cyan]")
        elif opcion == "4":
            console.clear() 
            simular()  # ✅ Corre la simulación y vuelve al menú al terminar
            console.print("[green]▶ Ejecutando simulación con gráfica PID[/green]")
        elif opcion == "5":
            console.print("[cyan]📈 Gráfica térmica (aún no implementada)[/cyan]")
        elif opcion == "6":
            console.print("[cyan]📊 Mostrar gráfica de tendencia (futura)[/cyan]")
        elif opcion == "7":
            console.clear()
            console.print("[bold red]👋 Saliendo del simulador...[/bold red]")
            break
        else:
            console.print("[red]❌ Opción inválida[/red]")

if __name__ == "__main__":
    main()
