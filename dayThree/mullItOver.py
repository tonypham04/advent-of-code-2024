import re

def parse_corrupted_data_for_muls(corrupted_data: str) -> tuple[str]:
    pattern = r'(mul\(\d+,\d+\))'
    return re.findall(pattern, corrupted_data)

def sum_all_muls(muls: list[str]) -> int:
    pass
