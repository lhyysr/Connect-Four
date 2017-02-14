#
# ps13pr2.py (Problem Set 13, Problem 2)
#
# A Connect Four Player class 
#
# name: Haoyuan Liu
# email: lhyysr@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from ps13pr1 import Board

# Write your Player class below.
class Player:

    # 1-constructor
    def __init__(self, checker):
        '''onstructs a new Player object
           input: 'X' or 'O'
        '''
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    # 2-method
    def __str__(self):
        '''returns a string representing a Player object'''
        s = 'Player' + ' ' + self.checker
        return s

    # 3-method
    def __repr__(self):
        '''returns a string representing a Player object'''
        return str(self)
    
    # 4-method
    def opponent_checker(self):
        '''returns a one-character string representing
           the checker of the Player object’s opponent
        '''
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    # 5-method
    def next_move(self, board):
        '''returns the column where the player wants to make the next move.
           input: Board
        '''
        col = int(input('Enter a column: '))
        while board.can_add_to(col) == False:
            print('Try again!')
            col = int(input('Enter a column: '))
        self.num_moves += 1
        return col
            










        
        
