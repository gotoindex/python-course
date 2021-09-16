import argparse
import json
import os


class FormattedNumber:
    """Formats any integer into a readable form.
    ### Params:
    - number - a valid integer less than one undecillion;
    - words - a dict of words to use.
    """

    def __init__(self, number, words):
        self.raw_number = abs(number)
        self.negative = number < 0
        self.library = words
        self.result = None

    def format(self):
        if self.raw_number:
            self.result = [self.library['other'][2]] if self.negative else []
            self.split()
            self.fill_result()
        else:
            self.result = [self.library['ones'][0]]

    def split(self):
        self.chunks = "{:,}".format(self.raw_number).split(',')
        self.chunks[0] = "{:03}".format(int(self.chunks[0]))
    
    def fill_result(self):
        for i in range(len(self.chunks)):
            self.bake_hundreds(i)
            self.bake_tens(i)
            self.bake_ones(i)
            self.bake_thousands(i)
    
    def bake_hundreds(self, i):
        if (hundred := int(self.chunks[i][0])) != 0:
            self.result.append(self.library['hundreds'][hundred - 1])
    
    def bake_tens(self, i):
        if int(self.chunks[i][1:]) > 20:
            self.result.append(self.library['tens'][int(self.chunks[i][1]) - 2])
    
    def bake_ones(self, i):
        is_thousand = i == len(self.chunks) - 2
        amount = int(self.chunks[i][1:])
        if amount % 10 != 0 or amount == 10:
            if is_thousand and amount % 10 == 1 and amount != 11:
                self.result.append(self.library['other'][0])
            elif is_thousand and amount % 10 == 2 and amount != 12:
                self.result.append(self.library['other'][1])
            elif int(self.chunks[i][1:]) > 20:
                self.result.append(self.library['ones'][amount % 10])
            else:
                self.result.append(self.library['ones'][amount])
    
    def bake_thousands(self, i):
        offset = len(self.chunks) - i - 2
        amount = int(self.chunks[i][1:])
        if i != len(self.chunks) - 1:
            if amount == 1:
                self.result.append(self.library['milestones'][offset][0])
            elif amount % 10 > 4 or 4 < amount < 21 or amount % 10 == 0:
                self.result.append(self.library['milestones'][offset][2])
            else:
                self.result.append(self.library['milestones'][offset][1])
    
    def show(self):
        print(' '.join(self.result).capitalize())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Format an integer into a readable form.')
    parser.add_argument('number', type=int, help='a valid integer less than one undecillion')
    args = parser.parse_args()

    # loading the library of words
    with open(os.path.join(os.path.dirname(__file__), 'words_ru.json'), encoding='utf-8') as jfile:
        words = json.load(jfile)
        jfile.close()

    fn = FormattedNumber(args.number, words)
    fn.format()
    fn.show()
