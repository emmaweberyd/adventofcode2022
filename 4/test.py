import unittest
from part1 import *

class TestSolution(unittest.TestCase):

    def test_do_assignments_fully_overlap(self):
        self.assertEqual(do_assignments_fully_overlap('2-4,6-8'), False, "Should be false")
        self.assertEqual(do_assignments_fully_overlap('2-3,4-5'), False, "Should be false")
        self.assertEqual(do_assignments_fully_overlap('5-7,7-9'), False, "Should be false")
        self.assertEqual(do_assignments_fully_overlap('2-8,3-7'), True, "Should be true")
        self.assertEqual(do_assignments_fully_overlap('6-6,4-6'), True, "Should be true")
        self.assertEqual(do_assignments_fully_overlap('2-6,4-8'), False, "Should be false")

if __name__ == '__main__':
    unittest.main()