
import minimax_helpers
import gamestate as game
import minimax
import search
import openingbook



print("Creating empty game board...")
g = game.GameState()

print("Checking active player on an empty board...")
if g.player() != 0:
    print("Failed\n Uh Oh! Your game did not return player " +
          "id 0 on an empty board.")
else:
    print("Passed.")
print('----------------------------------------------------')

print("Checking terminal test on an empty board...")
if g.terminal_test() != False:
    print("Failed\n Uh Oh! Your game marked an empty game state as terminal.")
else:
    print("Passed.")
print('----------------------------------------------------')

print("Checking liberties on an empty board...")
p1_liberties = g.liberties(None)
if len(p1_liberties) != 5:
    print("Failed\n Uh oh! Your game did not return 5 empty " +
          "cell locations as liberties on an empty board.")
else:
    print("Passed.")
print('----------------------------------------------------')

print("Getting legal moves for player 1...")
p1_empty_moves = g.actions()
print("Found {} legal moves.".format(len(p1_empty_moves or [])))

print("Applying move {} for player 1...".format(p1_empty_moves[0]))
g1 = g.result(p1_empty_moves[0])

print("Getting legal moves for player 2...")
p2_empty_moves = g1.actions()
if len(p2_empty_moves) != 4:
    print("Failed\n  Uh oh! Your game did not return the expected " +
          "number of actions for player 2!")
else:
    print("Passed.")
print('----------------------------------------------------')

print("\nPlaying a full game")
for _ in range(5):
    if g.terminal_test(): break
    g = g.result(g.actions()[0])

print("Checking terminal test on a terminal board...")
if g.terminal_test() != True:
    print("Failed\n  Uh oh! Your game did not correctly evalute " +
          "a terminal game state as terminal!")
else:
    print("Passed.")
print('----------------------------------------------------')

depth_limit = 10
g_new = game.GameState()
inf = float("inf")
actions = [((0, 0), inf), ((1, 0), -inf), ((2, 0), inf), ((0, 1), inf), ((1, 1), -inf)]

if all(minimax_helpers.minimax_min_value(g_new.result(a), depth_limit) == ev for a, ev in actions):
    print("Looks like everything works!")
else:
    print("Uh oh! Not all the scores matched.")

print('----------------------------------------------------')

best_moves = set([(0, 0), (2, 0), (0, 1)])
rootNode = game.GameState()
minimax_move = minimax.minimax_decision(rootNode, depth_limit)
print("Best move choices: {}".format(list(best_moves)))
print("Your code chose: {}".format(minimax_move))

if minimax_move in best_moves:
    print("That's one of the best move choices. Looks like your minimax-decision function worked!")
else:
    print("Uh oh...looks like there may be a problem.")

print('----------------------------------------------------')

# Test the depth limit by checking the number of nodes visited
# -- recall that minimax visits every node in the search tree,
# so if we search depth one on an empty board then minimax should
# visit each of the five open spaces
depth_limit = 1
game.call_counter = 0
expected_node_count = 5
rootNode = game.GameState()
_ = minimax.minimax_decision(rootNode, depth_limit)
print("Expected node count: {}".format(expected_node_count))
print("Your node count: {}".format(game.call_counter))

if game.call_counter == expected_node_count:
    print("That's right! Looks like your depth limit is working!")
else:
    print("Uh oh...looks like there may be a problem.")

print('----------------------------------------------------')

depth_limit = 1
expected_values = 0
rootNode = game.GameState()
tests = [((0, 0), 2), ((1, 0), 3), ((2, 0), 1), ((0, 1), 2), ((1, 1), 3)]

if all(minimax_helpers.minimax_min_value(rootNode.result(a), depth_limit) == v for a, v in tests):
    print("Evaluation function worked, good job!")
else:
    print("Uh oh!\n Looks like one or more of the values didn't match.")

print('----------------------------------------------------')


# Test the depth limit by checking the number of nodes visited
# -- recall that minimax visits every node in the search tree,
# so if we search depth one on an empty board then minimax should
# visit the sum of each sub-tree
game.call_counter = 0
depth_limit = 2
expected_node_count = 30
rootNode = game.GameState()
search.get_action(rootNode, depth_limit)

print("Expected node count: {}".format(expected_node_count))
print("Your node count: {}".format(game.call_counter))

if game.call_counter == expected_node_count:
    print("That's right! Iterative deepening is working!")
else:
    print("Uh oh...looks like there may be a problem.")

print('----------------------------------------------------')

# Test the depth limit by checking the number of nodes visited
# -- recall that minimax visits every node in the search tree,
# so if we search depth one on an empty board then minimax should
# visit each of the five open spaces
game.call_counter = 0
expected_node_count = 55
rootNode = game.GameState()
minimax.alpha_beta_search(rootNode)

print("Expected node count: {}".format(expected_node_count))
print("Your node count: {}".format(game.call_counter))

if game.call_counter == expected_node_count:
    print("That's right! Looks like your alpha-beta pruning is working!")
else:
    print("Uh oh...looks like there may be a problem.")

print('----------------------------------------------------')
book = openingbook.build_table(10)

assert len(book) > 0, "Your opening book is empty"
assert all(isinstance(k, tuple) for k in book), \
    "All the keys should be `hashable`"
assert all(isinstance(v, tuple) and len(v) == 2 for v in book.values()), \
    "All the values should be tuples of (x, y) actions"
print("Looks like your book worked!")
print(book)