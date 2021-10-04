import argparse


class Fibonacci:
    """The purpose of this class is to print out
    all fibonacci numbers that are > min and < max.\n
    Any negative inputs will be converted into positive ones.
    ### Params:
    - min - an integer lower border of displayed numbers;
    - max - an integer upper border of displayed numbers.
    """

    def __init__(self, a:int, b:int):
        self.min = min(a, b)
        self.max = max(a, b)
        self.numbers = []  # holds all fib. numbers that are in minmax range
        self.find_numbers_in_range()

    def find_numbers_in_range(self, i=1, prev_i=0):
        if i < self.max:
            if i > self.min:
                if prev_i == 0 and prev_i > self.min:
                    self.numbers.append('0')
                self.numbers.append(str(i))
            self.find_numbers_in_range(i + prev_i, i)

    def __str__(self):
        return ', '.join(self.numbers)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display Fibonacci sequence \
                                                  numbers in a range.')
    parser.add_argument('min', type=int,
                        help='an integer lower border of displayed numbers')
    parser.add_argument('max', type=int,
                        help='an integer upper border of displayed numbers')
    args = parser.parse_args()
    print(Fibonacci(args.min, args.max))
