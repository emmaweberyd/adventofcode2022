import unittest
from functions import *

class TestSolution(unittest.TestCase):

    def test_assignments_fully_overlap(self):
        self.assertEqual(assignments_fully_overlap('2-4,6-8'), False, "Should be false")
        self.assertEqual(assignments_fully_overlap('2-3,4-5'), False, "Should be false")
        self.assertEqual(assignments_fully_overlap('5-7,7-9'), False, "Should be false")
        self.assertEqual(assignments_fully_overlap('2-8,3-7'), True, "Should be true")
        self.assertEqual(assignments_fully_overlap('6-6,4-6'), True, "Should be true")
        self.assertEqual(assignments_fully_overlap('2-6,4-8'), False, "Should be false")

    def test_assignments_overlap(self):
        self.assertEqual(assignments_overlap('2-4,6-8'), False, "Should be false")
        self.assertEqual(assignments_overlap('2-3,4-5'), False, "Should be false")
        self.assertEqual(assignments_overlap('5-7,7-9'), True, "Should be true")
        self.assertEqual(assignments_overlap('2-8,3-7'), True, "Should be true")
        self.assertEqual(assignments_overlap('6-6,4-6'), True, "Should be true")
        self.assertEqual(assignments_overlap('2-6,4-8'), True, "Should be true")

if __name__ == '__main__':
    unittest.main()