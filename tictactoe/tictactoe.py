"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    ex = 0
    oh = 0
    for r in board:
        for tile in r:
            if tile == X: ex += 1
            if tile == O: oh += 1
    return X if oh >= ex else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empties = set()
    r = 0
    for row in board:
        c = 0
        for tile in row:
            if tile == EMPTY:
                empties.add((r, c))
            c += 1
        r += 1
    return empties


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    sampleBoard = copy.deepcopy(board)
    if not action in actions(sampleBoard): raise LookupError
    else:
        sampleBoard[action[0]][action[1]] = player(sampleBoard)
        return sampleBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    transBoard = list(map(list, zip(*copy.deepcopy(board))))
    
    for r in board:
        sum = 0
        for c in r:
            if c == X: sum += 1
            elif c == O: sum -= 1
            else: break
        if sum == 3: return X
        if sum == -3: return O

    for r in transBoard:
        sum = 0
        for c in r:
            if c == X: sum += 1
            elif c == O: sum -= 1
            else: break
        if sum == 3: return X
        if sum == -3: return O

    for r in [
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]:
        sum = 0
        for c in r:
            if c == X: sum += 1
            elif c == O: sum -= 1
            else: break
        if sum == 3: return X
        if sum == -3: return O
            
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empties = False
    if winner(board) != None: return True # Winner
    for r in board:
        if r.count(EMPTY) > 0:
                empties = True
                break
    if not empties: return True # Tie
    else: return False # Not done yet
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X: return 1
    elif winner(board) == O: return -1
    else: return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    curPlayer = player(board)
    score = -99999999999 if curPlayer == X else 99999999999
    bestAction = []
    for action in actions(board):
        if curPlayer == X:
            v = minValue(result(board, action))
            if score < v:
                score = v
                bestAction.insert(0, action)
        else:
            v = maxValue(result(board, action))
            if score > v:
                score = v
                bestAction.insert(0, action)
    return bestAction[0]
        
        
def maxValue(board):
    if terminal(board): return utility(board)
    v = -99999999999
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v
    
    
def minValue(board):
    if terminal(board):
        return utility(board)
    v = 99999999999
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
        
    return v