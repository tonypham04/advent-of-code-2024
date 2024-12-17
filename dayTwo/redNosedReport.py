def __is_adjacent_levels_diff_safe(level: int, adjacent_level: int, min_diff: int, max_diff: int) -> bool:
    diff = abs(level - adjacent_level)
    return diff >= min_diff and diff <= max_diff

def __is_report_safe(report: list[int], min_diff: int, max_diff: int) -> bool:
    isIncreasing = None
    for i in range(0, len(report) - 1):
        if report[i] > report[i + 1]:
            if isIncreasing != None and not isIncreasing:
                return False
            isIncreasing = True
        elif report[i] < report[i + 1]:
            if isIncreasing != None and isIncreasing:
                return False
            isIncreasing = False
        else:
            return False
        if not __is_adjacent_levels_diff_safe(report[i], report[i + 1], min_diff, max_diff):
            return False
    return True

def get_num_safe_reports(reports: list[list[int]], min_diff: int, max_diff: int) -> int:
    num_safe_reports = 0
    for report in reports:
        if __is_report_safe(report, min_diff, max_diff):
            num_safe_reports += 1
    return num_safe_reports

if __name__ == '__main__':
    pass
