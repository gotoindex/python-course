import argparse
import os


STR_COUNT = 'The substring "{}" appears in {} {} time(s).'
STR_REPLACE = 'Successfully replaced {} with {}!'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Count or replace substrs in a file.')
    parser.add_argument('path',
                        help='name of a .txt file filled with text')
    parser.add_argument('--count',
                        help='a substring to search for')
    parser.add_argument('--replace', nargs=2,
                        help='replace all substr1 with substr2')
    return parser.parse_args()


class TextEditor:
    """The purpose of this class is to analyse and manipulate
    a piece of multiline text.
    ### Params:
    - text - a list of strings to work with.
    """

    def __init__(self, text:list):
        self.text = text
    
    def __str__(self):
        return ''.join(self.text)

    def count_occurances(self, sub:str, counter:int=0, start:int=0) -> int:
        """Custom counting method instead of count() to account for overlaps."""
        start = str(self).find(sub, start) + 1
        if start > 0:
            return self.count_occurances(sub, counter + 1, start)
        else:
            return counter

    def replace(self, sub1:str, sub2:str) -> list:
        for i in range(len(self.text)):
            self.text[i] = self.text[i].replace(sub1, sub2)
        return self.text


class TextFileManager:
    """The purpose of this class is to load/save the content of a .txt file.
    ### Params:
    - fullpath - a full path to the file to load content from.
    """

    def __init__(self, fullpath:str):
        self.fullpath = fullpath
        self.text = []

    def load(self) -> list:
        with open(self.fullpath) as txt:
            self.text = txt.readlines()
            txt.close()
        return self.text

    def save(self, text:list=None):
        with open(self.fullpath, 'w') as txt:
            for line in text or self.text:
                txt.write(line)
            txt.close()


if __name__ == '__main__':
    args = parse_args()

    f = TextFileManager(os.path.join(os.path.dirname(__file__), args.path))

    text_editor = TextEditor(f.load())
    if args.count:
        c = text_editor.count_occurances(args.count)
        print(STR_COUNT.format(args.count, args.path, c))
    if args.replace:
        f.save(text_editor.replace(*args.replace))
        print(STR_REPLACE.format(args.replace[0], args.replace[1]))
