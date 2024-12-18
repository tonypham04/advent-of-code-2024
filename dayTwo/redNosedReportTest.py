from redNosedReport import get_num_safe_reports
from problemDampener import ProblemDampener
import unittest

class RedNosedReportTest(unittest.TestCase):
    def test_get_num_safe_reports(self):
        # Arrange
        reports = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]
        ]
        min_diff = 1
        max_diff = 3
        expected_num_safe_reports = 2
        # Act
        sut = get_num_safe_reports(reports, min_diff, max_diff)
        # Assert
        self.assertEqual(sut, expected_num_safe_reports)

    def test_get_num_safe_reports_with_problem_dampener(self):
        # Arrange
        reports = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]
        ]
        min_diff = 1
        max_diff = 3
        expected_num_safe_reports = 4
        num_tolerated_bad_levels = 1
        problem_dampener = ProblemDampener(num_tolerated_bad_levels)
        # Act
        sut = get_num_safe_reports(reports, min_diff, max_diff, problem_dampener)
        # Assert
        self.assertEqual(sut, expected_num_safe_reports)

if __name__ == '__main__':
    unittest.main()
