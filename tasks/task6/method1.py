import argparse
import os


def get_tickets(path:str) -> list:
    fullpath = os.path.join(os.path.dirname(__file__), path)
    with open(fullpath) as txt:
        tickets = txt.readlines()
        txt.close()
    return tickets


class LuckyCounter:
    """This class counts lucky tickets through different methods.
    ### Params:
    - ticket_list - a list of 6-digit strings (tickets).
    """

    def __init__(self, ticket_list):
        self.tickets = ticket_list

    def count_moscow(self, counter:int=0) -> int:
        for ticket in self.tickets:
            if (sum(tuple(int(digit) for digit in ticket[:3])) ==
                sum(tuple(int(digit) for digit in ticket[3:6]))):
                counter += 1
        return counter

    def count_piter(self, counter:int=0) -> int:
        for ticket in self.tickets:
            if (sum(tuple(int(digit) for digit in ticket[0:6:2])) ==
                sum(tuple(int(digit) for digit in ticket[1:6:2]))):
                counter += 1
        return counter


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count lucky tickets.')
    parser.add_argument('path',
                        help='name of a .txt file filled with ticket numbers')
    parser.add_argument('-m', '--moscow', action='store_true',
                        help='use Moscow method to count lucky tickets')
    parser.add_argument('-p', '--piter', action='store_true',
                        help='use Piter method to count lucky tickets')
    args = parser.parse_args()

    lc = LuckyCounter(get_tickets(args.path))
    if args.moscow:
        print('Amount of lucky tickets (Moscow method):', lc.count_moscow())
    if args.piter:
        print('Amount of lucky tickets (Piter method):', lc.count_piter())
