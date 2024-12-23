import unittest
from mullItOver import parse_corrupted_data_for_muls, sum_all_muls

class MullItOverTest(unittest.TestCase):
    def test_parse_corrupted_data_for_muls(self):
        # Arrange
        corrupted_data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
        expected_results = ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']

        # Act
        sut = parse_corrupted_data_for_muls(corrupted_data)

        # Assert
        self.assertEqual(len(sut), len(expected_results))
        for i in range(0, len(expected_results)):
            self.assertEqual(sut[i], expected_results[i])

    def test_sum_all_muls(self):
        # Arrange
        muls = ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']
        expected_sum = 161
        # Act
        sut = sum_all_muls(muls)
        # Assert
        self.assertEqual(sut, expected_sum)

if __name__ == '__main__':
    unittest.main()
