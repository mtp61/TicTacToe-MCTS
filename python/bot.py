import random
import time
import copy
import math

from shared import *

class Bot():
    def __init__(self, MAX_ITR=200):
        # seed the random number generator
        random.seed = time.time()

        # define max iterations
        self.MAX_ITR = MAX_ITR


    def get_move(self, board):
        # make the root node
        root = Node(board, -1, 2, 0, "root")

        """
        # simple random move bot
        root.generate_children()
        num_moves = len(root.children)
        print(f"{ num_moves } possible moves")
        child = root.children[random.randrange(num_moves)]
        return child.move
        """

        # main loop
        for _ in range(MAX_ITR):
            # selection
            current_node = root
            node_chain = [current_node]
            while current_node.num_visits > 0:
                if current_node.is_win != 0:
                    
                    break
                

            # expansion


            # simulation


            # backpropogation
            
            
            pass


class Node():
    def __init__(self, board, move, player_to_act, is_win, id="node"):
        # game state info
        self.board = board
        self.move = move
        self.player_to_act = player_to_act
        self.is_win = is_win
        self.children = []

        # for MCTS



        # needed for drawing tree
        self.id = id

    
    def generate_children(self):
        # needed for naming children
        ROW_LABELS = ['1', '2', '3']
        COLUMN_LABELS = ['a', 'b', 'c']

        # get open squares
        potential_moves = []
        for i, square in enumerate(self.board):
            if square == 0:
                potential_moves.append(i)
        
        # make a child for each of the potential moves
        for move in potential_moves:
            new_board = copy.deepcopy(self.board)
            new_board[move] = 2
            new_id = COLUMN_LABELS[move % 3] + ROW_LABELS[math.floor(move / 3)]
            self.children.append(Node(new_board, move, 1, check_win(new_board), new_id))
