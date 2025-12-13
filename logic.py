"""Plantilla con las funciones que el alumnado debe completar para M3.

La capa gráfica llama a estas funciones para mover el estado del juego. No es
necesario crear clases; basta con manipular listas, diccionarios y tuplas.
"""
from __future__ import annotations

import random
from typing import Dict, List, Tuple

STATE_HIDDEN = "hidden"
STATE_VISIBLE = "visible"
STATE_FOUND = "found"

Card = Dict[str, str]
Board = List[List[Card]]
Position = Tuple[int, int]
GameState = Dict[str, object]


def build_symbol_pool(rows: int, cols: int) -> List[str]:
    """Crea la lista de símbolos necesaria para rellenar todo el tablero.

    Sugerencia: parte de un listado básico de caracteres y duplícalo tantas
    veces como parejas necesites. Después baraja el resultado.
    """

    raise NotImplementedError


def create_game(rows: int, cols: int) -> GameState:
    """Genera el diccionario con el estado inicial del juego.

    El estado debe incluir:
    - ``board``: lista de listas con cartas (cada carta es un dict con
      ``symbol`` y ``state``).
    - ``pending``: lista de posiciones descubiertas en el turno actual.
    - ``moves``: contador de movimientos realizados.
    - ``matches``: parejas acertadas.
    - ``total_pairs``: número total de parejas disponibles.
    - ``rows`` / ``cols``: dimensiones del tablero.
    """

    raise NotImplementedError


def reveal_card(game: GameState, row: int, col: int) -> bool:
    """Intenta revelar la carta en (row, col). Devuelve True si se revela."""
    revelada = True

    # Validar coordenadas
    if row < 0 or col < 0 or row >= game["rows"] or col >= game["cols"]:
        revelada = False
    else:
        card = game["board"][row][col]
        pending = game["pending"]

        # No permitir más de dos cartas visibles
        if len(pending) >= 2:
            revelada = False
        # Evitar revelar la misma carta dos veces
        elif card["state"] != STATE_HIDDEN:
            revelada = False

        # Si todo es correcto, revelar
        if revelada:
            card["state"] = STATE_VISIBLE
            pending.append((row, col))

    return revelada


def resolve_pending(game: GameState) -> Tuple[bool, bool]:
    """Resuelve el turno si hay dos cartas pendientes.

    Devuelve una tupla ``(resuelto, pareja_encontrada)``. Este método debe
    ocultar las cartas si son diferentes o marcarlas como ``found`` cuando
    coincidan. Además, incrementa ``moves`` y ``matches`` según corresponda.
    """

    raise NotImplementedError


def has_won(game: GameState) -> bool:
    """Indica si se han encontrado todas las parejas."""

    raise NotImplementedError
