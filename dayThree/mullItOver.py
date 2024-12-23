import re

def parse_corrupted_data_for_muls(corrupted_data: str) -> tuple[str]:
    pattern = r'(mul\(\d+,\d+\))'
    return re.findall(pattern, corrupted_data)

def sum_all_muls(muls: list[str]) -> int:
    sum = 0
    pattern_for_any_int = r'\d+'
    for mul in muls:
        xy = re.findall(pattern_for_any_int, mul)
        sum += int(xy[0]) * int(xy[1])
    return sum
