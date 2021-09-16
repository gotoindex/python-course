import argparse


class Chessboard:
    """The purpose of this class is to print out
    a table of symbols imitating a chessboard.\n
    Any negative inputs will be converted into positive ones.
    ### Params:
    - width - an integer amount of columns of the chessboard;
    - height - an integer amount of rows of the chessboard.
    """

    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.odd_line = ''.join(tuple('█░' for i in range(int(self.width / 2))))
        if self.width % 2 != 0:
            self.odd_line = self.odd_line + '█'
        self.even_line = '░' + self.odd_line[:-1]

    def show(self):
        for i in range(int(self.height / 2)):
            print(self.odd_line)
            print(self.even_line)
        if self.height % 2 != 0:
            print(self.odd_line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display a custom-sized chessboard.')
    parser.add_argument('height', type=int,
                        help='an integer amount of rows of the chessboard')
    parser.add_argument('width', type=int,
                        help='an integer amount of columns of the chessboard')
    args = parser.parse_args()
    Chessboard(abs(args.width), abs(args.height)).show()
