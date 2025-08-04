
from utils.flujo import simular
from visualizacion.menu import mostrar_menu
from rich.console import Console
from utils.flujo import simular
#from rich.prompt import Prompt
from utils.var_pid import pedir_valores_pid
from utils.var_horno import pedir_valores_horno

#comando para actualizar requirements.txt
#pip freeze > nuevo_requirements.txt

# ================================
# EJECUCIÓN DEL PROGRAMA
# ================================

console = Console()

def main():
    console.clear()
    while True:
        console.clear()
        opcion = mostrar_menu()
        
        if opcion == "1":
             console.clear() 
             pedir_valores_pid()
             
        elif opcion == "2":
            console.clear() 
            pedir_valores_horno()
            console.clear() 
        elif opcion == "3":
            console.print("📋 [cyan]Ver parámetros actuales del horno (opcional futuro)[/cyan]")
        elif opcion == "4":
            console.clear() 
            simular()  # ✅ Corre la simulación y vuelve al menú al terminar
            console.clear() 
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
