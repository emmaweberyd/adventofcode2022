import unittest
from functions import *

class TestSolution(unittest.TestCase):

    def test_nr_of_chars_after_4_unique_chars(self):
        self.assertEqual(nr_of_chars_after_x_unique_chars('bvwbjplbgvbhsrlpgdmjqwftvncz', 4), 5)
        self.assertEqual(nr_of_chars_after_x_unique_chars('nppdvjthqldpwncqszvftbrmjlhg', 4), 6)
        self.assertEqual(nr_of_chars_after_x_unique_chars('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4), 10)
        self.assertEqual(nr_of_chars_after_x_unique_chars('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4), 11)

    def test_nr_of_chars_after_14_unique_chars(self):
        self.assertEqual(nr_of_chars_after_x_unique_chars('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14), 19)
        self.assertEqual(nr_of_chars_after_x_unique_chars('bvwbjplbgvbhsrlpgdmjqwftvncz', 14), 23)
        self.assertEqual(nr_of_chars_after_x_unique_chars('nppdvjthqldpwncqszvftbrmjlhg', 14), 23)
        self.assertEqual(nr_of_chars_after_x_unique_chars('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14), 29)
        self.assertEqual(nr_of_chars_after_x_unique_chars('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14), 26)

if __name__ == '__main__':
    unittest.main()