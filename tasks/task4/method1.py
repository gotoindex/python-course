import argparse
import os


class TextEditor:
    """The purpose of this class is to analyse and manipulate
    a piece of multiline text.
    ### Params:
    - path - name of a .txt file filled with text.
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

    def replace(self, sub1:str, sub2:str):
        for i in range(len(self.text)):
            self.text[i] = self.text[i].replace(sub1, sub2)

    def save(self, fullpath):
        with open(fullpath, 'w') as txt:
            for line in self.text:
                txt.write(line)
            txt.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count or replace substrs in a file.')
    parser.add_argument('path',
                        help='name of a .txt file filled with text')
    parser.add_argument('--count',
                        help='a substring to search for')
    parser.add_argument('--replace', nargs=2,
                        help='replace all substr1 with substr2')
    args = parser.parse_args()

    fullpath = os.path.join(os.path.dirname(__file__), args.path)
    with open(fullpath) as txt:
        text = txt.readlines()
        txt.close()

    text_editor = TextEditor(text)
    if args.count:
        c = text_editor.count_occurances(args.count)
        print(f'The substring "{args.count}" appears in {args.path} {c} time(s).')
    if args.replace:
        text_editor.replace(*args.replace)
        text_editor.save(fullpath)
        print(f'Successfully replaced {args.replace[0]} with {args.replace[1]}!')
