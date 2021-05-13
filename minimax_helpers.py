# DO NOT MODIFY THE PLAYER ID
player_id = 0

def my_moves(gameState):
    loc = gameState._player_locations[player_id]
    return len(gameState.liberties(loc))

def minimax_min_value(gameState, depth):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)

    if depth <= 0:
        return my_moves(gameState)

    v = float("inf")
    for a in gameState.actions():
        # the depth should be decremented by 1 on each call
        v = min(v, minimax_max_value(gameState.result(a), depth - 1))
    return v


def minimax_max_value(gameState, depth):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)

    if depth <= 0:
        return my_moves(gameState)

    v = float("-inf")
    for a in gameState.actions():
        # the depth should be decremented by 1 on each call
        v = max(v, minimax_min_value(gameState.result(a), depth - 1))
    return v


def ab_min_value(gameState, alpha, beta):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)

    v = float("inf")
    for a in gameState.actions():
        v = min(v, ab_max_value(gameState.result(a), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def ab_max_value(gameState, alpha, beta):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if gameState.terminal_test():
        return gameState.utility(0)

    v = float("-inf")
    for a in gameState.actions():
        v = max(v, ab_min_value(gameState.result(a), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v