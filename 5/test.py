import unittest
from part1 import *

class TestSolution(unittest.TestCase):

    def test_create_stacks(self):
        illustration, _ = split_input(read_input('example.txt'))
        self.assertEqual(create_stacks(illustration), [['Z','N'], ['M', 'C', 'D'], ['P']])

    def test_main(self):
        self.assertEqual(main('example.txt'), 'CMZ')


if __name__ == '__main__':
    unittest.main()