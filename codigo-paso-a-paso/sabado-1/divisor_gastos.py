"""Divisor de gastos de gmaron, según especificacion.md.

Divide una cuenta en partes iguales y calcula quién le transfiere a quién
para quedar a mano. Las transferencias son siempre en pesos enteros.
"""

from collections import Counter
from dataclasses import dataclass
from decimal import ROUND_CEILING, Decimal
from typing import NamedTuple

LARGO_MINIMO_NOMBRE = 3
MENSAJE_A_MANO = "Están a mano"

Pago = tuple[str, float]
"""(nombre, cuánto puso)."""


class Transferencia(NamedTuple):
    quien_paga: str
    a_quien: str
    monto: int


@dataclass(frozen=True)
class Persona:
    """Una persona de la salida.

    El alias es su posición en la lista de pagos. Así, dos personas con el
    mismo nombre se cuentan por separado y su plata no se mezcla.
    """

    alias: int
    nombre: str
    aporte: Decimal


class _Movimiento(NamedTuple):
    """Una transferencia entre personas, con su alias, antes de pasarla a nombres."""

    quien_paga: Persona
    a_quien: Persona
    monto: int


def dividir(pagos: list[Pago]) -> list[Transferencia]:
    """Devuelve las transferencias necesarias para que todos queden a mano.

    Una lista vacía significa "Están a mano".
    Lanza ValueError si un nombre es muy corto o un monto es negativo.
    """
    return [
        Transferencia(m.quien_paga.nombre, m.a_quien.nombre, m.monto)
        for m in _calcular_movimientos(pagos)
    ]


def mostrar(pagos: list[Pago]) -> str:
    """Texto para la pantalla: las transferencias, "Están a mano" o el error.

    Si un nombre se repite, cada uno lleva su número según el orden en que se cargó.
    """
    try:
        movimientos = _calcular_movimientos(pagos)
    except ValueError as error:
        return f"Error: {error}"
    if not movimientos:
        return MENSAJE_A_MANO
    etiquetas = _etiquetar(pagos)
    return "\n".join(
        f"{etiquetas[m.quien_paga.alias]} le transfiere ${m.monto} a {etiquetas[m.a_quien.alias]}"
        for m in movimientos
    )


def explicar(pagos: list[Pago]) -> str:
    """Las cuentas paso a paso y después las transferencias, para que cualquiera pueda verificarlas."""
    try:
        personas = _crear_personas(pagos)
    except ValueError as error:
        return f"Error: {error}"
    if not personas:
        return MENSAJE_A_MANO

    total = sum((p.aporte for p in personas), Decimal(0))
    cuota = total / len(personas)
    deudas, creditos = _calcular_saldos(personas, cuota)
    etiquetas = _etiquetar(pagos)

    lineas = [
        f"Entre todos pusieron {_pesos(total)}.",
        f"Son {len(personas)} personas: a cada una le toca {_pesos(total)} / {len(personas)} = {_pesos(cuota)}.",
        "",
    ]
    for p in personas:
        if p in deudas:
            saldo = f"debe {_pesos(cuota)} - {_pesos(p.aporte)} = {_pesos(cuota - p.aporte)}"
            if deudas[p] != cuota - p.aporte:
                saldo += f", redondeado para arriba: ${deudas[p]}"
        elif p in creditos:
            saldo = f"le devuelven {_pesos(p.aporte)} - {_pesos(cuota)} = {_pesos(p.aporte - cuota)}"
            if creditos[p] != p.aporte - cuota:
                saldo += f", redondeado para arriba: ${creditos[p]}"
        else:
            saldo = "está a mano"
        lineas.append(f"  {etiquetas[p.alias]} puso {_pesos(p.aporte)}: {saldo}.")

    if any(deudas[p] != cuota - p.aporte for p in deudas):
        lineas += ["", "Los centavos se redondean para arriba, a favor de quien pagó."]
    if deudas and creditos:
        sobrante = sum(deudas.values()) - sum(creditos.values())
        if sobrante > 0:
            el_que_mas_puso = max(creditos, key=lambda p: p.aporte)
            lineas.append(
                f"Por el redondeo se juntan ${sobrante} de más: van a {etiquetas[el_que_mas_puso.alias]}, "
                f"que es quien más puso, y recibe ${creditos[el_que_mas_puso] + sobrante} en total."
            )

    return "\n".join(lineas + ["", mostrar(pagos)])


