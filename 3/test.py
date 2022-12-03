import unittest

from functions import identify_item, convert_item_to_priority

class TestSolution(unittest.TestCase):

    def test_identify_item(self):
        self.assertEqual(identify_item('vJrwpWtwJgWrhcsFMMfFFhFp'), 'p', "Should be p")
        self.assertEqual(identify_item('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'), 'L', "Should be L")
        self.assertEqual(identify_item('PmmdzqPrVvPwwTWBwg'), 'P', "Should be P")
        self.assertEqual(identify_item('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'), 'v', "Should be v")
        self.assertEqual(identify_item('ttgJtRGJQctTZtZT'), 't', "Should be t")
        self.assertEqual(identify_item('CrZsJsPPZsGzwwsLwLmpwMDw'), 's', "Should be s")

    def test_convert_item_to_priority(self):
        self.assertEqual(convert_item_to_priority('a'), 1, "Should be 1")
        self.assertEqual(convert_item_to_priority('z'), 26, "Should be 26")
        self.assertEqual(convert_item_to_priority('A'), 27, "Should be 27")
        self.assertEqual(convert_item_to_priority('Z'), 52, "Should be 52")
    
        

if __name__ == '__main__':
    unittest.main()