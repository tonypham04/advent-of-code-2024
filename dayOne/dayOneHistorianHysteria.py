def __populate_location_ids_from_file(file_name: str, separator: str) -> tuple[list[int], list[int]]:
    first_list_of_location_ids = []
    second_list_of_location_ids = []
    with open(file_name, 'r', encoding = 'utf-8') as file_handler:
        for line in file_handler:
            first_location_id, second_location_id = line.split(separator)
            first_list_of_location_ids.append(int(first_location_id))
            second_list_of_location_ids.append(int(second_location_id))
    return first_list_of_location_ids, second_list_of_location_ids

def __swap_positions(first_index: int, second_index: int, int_list: list[int]) -> None:
    temp = int_list[first_index]
    int_list[first_index] = int_list[second_index]
    int_list[second_index] = temp

def __sort_list_from_least_to_greatest(int_list: list[int]) -> None:
    for i in range(0, len(int_list)):
        for j in range(i + 1, len(int_list)):
            if int_list[i] > int_list[j]:
                __swap_positions(i, j, int_list)

def sum_list_differences(first_list: list[int], second_list: list[int]) -> int:
    # Sort the two list from least to greatest
    __sort_list_from_least_to_greatest(first_list)
    __sort_list_from_least_to_greatest(second_list)
    # Return the sum the differences of each pair
    sum = 0
    for i in range(0, len(first_list)):
        sum += abs(first_list[i] - second_list[i])
    return sum

def get_similarity_score(first_list: list[int], second_list: list[int]) -> int:
    # Get frequency of each value in second_list
    score = 0
    for value in first_list:
        frequency_count = second_list.count(value)
        score += value * frequency_count
    # return sum of value x frequency
    return score

def __run_part_one(file_name: str, separator: str) -> None:
    first_location_ids_list, second_location_ids_list = __populate_location_ids_from_file(file_name, separator)
    total_distance = sum_list_differences(first_location_ids_list, second_location_ids_list)
    print('What is the total distance between your list?')
    print(f'Answer: {total_distance}')

def __run_part_two(file_name: str, separator: str) -> None:
    first_location_ids_list, second_location_ids_list = __populate_location_ids_from_file(file_name, separator)
    similarity_score = get_similarity_score(first_location_ids_list, second_location_ids_list)
    print('What is their similarity score?')
    print(f'Answer: {similarity_score}')

def __run() -> None:
    part_number = int(input('Please enter the part number to run (1 or 2): '))
    file_name = input('Please enter the file name: ')
    separator = '   '
    if part_number == 1:
        __run_part_one(file_name, separator)
    else:
        __run_part_two(file_name, separator)

if __name__ == '__main__':
    __run()
