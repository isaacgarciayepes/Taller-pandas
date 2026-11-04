import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def analizar(df):
    print("\nInfo general:")
    df.info()
    print("\nEstadísticas numéricas:")
    print(df.describe())

    ingresos_por_categoria(df)
    canal_que_mas_vende(df)
    clientes_vip_vs_regular(df)
    metodo_pago_mas_usado(df)
    top5_clientes(df)
    ejemplo_loc_iloc_concat(df)


def ingresos_por_categoria(df):
    """Pregunta 1: ¿Qué categoría genera más ingresos?"""
    # TODO 8
    ingresos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    print("\n[P1] Ingresos por categoría:")
    print(ingresos)
    print(f"Categoría que más ingresa: {ingresos.index[0]} (${ingresos.iloc[0]:,.0f})")


def canal_que_mas_vende(df):
    """Pregunta 2: ¿Qué canal vende más?"""
    # TODO 9
    canales = df.groupby("canal").agg(ventas=("id_venta", "count"), ingresos=("total", "sum"))
    canales = canales.sort_values("ingresos", ascending=False)
    print("\n[P2] Ventas e ingresos por canal:")
    print(canales)
    print(f"Canal con más ingresos: {canales.index[0]} | canal con más ventas: {canales['ventas'].idxmax()}")


def clientes_vip_vs_regular(df):
    """Pregunta 3: ¿Los clientes VIP compran más que los Regulares?"""
    # TODO 10
    seg = df.groupby("segmento_cliente").agg(
        clientes=("id_cliente", "nunique"),
        compras=("id_venta", "count"),
        gasto_total=("total", "sum"),
    )
    seg["compras_por_cliente"] = seg["compras"] / seg["clientes"]
    seg["gasto_por_cliente"] = seg["gasto_total"] / seg["clientes"]
    print("\n[P3] VIP vs Regular (promedios por cliente):")
    print(seg)
    print(f"Mayor gasto promedio por cliente: {seg['gasto_por_cliente'].idxmax()}")


def metodo_pago_mas_usado(df):
    """Pregunta 4: ¿Qué método de pago es más usado?"""
    # TODO 11
    conteo = df["metodo_pago"].value_counts()
    print("\n[P4] Ventas por método de pago:")
    print(conteo)
    print(f"Método más usado: {conteo.index[0]} ({conteo.iloc[0]} ventas)")


def top5_clientes(df):
    """Pregunta 5: ¿Top 5 clientes con más compras?"""
    # TODO 12
    top = (
        df.groupby(["id_cliente", "nombre_cliente"])
        .agg(compras=("id_venta", "count"), gasto_total=("total", "sum"))
        .sort_values(["compras", "gasto_total"], ascending=False)
        .head(5)
    )
    print("\n[P5] Top 5 clientes por número de compras (desempate por gasto):")
    print(top)


def ejemplo_loc_iloc_concat(df):
    """Requisito del reto: una línea con loc/iloc y una con concat."""
    grandes = df.loc[df["total"] > 500000, ["id_venta", "producto", "total"]]
    print("\n[loc] Ventas con total mayor a 500.000:")
    print(grandes)

    print("\n[iloc] Primeras 3 filas y 3 columnas:")
    print(df.iloc[0:3, 0:3])

    online = df[df["canal"] == "Online"]
    tienda = df[df["canal"] == "Tienda"]
    unido = pd.concat([online, tienda])
    print(f"\n[concat] Online: {len(online)} + Tienda: {len(tienda)} = {len(unido)} filas (original: {len(df)})")