# Tic-Tac-Toe MCTS

This program uses Monte-Carlo Tree Search with Upper Confidence Trees to play a user in the game of Tic-Tac-Toe. While MCTS is clearly not required for a game with a small game tree like Tic-Tac-Toe, I wanted to make sure I got the algorithm correct before moving on to more complex applications.

The program is implemented in both Python and C++ (or will be soon...)

Improvements could be made to the simulations, for example if an opponent can win with a move they should always take it, and this should be reflected in the is_win variable for the parent node.