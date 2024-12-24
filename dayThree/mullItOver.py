import re

def parse_corrupted_data_for_muls(corrupted_data: str) -> tuple[str]:
    pattern = r'(mul\(\d+,\d+\))'
    return re.findall(pattern, corrupted_data)

def parse_corrpupted_data_for_muls_with_new_instructions(corrupted_data: str) -> tuple[str]:
    pattern_for_dont_do_instructions = r"don't\(\).*?mul\(\d+,\d+\).*?do\(\)"
    data_without_dont_do_instructions = re.sub(pattern_for_dont_do_instructions, 'do()', corrupted_data, flags = re.DOTALL)
    pattern_for_remaining_dont_instructions = r"don't\(\).*mul\(\d+,\d+\).*"
    data_without_any_dont_instructions = re.sub(pattern_for_remaining_dont_instructions, '', data_without_dont_do_instructions, flags = re.DOTALL)
    return parse_corrupted_data_for_muls(data_without_any_dont_instructions)

def sum_all_muls(muls: tuple[str]) -> int:
    sum = 0
    pattern_for_any_int = r'\d+'
    for mul in muls:
        xy = re.findall(pattern_for_any_int, mul)
        sum += int(xy[0]) * int(xy[1])
    return sum

def __obtain_data_from_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as file_handler:
        return file_handler.read()

def __run():
    part_num = 0
    muls = []
    while part_num not in range(1, 3):
        part_num = int(input('Please enter the part you would like to run: '))
    filename = input('Please enter the file name: ')
    data = __obtain_data_from_file(filename)
    if part_num == 1:
        muls = parse_corrupted_data_for_muls(data)
    else:
        muls = parse_corrpupted_data_for_muls_with_new_instructions(data)
    result = sum_all_muls(muls)
    print('What do you get if you add up all of the results of the multiplications?')
    print(f'Answer: {result}')

if __name__ == '__main__':
    __run()
