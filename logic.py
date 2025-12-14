"""Plantilla con las funciones que el alumnado debe completar para M3.

La capa gráfica llama a estas funciones para mover el estado del juego. No es
necesario crear clases; basta con manipular listas, diccionarios y tuplas.
"""
from __future__ import annotations

import random
import string
import pygame
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

    total_cartas = rows*cols

    if rows > 8:
        raise ValueError("El limite de filas es de 8.")
    elif cols > 10:
        raise ValueError("El limite de columnas es de 10.")
    elif total_cartas > 60:
        raise ValueError("El limite total de cartas es de 60")
    
    num_parejas_necesarias = total_cartas // 2

    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    if num_parejas_necesarias > len(caracteres):
       raise ValueError(f"Se necesitan {num_parejas_necesarias} símbolos únicos, pero solo hay {len(caracteres)} disponibles.")
    
    random_simbolos = ''.join([random.choice(caracteres) for n in range(num_parejas_necesarias)])

    # Se duplican las cartas
    lista_simbolos = []
    for simbol in random_simbolos:
        lista_simbolos.append(simbol)
        lista_simbolos.append(simbol)

    # Se barajan las cartas
    random.shuffle(lista_simbolos)
    return lista_simbolos


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
    
                
    try:
        # Asegúrate de que el módulo mixer esté disponible/inicializado
        if not pygame.mixer.get_init():
            pygame.mixer.init()
            
        # Carga y reproduce la música de fondo
        pygame.mixer.music.load("misc/m1.mp3") 
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.3)
        
    except pygame.error as e:
        print(f"Advertencia: No se pudo iniciar la música de fondo. Asegúrate de tener el archivo de musica. Error: {e}")

    # Obtiene la lista de símbolos barajados (depende de tu parte Alex)
    simbolos = build_symbol_pool(rows, cols)
    
    # Construir el tablero (lista de listas de cartas)
    tablero = []
    indice_simbolo = 0
    
    for fila in range(rows):
        cartas_fila = []
        for columna in range(cols):
            carta = {
                "symbol": simbolos[indice_simbolo],
                "state": STATE_HIDDEN
            }
            cartas_fila.append(carta)
            indice_simbolo += 1
        tablero.append(cartas_fila)
    
    # Se calcula el numero total de parejas
    casillas_totales = rows * cols      
    parejas_totales = casillas_totales // 2
    
    #devuelve el estado inicial del juego.
    estado_juego = {
        "board": tablero,
        "pending": [],
        "moves": 0,
        "matches": 0,
        "total_pairs": parejas_totales,
        "rows": rows,
        "cols": cols
    }
    
    return estado_juego

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

    # Obtener las coordenadas de las cartas pendientes
    card1_coords, card2_coords = game['pending']
    
    # Acceder a las cartas usando las coordenadas
    card1 = game['board'][card1_coords[0]][card1_coords[1]]
    card2 = game['board'][card2_coords[0]][card2_coords[1]]
    
    # Inicializar la variable para saber si hay pareja
    pareja_encontrada = False
    
    # Comprobar si las cartas coinciden
    if card1['symbol'] == card2['symbol']:
        # Las cartas coinciden, se marcan como encontradas
        card1['state'] = STATE_FOUND
        card2['state'] = STATE_FOUND
        
        # Incrementar el contador de matches
        game['matches'] += 1
        pareja_encontrada = True
    else:
        # Las cartas no coinciden, se ocultan de nuevo
        card1['state'] = STATE_HIDDEN
        card2['state'] = STATE_HIDDEN
    
    # Incrementar el contador de movimientos
    game['moves'] += 1
    
    # Limpiar la lista de pendientes
    game['pending'] = []
    
    # Devolver la tupla: (resuelto, pareja_encontrada)
    return True, pareja_encontrada


def has_won(game: GameState) -> bool:
    """Indica si se han encontrado todas las parejas."""
    return game["matches"] == game["total_pairs"]
