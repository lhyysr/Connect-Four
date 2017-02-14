#
# ps14pr1.py (Problem Set 14, Problem 1)
#
# An AI Player for Connect Four
#
# name: Haoyuan
# email: lhyysr@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from ps13pr3 import *
import random

# 1 class header
class AIPlayer(Player):

    # 2 constructor
    def __init__(self, checker, tiebreak, lookahead):
        '''inherit attributes form Player, and two new attributes'''
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        Player.__init__(self, checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    # 3 method
    def __str__(self):
        '''that returns a string representing an AIPlayer object'''
        s = Player.__str__(self) + ' (' + str(self.tiebreak) + ', ' + \
            str(self.lookahead) + ')'
        return s

    # 4 method
    def max_score_column(self, scores):
        '''returns the index of the column with the maximum score.
           input: a list of scores
        '''
        m = max(scores)
        lst_of_i = []
        for i in range(len(scores)):
            if scores[i] == m:
                lst_of_i += [i]

        if self.tiebreak == 'LEFT':
            i = lst_of_i[0]
        elif self.tiebreak == 'RIGHT':
            i = lst_of_i[-1]
        else:
            i = random.choice(lst_of_i)
        return i

    # 5 method
    def scores_for(self, board):
        '''return a list containing one score for each column.
           input: a Board
        '''
        scores = [50] * board.width
        for col in range(board.width):
            # a
            if board.can_add_to(col) == False:
                scores[col] = -1
            # b
            elif board.is_win_for(self.checker):
                scores[col] = 100
            # c
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            # d
            elif self.lookahead == 0:
                scores[col] = 50
            # e
            else:
                board.add_checker(self.checker, col) # i
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, \
                               self.lookahead - 1)         # ii
                opp_scores = opp.scores_for(board)
                scores[col] = 100 - max(opp_scores)
                board.remove_checker(col)
        return scores   
    
    # 6 method
    def next_move(self, board):
        '''return the called AIPlayer‘s judgment of its best possible move.
           input: a Board
        '''
        scores = self.scores_for(board)
        col = self.max_score_column(scores)
        self.num_moves += 1
        return col       













        
