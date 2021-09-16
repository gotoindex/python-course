import argparse
import os


class TextEditor:
    """The purpose of this class is to analyse and manipulate
    a piece of multiline text.
    ### Params:
    - path - name of a .txt file filled with text.
    """

    def __init__(self, path):
        self.path = path
        self.fullpath = os.path.join(os.path.dirname(__file__), path)
        with open(self.fullpath) as txt:
            self.text = txt.readlines()
            self.string = ''.join(self.text)
            txt.close()

    def show_occurances(self, sub:str):
        result = self.count_occurances(sub)
        print(f'The substring "{sub}" appears in {self.path} {result} time(s).')

    def count_occurances(self, sub:str, counter:int=0, start:int=0) -> int:
        """Custom counting method instead of count() to account for overlaps."""
        start = self.string.find(sub, start) + 1
        if start > 0:
            return self.count_occurances(sub, counter + 1, start)
        else:
            return counter

    def replace(self, sub1:str, sub2:str):
        with open(self.fullpath, 'w') as txt:
            for line in self.text:
                txt.write(line.replace(sub1, sub2))
            txt.close()
            print(f'Successfully replaced {sub1} with {sub2} in {self.path}!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count or replace substrs in a file.')
    parser.add_argument('path',
                        help='name of a .txt file filled with text')
    parser.add_argument('--count',
                        help='a substring to search for')
    parser.add_argument('--replace', nargs=2,
                        help='replace all substr1 with substr2')
    args = parser.parse_args()
    text_editor = TextEditor(args.path)
    if args.count:
        text_editor.show_occurances(args.count)
    if args.replace:
        text_editor.replace(*args.replace)
