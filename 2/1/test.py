import unittest

from functions import get_shape, shape_score, is_draw, is_win, round_score

class TestSolution(unittest.TestCase):

    def test_get_shape(self):
        self.assertEqual(get_shape('A'), 'Rock', "Should be Rock")
        self.assertEqual(get_shape('B'), 'Paper', "Should be Paper")
        self.assertEqual(get_shape('C'), 'Scissors', "Should be Scissors")
        self.assertEqual(get_shape('X'), 'Rock', "Should be Rock")
        self.assertEqual(get_shape('Y'), 'Paper', "Should be Paper")
        self.assertEqual(get_shape('Z'), 'Scissors', "Should be Scissors")

    def test_shape_score(self):
        self.assertEqual(shape_score('X'), 1, "Should be 1")
        self.assertEqual(shape_score('Y'), 2, "Should be 2")
        self.assertEqual(shape_score('Z'), 3, "Should be 3")

    def test_is_draw(self):
        self.assertEqual(is_draw('Rock','Rock'), True, "Should be true")
        self.assertEqual(is_draw('Paper','Paper'), True, "Should be true")
        self.assertEqual(is_draw('Scissors','Scissors'), True, "Should be true")

        self.assertEqual(is_draw('Rock','Paper'), False, "Should be false")
        self.assertEqual(is_draw('Rock','Scissors'), False, "Should be false")

        self.assertEqual(is_draw('Paper','Rock'), False, "Should be false")
        self.assertEqual(is_draw('Paper','Scissors'), False, "Should be false")

        self.assertEqual(is_draw('Scissors','Rock'), False, "Should be false")
        self.assertEqual(is_draw('Scissors','Paper'), False, "Should be false")
    
    def test_is_win(self):
        self.assertEqual(is_win('Rock','Rock'), False, "Should be false")
        self.assertEqual(is_win('Rock','Paper'), True, "Should be true")
        self.assertEqual(is_win('Rock','Scissors'), False, "Should be false")

        self.assertEqual(is_win('Paper','Rock'), False, "Should be false")
        self.assertEqual(is_win('Paper','Paper'), False, "Should be false")
        self.assertEqual(is_win('Paper','Scissors'), True, "Should be true")

        self.assertEqual(is_win('Scissors','Rock'), True, "Should be true")
        self.assertEqual(is_win('Scissors','Paper'), False, "Should be false")
        self.assertEqual(is_win('Scissors','Scissors'), False, "Should be false")

    def test_round_score(self):
        self.assertEqual(round_score('A', 'Y'), 8, "Should be 8")
        self.assertEqual(round_score('B', 'X'), 1, "Should be 1")
        self.assertEqual(round_score('C', 'Z'), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()