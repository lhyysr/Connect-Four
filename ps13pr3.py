#
# ps13pr3.py (Problem Set 13, Problem 3)
#
# Playing the game!
#
# name: Haoyuan Liu
# email: lhyysr@bu.edu
#
# This is an individual-only problem that you must complete on your own,
# without a partner.
#

from ps13pr1 import Board
from ps13pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
        players (objects of the Player class or a subclass of Player).
        One of them should use 'X' checkers and the other should
        use 'O' checkers.
    """
    # Make sure that one is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board

# Function 1
def process_move(player, board):
    '''perform all of the steps involved in processing a single move
       inputs: a Player and a Board
    '''
    print(str(player) + "'s turn")     # a
    put_in = player.next_move(board)   # b
    print(str(put_in))
    board.add_checker(player.checker, put_in)
    print()
    print(board)
    if board.is_win_for(player.checker):
        s = str(player) + ' wins in ' + str(player.num_moves) + ' moves.\n' + \
            'Congratulations!'
        print(s)
        return True
    elif board.is_full():
        print("It's a tie!")
        return True
    else:
        return False
    

# 2-define class
class RandomPlayer(Player):   #a

    #c
    def next_move(self, board):
        '''choose at random col in the specified board that are not yet full,
           and return the index of that randomly selected column.
           input: board
        '''
        available_col = [col for col in range(board.width) \
                         if board.can_add_to(col)]
        col = random.choice(available_col)
        self.num_moves += 1
        return col
    











