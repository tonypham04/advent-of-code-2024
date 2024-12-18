class ProblemDampener:
    def __init__(self, num_tolerated_bad_levels):
        self.num_tolerated_bad_levels = num_tolerated_bad_levels
        self.num_bad_levels = 0

    def increment_num_bad_levels(self):
        self.num_bad_levels += 1

    def is_report_still_safe(self):
        return self.num_bad_levels <= self.num_tolerated_bad_levels
