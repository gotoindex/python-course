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
        self.calculate_area(abs(a), abs(b), abs(c))

    def calculate_area(self, a, b, c):
        p = 0.5 * (a + b + c)
        self.area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    def __str__(self):
        return 'Triangle ' + self.name + ' ' + str(self.area)


class TriangleSorting:
    """The purpose of this class is to sort any amount of
    triangles by their area.\n
    After initialazing an object of this class you will be prompted to
    input a preferred amount of triangles before sorting.
    """

    def __init__(self):
        self.triangles = []
        self.input()
        self.show()

    def input(self):
        raw_input = input(
            """Please enter a proper triangle info.
            - note, that each side should be shorter than the sum of other sides.
            - input format: <name>, <side1>, <side2>, <side3>\n"""
        )
        cleaned_input = None
        while not cleaned_input:
            cleaned_input = self.clean_input(raw_input)
            if cleaned_input:
                self.triangles.append(Triangle(*cleaned_input))
                if input('Enter another triangle? ') == 'y':
                    cleaned_input = None
                    raw_input = input()
            else:
                raw_input = input('Please retry with a correct format: ')

    def clean_input(self, raw_input):
        try:
            sub = (re.sub(r'[^\w\,\.]', '', raw_input)).split(',')
            return (','.join(sub[:-3]), float(sub[-3]), float(sub[-2]), float(sub[-1]))
        except (ValueError, IndexError):
            return None

    def sort(self):
        self.triangles = sorted(self.triangles.copy(), key=lambda t: t.area)

    def show(self):
        print('============= Triangles list: ===============')
        for i in range(len(self.triangles)):
            print(f'{i + 1}. ' + str(self.triangles[i]))


TriangleSorting()
