import unittest
from dayOneHistorianHysteria import sum_list_differences, get_similarity_score

class DayOneHistorianHysteriaTest(unittest.TestCase):
    def test_sum_list_differences(self):
        # Arrange
        first_location_id_list = [3, 4, 2, 1, 3, 3]
        second_location_id_list = [4, 3, 5, 3, 9, 3]
        expected_sum = 11
        # Act
        sut = sum_list_differences(first_location_id_list, second_location_id_list)
        # Assert
        self.assertEqual(sut, expected_sum)

    def test_get_similarity_score(self):
        # Arrange
        first_location_id_list = [3, 4, 2, 1, 3, 3]
        second_location_id_list = [4, 3, 5, 3, 9, 3]
        expected_similarity_score = 31
        # Act
        sut = get_similarity_score(first_location_id_list, second_location_id_list)
        # Assert
        self.assertEqual(sut, expected_similarity_score)

if __name__ == '__main__':
    unittest.main()
