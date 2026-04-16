"""
Operaciones aritméticas básicas con validación estricta de operandos y resultados.
"""

from __future__ import annotations

import math
import sys
from typing import Final, Union

# Constante matemática (misma precisión que math.pi, IEEE 754 doble precisión)
PI: Final[float] = math.pi

# Límite superior conservador para el valor absoluto de operandos float
# (evita combinar valores tan grandes que el resultado sea inf por desbordamiento)
_MAX_OPERANDO_FLOAT: Final[float] = sys.float_info.max


def _validar_operando(valor: object, nombre: str) -> Union[int, float]:
    """
    Comprueba que el valor sea un número real finito aceptable.

    Rechaza: None, bool (subclase de int en Python), tipos no numéricos,
    NaN e infinitos en float.
    """
    if valor is None:
        raise TypeError(f"{nombre} no puede ser None.")

    if isinstance(valor, bool):
        raise TypeError(
            f"{nombre} no puede ser de tipo bool; use int o float explícitamente."
        )

    if isinstance(valor, int):
        return valor

    if isinstance(valor, float):
        if math.isnan(valor):
            raise ValueError(f"{nombre} no puede ser NaN (no es un número válido).")
        if not math.isfinite(valor):
            raise ValueError(f"{nombre} debe ser finito (no se admiten infinitos).")
        if abs(valor) > _MAX_OPERANDO_FLOAT:
            raise OverflowError(
                f"{nombre} excede el rango máximo permitido para operaciones seguras."
            )
        return valor

    raise TypeError(
        f"{nombre} debe ser int o float; se recibió {type(valor).__name__!r}."
    )


def _resultado_float_seguro(x: float) -> float:
    """Asegura que un resultado float sea finito y representable."""
    if math.isnan(x):
        raise ValueError("El resultado de la operación no es un número válido (NaN).")
    if not math.isfinite(x):
        raise OverflowError(
            "El resultado de la operación excede el rango numérico representable."
        )
    return x


def sumar(a: object, b: object) -> Union[int, float]:
    """
    Suma dos números.

    Si ambos operandos son int, el resultado es int cuando la suma es exacta
    en enteros; en caso contrario se devuelve float.
    """
    x = _validar_operando(a, "a")
    y = _validar_operando(b, "b")

    if isinstance(x, int) and isinstance(y, int):
        try:
            return x + y
        except OverflowError as exc:
            raise OverflowError(
                "La suma de enteros excede el rango representable en esta plataforma."
            ) from exc

    resultado = float(x) + float(y)
    return _resultado_float_seguro(resultado)


def restar(a: object, b: object) -> Union[int, float]:
    """Resta el segundo operando al primero (a - b)."""
    x = _validar_operando(a, "a")
    y = _validar_operando(b, "b")

    if isinstance(x, int) and isinstance(y, int):
        try:
            return x - y
        except OverflowError as exc:
            raise OverflowError(
                "La resta de enteros excede el rango representable en esta plataforma."
            ) from exc

    resultado = float(x) - float(y)
    return _resultado_float_seguro(resultado)


def multiplicar(a: object, b: object) -> Union[int, float]:
    """Multiplica dos números."""
    x = _validar_operando(a, "a")
    y = _validar_operando(b, "b")

    if isinstance(x, int) and isinstance(y, int):
        try:
            return x * y
        except OverflowError as exc:
            raise OverflowError(
                "El producto de enteros excede el rango representable en esta plataforma."
            ) from exc

    resultado = float(x) * float(y)
    return _resultado_float_seguro(resultado)


def dividir(a: object, b: object) -> float:
    """
    Divide a entre b (a / b).

    No se permite división por cero ni operandos que produzcan resultados no finitos.
    """
    x = _validar_operando(a, "a")
    y = _validar_operando(b, "b")

    if y == 0:
        raise ZeroDivisionError("No se puede dividir por cero (el divisor b es 0).")

    resultado = float(x) / float(y)
    return _resultado_float_seguro(resultado)
