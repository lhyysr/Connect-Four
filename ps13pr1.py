##ps13pr1.py - problem set 13, problem 1
##
##name: Haoyuan Liu
##email: lhyysr@bu.edu

class Board:

    # 1-constructor
    def __init__(self, height, width):
        '''constructs a new Board object'''
        self.height = height
        self.width = width
        self.slots = [[' '] * width for n in range(height)]

    # 2-str metod
    def __str__(self):
        '''returns a str representing a Board object'''
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'    # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'   # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        s += '-' * (self.width * 2 + 1) + '\n'

        # and the numbers underneath it.
        for col in range(self.width):
            num = col % 10
            s += ' ' + str(num)
        s += '\n'
        
        return s

    # 3-method
    def __repr__(self):
        '''returns a string representing the called Board object. '''
        return str(self)

    # 4-method
    def add_checker(self, checker, col):
        '''returns a Board with the new checker in it
           inputs: Checker represented by 'X' or 'O'
                   col an int
        '''
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)

        row = 0
        while row< self.height and self.slots[row][col] == ' ':
            row += 1
        row -= 1
        self.slots[row][col] = checker

    # 5-method
    def clear(self):
        '''clear the Board object'''
        self.slots = [[' '] * self.width for n in range(self.height)]   

    # 6-method
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'    

    # 7-method
    def can_add_to(self, col):
        ''' returns True if it is valid to place a checker in the column col,
            Otherwise, it should return False.
            input: int
        '''
        if col in range(self.width) and self.slots[0][col] == ' ':
            return True
        else:
            return False

    # 8-method
    def is_full(self):
        '''returns True if the called Board object is completely full,
            returns False otherwise.
        '''
        for col in range(self.width):
            if self.can_add_to(col):
                return False
        return True

    # 9-method
    def remove_checker(self, col):
        '''removes the top checker from column col of the called Board object.
           input: int
        '''
        assert(col >= 0 and col < self.width)

        row = 0
        while row< self.height and self.slots[row][col] == ' ':
            row += 1
        if row != self.height:
            self.slots[row][col] = ' '

    # 10-method
    def is_win_for(self, checker):
        '''returns True if there are four consecutive slots containing checker,
           Otherwise, it should return False.
           input: 'X' or 'O' as checker
        '''
        assert(checker == 'X' or checker == 'O')

        # call the helper functions and use their return values to
        # determine whether to return True or False
        if self.is_horizontal_win(checker) or \
           self.is_vertical_win(checker) or \
           self.is_down_diagonal_win(checker) or \
           self.is_up_diagonal_win(checker):
            return True
        return False
    

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

                # if we make it here, there were no horizontal wins
        return False


    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False


    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width -3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False
    

    def is_up_diagonal_win(self, checker):
        ''' Checks for a up diagonal win for the specified checker
        '''
        for row in range(self.height - 3):
            for col in range(4, self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col - 1] == checker and \
                   self.slots[row + 2][col - 2] == checker and \
                   self.slots[row + 3][col - 3] == checker:
                    return True
        return False










