import unittest
from ceresSearch import get_count_of_word_in_word_search
from ceresSearch import get_count_of_word_horizontally

class CeresSearchTest(unittest.TestCase):

    def test_get_count_of_word_in_word_search(self):
        # Arrange
        word_search = [
            ('M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'),
            ('M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'),
            ('A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'),
            ('M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'),
            ('X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'),
            ('X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'),
            ('S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'),
            ('S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'),
            ('M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'),
            ('M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X')
        ]
        word_to_look_for = 'XMAS'
        expected_count = 18
        # Act
        sut = get_count_of_word_in_word_search(word_search, word_to_look_for)
        # Assert
        self.assertEqual(expected_count, sut)

    def test_get_count_of_word_horizontally(self):
        # Arrange
        row_of_letters = ('X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M')
        search_term = 'XMAS'
        expected_count = 2
        # Act
        sut = get_count_of_word_horizontally(row_of_letters, search_term)
        # Assert
        self.assertEqual(expected_count, sut)

if __name__ == '__main__':
    unittest.main()
