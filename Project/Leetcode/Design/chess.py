'''
https://www.daniweb.com/programming/software-development/threads/416196/chess-in-python

   0 1 2 3 4 5 6 7
0  R N B K Q B N R
1  p p p p p p p p
2
3
4
5
6   p p p p p p p p
7   R N B K Q B N R
'''
class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [[1] * 8 for i in range(8)]
        return board

class piece(Board):
    def __init__(self, color, name):
        self.position = (0, 0)
        self.name = ''
        self.color = color
        self.board = self.create_board()

    def move(self, x, y):
        pass

    def isInBound(self, x, y):
        if x < 0 or x > 7 or y < 0 or y > 7: return False
        return True


class King(piece):
    def __init__(self, x, y, color):
        self.position = (x, y)
        self.name = 'K'
        self.color = color
        self.board[x][y] = self.name

    def move(self, x, y):
        pass

class Queen(piece):
    def __init__(self, x, y, color):
        self.position = (x, y)
        self.name = 'Q'
        self.color = color
        # self.board[x][y] = self.name

    def move(self, x, y):
        pass
class Rook(piece):
    def __init__(self):
        self.position = (x, y)
        self.name = 'Q'
    def move(self, x, y):
        pass
class Bishop(piece):
    def __init__(self):
        self.position = (x, y)
        self.name = 'Q'
    def move(self, x, y):
        pass

class Knight(piece):
    def __init__(self):
        self.position = (x, y)
        self.name = 'Q'
    def move(self, x, y):
        pass

class Pawns(piece):
    def __init__(self):
        self.position = (x, y)
        self.name = 'Q'
    def move(self, x, y):
        pass

class game:
    def __init__(self):
      pass
    def checkMate(self):
        pass
    def isCheck(self):
        pass

if __name__ == '__main__':
    chess_board = Board()

    # piece of player_1
    p1_Queen = Queen(1, 2, 'White')
    # p1_King = King()
    # p1_Knight_1 = Knight()
    # p1_Knight_2 = Knight()
    # p1_Pawn = Pawns()
    # p1_Bishop_1 = Bishop()
    # p1_Bishop_2 = Bishop()
    # p1_Rook_1 = Rook()
    # p1_Rook_2 = Rook()


    # Piece of player_2
    p2_Queen = Queen(1, 2, 'Black')
    # p2_Queen = Queen(5, 2)


    print(p1_Queen.color)
    print(p2_Queen.color)
    # print(p2_Queen.position)
    # print(chess_board.board)
