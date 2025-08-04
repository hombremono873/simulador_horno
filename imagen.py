# 📦 Importación de librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# 🔁 Definición de la función a integrar
def f(x):
    return 1 / (x + 1)

# 🖼️ Función para generar y mostrar el gráfico
def graficar_integral_rectangulos():
    # 🔢 Parámetros
    a, b = 0, 6              # Intervalo de integración
    n = 6                    # Número de rectángulos
    x = np.linspace(a, b, 1000)  # Puntos finos para curva

    # 📏 Particiones
    x_rect = np.linspace(a, b, n + 1)
    x_left = x_rect[:-1]              # extremos izquierdos
    width = (b - a) / n
    heights = f(x_left)               # alturas de rectángulos

    # 🎨 Crear la figura
    fig, ax = plt.subplots(figsize=(8, 5))
    plt.style.use('classic')

    # 📈 Dibujar la curva
    ax.plot(x, f(x), 'k', linewidth=2, label=r'$y = f(x)$')

    # ▭ Dibujar los rectángulos (método por la izquierda)
    for i in range(n):
        xi = x_left[i]
        hi = heights[i]
        ax.add_patch(plt.Rectangle((xi, 0), width, hi,
                                   edgecolor='black', facecolor='white', lw=1.5))

    # ✏️ Anotaciones matemáticas
    ax.text(x_left[0] + 0.1, heights[0] / 2, r'$a_k$', fontsize=13)
    ax.text(x_left[1] + 0.1, heights[1] / 2, r'$a_{k+1}$', fontsize=13)
    ax.text(3.5, 0.55, r'$\sum_{n=k}^{\infty} a_n$', fontsize=16)
    ax.text(0.5, f(0.5) + 0.05, r'$y = f(x)$', fontsize=14)

    # ⚙️ Configuración del gráfico
    ax.set_xlim(a, b)
    ax.set_ylim(0, 1.2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Fondo blanco
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()

# 🚀 Función principal
def main():
    graficar_integral_rectangulos()

# 📌 Punto de entrada
if __name__ == "__main__":
    main()
