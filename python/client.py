from bot import Bot
from shared import *

def main():
    # make game and bot
    game = Game()
    bot = Bot()

    # render starting board
    print("Tic-Tac-Toe")
    game.draw_board()

    # main loop
    current_player = 1
    while True:
        if current_player == 1:
            # get player move
            game.player_move()

            # next player is up
            current_player = 2
        else:
            # get bot move
            game.bot_move(bot)

            # next player is up
            current_player = 1
        
        game.draw_board()

        # check for win
        win_status = check_win(game.board)
        if win_status == 1:
            print("Player win")
            break
        elif win_status == 2:
            print("Bot win")
            break
        elif win_status == -1:
            print("Draw")
            break


class Game:
    def __init__(self):
        # define game variables
        self.ROW_LABELS = ['1', '2', '3']
        self.COLUMN_LABELS = ['a', 'b', 'c']
        self.game_active = True

        """
        make the board

        list of ints
        0 is empty square
        1 is player 1 (client)
        2 is player 2 (bot)

        starts at top left, goes by column then row
        """ 
        self.board = [0] * 9

    
    def draw_board(self):
        print()

        for i in range(3):
            print(f"{ self.ROW_LABELS[i] } ", end='')
            for j in range(3):
                if self.board[i * 3 + j] == 0:
                    print(' ', end=' ')
                elif self.board[i * 3 + j] == 1:
                    print('X', end=' ')
                elif self.board[i * 3 + j] == 2:
                    print('O', end=' ')
            print()
        
        print()
        print("  ", end='')
        for i in range(3):
            print(f"{ self.COLUMN_LABELS[i] } ", end='')            
        print()
        print()
    
                
    def player_move(self):
        while True:
            move = input("Enter your move [a-c][1-3]: ")

            # check that move follows format
            if len(move) != 2:
                continue
            if not (move[0] in self.COLUMN_LABELS and move[1] in self.ROW_LABELS):
                continue

            # check that move is legal
            move_parsed = 3 * self.ROW_LABELS.index(move[1]) + self.COLUMN_LABELS.index(move[0])
            if self.board[move_parsed] != 0:
                continue

            break

        # execute move
        self.board[move_parsed] = 1


    def bot_move(self, bot):
        # get move
        move = bot.get_move(self.board)

        # execute move
        self.board[move] = 2


if __name__ == '__main__':
    main()
