from pathlib import Path

import pandas as pd

PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
    # TODO 6: validaciones antes del merge
    ok = True

    if "id_cliente" not in clientes.columns or "id_cliente" not in ventas.columns:
        print("[validación] ERROR: falta la columna id_cliente en alguno de los dataframes.")
        return False
    print("[validación] OK: id_cliente existe en clientes y ventas.")

    repetidos = clientes["id_cliente"].duplicated().sum()
    if repetidos > 0:
        print(f"[validación] ERROR: hay {repetidos} id_cliente repetidos en clientes.")
        ok = False
    else:
        print("[validación] OK: id_cliente no está repetido en clientes.")

    if clientes["id_cliente"].dtype != ventas["id_cliente"].dtype:
        print(f"[validación] ERROR: tipos distintos ({clientes['id_cliente'].dtype} vs {ventas['id_cliente'].dtype}).")
        ok = False
    else:
        print(f"[validación] OK: id_cliente tiene el mismo tipo en ambos ({ventas['id_cliente'].dtype}).")

    sin_cliente = (~ventas["id_cliente"].isin(clientes["id_cliente"])).sum()
    print(f"[validación] Ventas sin cliente asociado: {sin_cliente}")

    return ok


def unir(clientes, ventas):
    # TODO 7: validar, hacer el merge, guardar el CSV y devolver el dataframe
    if not validar_premerge(clientes, ventas):
        print("No se hizo el merge porque la validación falló.")
        return None

    df = ventas.merge(clientes, on="id_cliente", how="left", validate="m:1")

    PROCESSED.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED / "merge.csv", index=False)

    print(f"[merge] ventas: {ventas.shape} | clientes: {clientes.shape} | resultado: {df.shape}")
    print(f"[merge] Columnas esperadas: {ventas.shape[1]} + {clientes.shape[1]} - 1 = {ventas.shape[1] + clientes.shape[1] - 1}")
    return df