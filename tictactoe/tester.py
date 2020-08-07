from tictactoe import player, actions, result, winner, terminal, utility, minimax
X = "X"
O = "O"
EMPTY = None

# print("Player: ", player([
#     [EMPTY,EMPTY,EMPTY],
#     [EMPTY,EMPTY,EMPTY],
#     [EMPTY,EMPTY,EMPTY]
# ]))

# print("Actions: ", actions([
#     [X,EMPTY,O],
#     [EMPTY,X,EMPTY],
#     [EMPTY,EMPTY,EMPTY]
# ]))

# print("Result: ", result([
#     [X,EMPTY,O],
#     [O,X,EMPTY],
#     [EMPTY,EMPTY,EMPTY]
# ], (2,2) ))

# print("Winner: ", winner([
#     [X, O, EMPTY],
#     [ O, O, O ],
#     [O, X, EMPTY]
# ]))

# print("Terminal: ", terminal([
#     [X,O,O],
#     [O,X,X],
#     [O,X,O]
# ]))

# print("Utility: ", utility([
#     [X, EMPTY, X],
#     [ O, EMPTY, O ],
#     [O, X, O]
# ]))

print("Minimax: ", minimax([
    [X,EMPTY,O],
    [EMPTY,X,EMPTY],
    [EMPTY,EMPTY,EMPTY]
]))