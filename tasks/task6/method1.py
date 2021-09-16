import argparse
import os


def get_tickets(path:str) -> list:
    fullpath = os.path.join(os.path.dirname(__file__), path)
    with open(fullpath) as txt:
        tickets = txt.readlines()
        txt.close()
    return tickets


def count_moscow(tickets:list, counter:int=0) -> int:
    for ticket in tickets:
        if (sum(tuple(int(digit) for digit in ticket[:3])) ==
            sum(tuple(int(digit) for digit in ticket[3:6]))):
            counter += 1
    return counter


def count_piter(tickets:list, counter:int=0) -> int:
    for ticket in tickets:
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

    tickets = get_tickets(args.path)
    if args.moscow:
        print('Amount of lucky tickets (Moscow method):', count_moscow(tickets))
    if args.piter:
        print('Amount of lucky tickets (Piter method):', count_piter(tickets))
