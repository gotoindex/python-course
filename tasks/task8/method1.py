import argparse


class Fibonacci:
    """The purpose of this class is to print out
    all fibonacci numbers that are > min and < max.\n
    Any negative inputs will be converted into positive ones.
    ### Params:
    - min - an integer lower border of displayed numbers;
    - max - an integer upper border of displayed numbers.
    """

    def __init__(self, min, max):
        self.min = abs(min)
        self.max = abs(max)
        self.numbers = []  # holds all fib. numbers that are in minmax range
        self.find_numbers()
        self.show()

    def find_numbers(self, i=1, prev_i=1):
        if i < self.max:
            if i > self.min:
                self.numbers.append(str(i))
                if i == 1:
                    self.numbers.append(str(i))
            self.find_numbers(i + prev_i, i)

    def show(self):
        print(', '.join(self.numbers))


parser = argparse.ArgumentParser(description='Display Fibonacci sequence \
                                              numbers in a range.')
parser.add_argument('min', type=int,
                    help='an integer lower border of displayed numbers')
parser.add_argument('max', type=int,
                    help='an integer upper border of displayed numbers')
args = parser.parse_args()
Fibonacci(args.min, args.max)
