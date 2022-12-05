import unittest
from functions import split_input
from part1 import *
from part2 import *

class TestSolution(unittest.TestCase):

    def test_create_stacks(self):
        illustration, _ = split_input(read_input('example.txt'))
        self.assertEqual(create_stacks(illustration), [['Z','N'], ['M', 'C', 'D'], ['P']])

    def test_crate_mover_9000(self):
        self.assertEqual(crate_mover_9000('example.txt'), 'CMZ')

    def test_crate_mover_9001(self):
        self.assertEqual(crate_mover_9001('example.txt'), 'MCD')


if __name__ == '__main__':
    unittest.main()