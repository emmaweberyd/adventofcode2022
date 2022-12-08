import unittest
from part1 import *

class TestSolution(unittest.TestCase):

    def test_nr_of_visible_trees(self):
        self.assertEqual(nr_of_visible_trees('example.txt'), 21)

    def test_is_an_edge(self):
        self.assertEqual(is_an_edge(0,4,(5,5)), True)
        self.assertEqual(is_an_edge(2,0,(5,5)), True)
        self.assertEqual(is_an_edge(4,2,(5,5)), True)
        self.assertEqual(is_an_edge(2,4,(5,5)), True)
        self.assertEqual(is_an_edge(2,2,(5,5)), False)

    def test_is_visible_from_an_edge(self):
        input = read_input('example.txt')
        map = read_map(input)
        self.assertEqual(is_visible_from_an_edge(1,1,map), True)
        self.assertEqual(is_visible_from_an_edge(1,2,map), True)
        self.assertEqual(is_visible_from_an_edge(1,3,map), False)
        self.assertEqual(is_visible_from_an_edge(2,1,map), True)
        self.assertEqual(is_visible_from_an_edge(2,2,map), False)
        self.assertEqual(is_visible_from_an_edge(2,3,map), True)
        self.assertEqual(is_visible_from_an_edge(3,1,map), False)
        self.assertEqual(is_visible_from_an_edge(3,2,map), True)
        self.assertEqual(is_visible_from_an_edge(3,3,map), False)



if __name__ == '__main__':
    unittest.main()