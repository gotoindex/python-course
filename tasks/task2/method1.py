import argparse


class Envelope:
    """An envelope than can be rotated by 90 degrees and back.\n
    Any negative inputs will be converted into positive ones.
    ### Params:
    - width - a float width of the envelope;
    - height - a float height of the envelope.
    """

    def __init__(self, width, height):
        self.width = abs(width)
        self.height = abs(height)
        self.rotated = False

    def rotate(self):
        tmp = self.width
        self.width = self.height
        self.height = tmp
        self.rotated = not self.rotated

    def fits_into(self, other):
        return other.width > self.width and other.height > self.height


class EnvelopeAnalysis:
    """The purpose of this class is to compare two envelopes
    by their size and whether one can fit into another or not.
    ### Params:
    - w1 - a float width of the first envelope;
    - h1 - a float height of the first envelope;
    - w2 - a float width of the second envelope;
    - h2 - a float height of the second envelope.
    """

    def __init__(self, w1, h1, w2, h2):
        self.first = Envelope(w1, h1)
        self.second = Envelope(w2, h2)
        self.analyse()

    def analyse(self):
        self.try_fitting()
        self.second.rotate()
        self.try_fitting()

    def try_fitting(self):
        if self.first.fits_into(self.second):
            if self.first.rotated or self.second.rotated:
                print('After rotation ', end='')
            print('First envelope fits into Second one.')
        if self.second.fits_into(self.first):
            if self.first.rotated or self.second.rotated:
                print('After rotation ', end='')
            print('Second envelope fits into First one.')


parser = argparse.ArgumentParser(description='Check if envelopes fit into each other.')
parser.add_argument('a', type=float,
                    help='a float width of the first envelope')
parser.add_argument('b', type=float,
                    help='a float height of the first envelope')
parser.add_argument('c', type=float,
                    help='a float width of the second envelope')
parser.add_argument('d', type=float,
                    help='a float height of the second envelope')
args = parser.parse_args()
EnvelopeAnalysis(args.a, args.b, args.c, args.d)
