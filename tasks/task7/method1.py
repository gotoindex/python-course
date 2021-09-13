import argparse
import math


class Sequence:
    """Displays all natural numbers whose square is less than n.\n
    Any negative inputs will be converted into positive ones.
    ### Params:
    - n - a positive integer. The square of each number in 
    the result will be smaller than this number.
    """

    def __init__(self, n):
        max = math.sqrt(abs(n))
        print(', '.join(tuple(str(i) for i in range(1, math.ceil(max)))))


parser = argparse.ArgumentParser(description='Display all natural numbers \
                                              whose square is less than n.')
parser.add_argument('n', type=int,
                    help='a positive integer. The square of each number in \
                          the result will be smaller than this number')
args = parser.parse_args()
Sequence(args.n)
