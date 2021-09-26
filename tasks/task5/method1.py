import argparse
import json
import os


def load_words(language:str) -> dict:
    path = os.path.join(os.path.dirname(__file__), f'words_{language}.json')
    with open(path, encoding='utf-8') as jfile:
        words = json.load(jfile)
        jfile.close()
    return words


class FormattedNumber:
    """Formats any integer into a readable form.
    ### Params:
    - number - a valid integer less than one undecillion;
    - language - a [ru/ua/en] str to determine which library to use.
    """

    def __init__(self, number:int, language:str):
        self.raw_number = abs(number)
        self.negative = number < 0
        self.library = load_words(language)
        self.result = []

    @property
    def formatted_number(self) -> str:
        """Text representation of the number, lowercase."""
        if self.raw_number:
            self.result = [self.library['other'][2]] if self.negative else []
            self.__split()
            self.__fill_result()
        else:
            self.result = [self.library['ones'][0]]
        return ' '.join(self.result)

    def __split(self):
        self.chunks = "{:,}".format(self.raw_number).split(',')
        self.chunks[0] = "{:03}".format(int(self.chunks[0]))

    def __fill_result(self):
        for i in range(len(self.chunks)):
            self.__bake_hundreds(i)
            self.__bake_tens(i)
            self.__bake_ones(i)
            self.__bake_thousands(i)

    def __bake_hundreds(self, i):
        if (hundred := int(self.chunks[i][0])) != 0:
            self.result.append(self.library['hundreds'][hundred - 1])

    def __bake_tens(self, i):
        if int(self.chunks[i][1:]) > 20:
            self.result.append(self.library['tens'][int(self.chunks[i][1]) - 2])

    def __bake_ones(self, i):
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

    def __bake_thousands(self, i):
        offset = len(self.chunks) - i - 2
        amount = int(self.chunks[i][1:])
        if i != len(self.chunks) - 1:
            if amount == 1:
                self.result.append(self.library['milestones'][offset][0])
            elif amount % 10 > 4 or 4 < amount < 21 or amount % 10 == 0:
                self.result.append(self.library['milestones'][offset][2])
            else:
                self.result.append(self.library['milestones'][offset][1])

    def __str__(self):
        return self.formatted_number.capitalize()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Format an integer into a readable form.')
    parser.add_argument('number', type=int, help='a valid integer less than one undecillion')
    parser.add_argument('-l', choices=('ru', 'ua', 'en',), default='ru',
                        help='a language to display the number in')
    args = parser.parse_args()

    print(FormattedNumber(args.number, args.l))
