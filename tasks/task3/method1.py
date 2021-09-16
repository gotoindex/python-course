import argparse
import math
import re


class Triangle:
    """A geometrical shape with three sides and a calculatable area.\n
    Note that each side should be smaller than the sum of other sides.
    ### Params:
    - a - a float lenght of the first side;
    - b - a float lenght of the second side;
    - c - a float lenght of the third side.
    """

    def __init__(self, name, a, b, c):
        self.name = name
        self.calculate_area(a, b, c)

    def calculate_area(self, a, b, c):
        """Calc or recalc the area of a triangle using Geron's method."""
        p = 0.5 * (a + b + c)
        self.area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    def __str__(self):
        return '[Triangle ' + self.name + ']: ' + '{:.2f}'.format(self.area) + ' cm'


class TriangleSorting:
    """The purpose of this class is to sort any amount of
    triangles by their area.\n
    After initialazing an object of this class you will be prompted to
    input a preferred amount of triangles before sorting.
    """

    def __init__(self, input_data):
        self.triangles = [Triangle(*t) for t in input_data]

    def sort(self):
        """Put triangles in order from the biggest area to the smallest."""
        self.triangles = sorted(self.triangles.copy(), key=lambda t: -t.area)

    def show(self):
        print('============= Triangles list: ===============')
        for i in range(len(self.triangles)):
            print(f'{i + 1}. ' + str(self.triangles[i]))


def input_triangles() -> list:
    triangles = []
    print(
        """Please enter a proper triangle info.
        - note, that each side should be shorter than the sum of other sides.
        - input format: <name>, <side1>, <side2>, <side3>"""
    )
    while True:
        cleaned_input = clean_input(input())
        if cleaned_input:
            if check_side_length(cleaned_input[1:]):
                triangles.append(cleaned_input)
                if input('Enter another triangle? ').lower()[0] != 'y':
                    break
            else:
                print('Please retry with proper lengths.')
        else:
            print('Please retry with a correct format.')
    return triangles


def clean_input(raw_input) -> tuple:
    """Filter out unwanted characters and split input into 4 values."""
    try:
        sub = re.sub(r'[^\w\,\.\-]', '', raw_input).lower().split(',')
        return (','.join(sub[:-3]), float(sub[-3]), float(sub[-2]), float(sub[-1]))
    except (ValueError, IndexError):
        return None


def check_side_length(sides) -> bool:
    """Figure out if a triangle can be built from the prompted sides."""
    for side in sides:
        if not ((sum(sides) - side) >= side >= 0):
            return False
    return True


if __name__ == '__main__':
    argparse.ArgumentParser(
        description='Sort triangles by area. You will be prompted to input any amount of triangles.'
        ).parse_args()
    ts = TriangleSorting(input_triangles())
    ts.sort()
    ts.show()
