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
    
    
    casillas_totales = rows * cols      #aqui se calcula el numero total de parejas
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