def _pesos(monto: Decimal) -> str:
    """$500 si es entero; $333,33 si tiene centavos."""
    if monto == monto.to_integral_value():
        return f"${int(monto)}"
    return f"${monto:.2f}".replace(".", ",")


def _crear_personas(pagos: list[Pago]) -> list[Persona]:
    _validar(pagos)
    return [
        Persona(alias, nombre, Decimal(str(monto)))
        for alias, (nombre, monto) in enumerate(pagos)
    ]


def _calcular_movimientos(pagos: list[Pago]) -> list[_Movimiento]:
    personas = _crear_personas(pagos)
    if not personas:
        return []

    cuota = sum((p.aporte for p in personas), Decimal(0)) / len(personas)
    deudas, creditos = _calcular_saldos(personas, cuota)
    if not deudas or not creditos:
        return []

    creditos = _sumar_sobrante_al_que_mas_puso(deudas, creditos)
    return _armar_transferencias(deudas, creditos)


def _etiquetar(pagos: list[Pago]) -> list[str]:
    """El nombre de cada persona para la pantalla, en el orden de los pagos.

    Los nombres repetidos se numeran: "Ana (1)", "Ana (2)". Los únicos quedan igual.
    """
    repeticiones = Counter(nombre for nombre, _ in pagos)
    vistos: Counter[str] = Counter()
    etiquetas = []
    for nombre, _ in pagos:
        if repeticiones[nombre] == 1:
            etiquetas.append(nombre)
            continue
        vistos[nombre] += 1
        etiquetas.append(f"{nombre} ({vistos[nombre]})")
    return etiquetas


def _validar(pagos: list[Pago]) -> None:
    for nombre, monto in pagos:
        if len(nombre) < LARGO_MINIMO_NOMBRE:
            raise ValueError(
                f"el nombre {nombre!r} tiene que tener al menos {LARGO_MINIMO_NOMBRE} caracteres"
            )
        if monto < 0:
            raise ValueError("no se aceptan montos negativos")


def _calcular_saldos(
    personas: list[Persona], cuota: Decimal
) -> tuple[dict[Persona, int], dict[Persona, int]]:
    """Cuánto debe cada deudor y cuánto cobra cada acreedor, en pesos enteros.

    Los dos se redondean para arriba: el redondeo queda a favor de quien pagó.
    """
    deudas = {p: _redondear_para_arriba(cuota - p.aporte) for p in personas if p.aporte < cuota}
    creditos = {p: _redondear_para_arriba(p.aporte - cuota) for p in personas if p.aporte > cuota}
    return deudas, creditos


def _sumar_sobrante_al_que_mas_puso(
    deudas: dict[Persona, int], creditos: dict[Persona, int]
) -> dict[Persona, int]:
    """Por el redondeo puede entrar más de lo que se reparte; el sobrante va al que más puso."""
    sobrante = sum(deudas.values()) - sum(creditos.values())
    if sobrante <= 0:
        return creditos
    el_que_mas_puso = max(creditos, key=lambda p: p.aporte)
    return {**creditos, el_que_mas_puso: creditos[el_que_mas_puso] + sobrante}


def _armar_transferencias(
    deudas: dict[Persona, int], creditos: dict[Persona, int]
) -> list[_Movimiento]:
    """El que más debe le paga primero al que más puso. Los empates van por orden alfabético."""
    deudores = sorted(deudas, key=lambda p: (-deudas[p], p.nombre, p.alias))
    acreedores = sorted(creditos, key=lambda p: (-p.aporte, p.nombre, p.alias))
    falta_cobrar = dict(creditos)

    transferencias: list[_Movimiento] = []
    for deudor in deudores:
        falta_pagar = deudas[deudor]
        for acreedor in acreedores:
            if falta_pagar == 0:
                break
            monto = min(falta_pagar, falta_cobrar[acreedor])
            if monto == 0:
                continue
            transferencias.append(_Movimiento(deudor, acreedor, monto))
            falta_cobrar[acreedor] -= monto
            falta_pagar -= monto
    return transferencias


def _redondear_para_arriba(monto: Decimal) -> int:
    return int(monto.to_integral_value(rounding=ROUND_CEILING))


def _leer_pagos() -> list[Pago]:
    """Lee una persona por línea ("nombre monto") hasta una línea vacía."""
    pagos: list[Pago] = []
    while linea := input("> ").strip():
        nombre, _, monto = linea.rpartition(" ")
        pagos.append((nombre, float(monto)))
    return pagos


if __name__ == "__main__":
    print("Una persona por línea: nombre monto (línea vacía para terminar)")
    print(explicar(_leer_pagos()))
