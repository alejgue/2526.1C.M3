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
    """Intenta descubrir la carta ubicada en ``row``, ``col``.

    Debe devolver ``True`` si el estado ha cambiado (es decir, la carta estaba
    oculta y ahora está visible) y ``False`` en cualquier otro caso. No permitas
    dar la vuelta a más de dos cartas simultáneamente.
    """

    raise NotImplementedError


def resolve_pending(game: GameState) -> Tuple[bool, bool]:
    """Resuelve el turno si hay dos cartas pendientes.

    Devuelve una tupla ``(resuelto, pareja_encontrada)``. Este método debe
    ocultar las cartas si son diferentes o marcarlas como ``found`` cuando
    coincidan. Además, incrementa ``moves`` y ``matches`` según corresponda.
    """

    # Obtener las coordenadas de las cartas pendientes
    card1_coords, card2_coords = GameState['pending']
    
    # Acceder a las cartas usando las coordenadas
    card1 = GameState['board'][card1_coords[0]][card1_coords[1]]
    card2 = GameState['board'][card2_coords[0]][card2_coords[1]]
    
    # Inicializar la variable para saber si hay pareja
    pareja_encontrada = False
    
    # Comprobar si las cartas coinciden
    if card1['symbol'] == card2['symbol']:
        # Las cartas coinciden, se marcan como encontradas
        card1['state'] = 'STATE_FOUND'
        card2['state'] = 'STATE_FOUND'
        
        # Incrementar el contador de matches
        GameState['matches'] += 1
        pareja_encontrada = True
    else:
        # Las cartas no coinciden, se ocultan de nuevo
        card1['state'] = 'STATE_HIDDEN'
        card2['state'] = 'STATE_HIDDEN'
    
    # Incrementar el contador de movimientos
    GameState['moves'] += 1
    
    # Limpiar la lista de pendientes
    GameState['pending'] = []
    
    # Devolver la tupla: (resuelto, pareja_encontrada)
    return True, pareja_encontrada

    raise NotImplementedError


def has_won(game: GameState) -> bool:
    """Indica si se han encontrado todas las parejas."""

    raise NotImplementedError
