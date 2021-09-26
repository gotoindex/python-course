import argparse


class Envelope:
    """An envelope than can be rotated by 90 degrees and back.\n
    Any negative inputs will be converted into positive ones.
    ### Params:
    - width - a float width of the envelope;
    - height - a float height of the envelope.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rotated = False

    def rotate(self):
        """Turn the envelope 90 degrees or reverse back."""
        tmp = self.width
        self.width = self.height
        self.height = tmp
        self.rotated = not self.rotated

    def fits_into(self, other) -> bool:
        """Check if this envelope fits into another."""
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
        self.first = Envelope(abs(w1), abs(h1))
        self.second = Envelope(abs(w2), abs(h2))

    def analyse(self):
        """Try to fit envelopes into each other and and print out results."""
        self.__try_fitting()
        self.second.rotate()
        self.__try_fitting()

    def __try_fitting(self):
        result = ''
        if self.first.fits_into(self.second):
            if self.first.rotated or self.second.rotated:
                result += 'After rotation '
            result += 'First envelope fits into Second one.'
        if self.second.fits_into(self.first):
            if self.first.rotated or self.second.rotated:
                result += 'After rotation '
            result += 'Second envelope fits into First one.'
        self.__output(result)
    
    def __output(self, result):
        print(result)


if __name__ == '__main__':
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
    EnvelopeAnalysis(args.a, args.b, args.c, args.d).analyse()
