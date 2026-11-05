from pathlib import Path

import matplotlib.pyplot as plt

SALIDA = Path(__file__).parent / "Data" / "processed" / "graficos"


def grafico_ventas_por_categoria(df):
    """Gráfico de barras: total vendido por categoría."""
    # TODO 13
    SALIDA.mkdir(parents=True, exist_ok=True)
    datos = df.groupby("categoria")["total"].sum()
    datos.plot(kind="bar")
    plt.title("Total vendido por categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Total vendido (COP)")
    plt.savefig(SALIDA / "ventas_por_categoria.png", bbox_inches="tight")
    plt.show()
    plt.close()


def grafico_ventas_por_canal(df):
    """Gráfico de barras: total vendido por canal (Online contra Tienda)."""
    # TODO 14
    SALIDA.mkdir(parents=True, exist_ok=True)
    datos = df.groupby("canal")["total"].sum()
    datos.plot(kind="bar")
    plt.title("Total vendido por canal")
    plt.xlabel("Canal")
    plt.ylabel("Total vendido (COP)")
    plt.savefig(SALIDA / "ventas_por_canal.png", bbox_inches="tight")
    plt.show()
    plt.close()


def graficar(df):
    grafico_ventas_por_categoria(df)
    grafico_ventas_por_canal(df)