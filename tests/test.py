import unittest
import json
import os
from tasks.task1.method1 import Chessboard
from tasks.task2.method1 import EnvelopeAnalysis
from tasks.task3.method1 import TriangleSorting
from tasks.task4.method1 import TextEditor
from tasks.task5.method1 import FormattedNumber
from tasks.task6.method1 import LuckyCounter
from tasks.task7.method1 import Sequence
from tasks.task8.method1 import Fibonacci


def load_cases(filename:str) -> list:
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, encoding='utf-8') as jfile:
        cases = json.load(jfile)['cases']
        jfile.close()
    return cases


class task1TestCase(unittest.TestCase):
    def testRegular(self):
        for case in load_cases('test1.json'):
            self.assertEqual(Chessboard(**case['input']).table, case['output'])

    def testExceptions(self):
        self.assertRaises(TypeError, Chessboard, width=8.5, height=8.5)


class MockEnvelopeAnalysis(EnvelopeAnalysis):
    def __init__(self, *args, **kwargs):
        self.result = []
        super().__init__(*args, **kwargs)

    def __output(self, result):
        if result:
            self.result.append(result)


class task2TestCase(unittest.TestCase):
    def testRegular(self):
        for case in load_cases('test2.json'):
            l = MockEnvelopeAnalysis(**case['input'])
            l.analyse()
            for i in range(len(l.result)):
                self.assertEqual(l.result[i], case['output'][i])

    def testExceptions(self):
        self.assertRaises(TypeError, MockEnvelopeAnalysis, w1="8", h1=8, w2=8, h2=8)


class task3TestCase(unittest.TestCase):
    def testRegular(self):
        for case in load_cases('test3.json'):
            ts = TriangleSorting(**case['input'])
            ts.sort()
            for i in range(len(ts.triangles)):
                self.assertEqual(str(ts.triangles[i]), case['output'][i])

    def testExceptions(self):
        self.assertRaises(TypeError, TriangleSorting, input_data="triangles")


class task4TestCase(unittest.TestCase):
    def testRegular(self):
        for case in load_cases('test4.json'):
            text_editor = TextEditor(case['input']['text'])
            o = text_editor.count_occurances(case['input']['count'])
            text_editor.replace(*case['input']['replace'])
            self.assertEqual(o, case['output']['count'])
            self.assertEqual(text_editor.text, case['output']['text'])

    def testExceptions(self):
        text_editor = TextEditor(text=-1)
        self.assertRaises(TypeError, text_editor.count_occurances, sub=-1)
        self.assertRaises(TypeError, text_editor.replace, sub1=-1, sub2=-1)


class task5TestCase(unittest.TestCase):
    def testRegular(self):
        for case in load_cases('test5.json'):
            self.assertEqual(str(FormattedNumber(**case['input'])), case['output'])

    def testExceptions(self):
        self.assertRaises(TypeError, FormattedNumber, number="", language=1)


class task6TestCase(unittest.TestCase):
    def testRegular(self):
        for case in load_cases('test6.json'):
            lc = LuckyCounter(**case['input'])
            print(lc.tickets)
            self.assertEqual(lc.count_moscow(), case['output']['moscow'])
            self.assertEqual(lc.count_piter(), case['output']['piter'])

    def testExceptions(self):
        lc = LuckyCounter(ticket_list=1)
        self.assertRaises(TypeError, lc.count_moscow)
        self.assertRaises(TypeError, lc.count_piter)


class task7TestCase(unittest.TestCase):
    def testRegular(self):
        for case in load_cases('test7.json'):
            self.assertEqual(str(Sequence(**case['input'])), case['output'])

    def testExceptions(self):
        self.assertRaises(TypeError, Sequence, n="")
        self.assertRaises(ValueError, Sequence, n=-10)


class task8TestCase(unittest.TestCase):
    def testRegular(self):
        for case in load_cases('test8.json'):
            self.assertEqual(str(Fibonacci(**case['input'])), case['output'])

    def testExceptions(self):
        self.assertRaises(TypeError, Fibonacci, a="", b=1)


if __name__ == '__main__':
        unittest.main()
