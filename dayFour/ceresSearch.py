def __get_count_of_word_in_row(row_of_letters: tuple[str], letters_in_search_term: list[str]) -> int:
    index_of_interest = 0
    index_of_found_letter = None
    count = 0
    for i in range(len(row_of_letters)):
        # Check if letter corresponds to the first letter
        # If yes, increment next index of interest
        # Account for fact that letters need to be found sequentially
        if row_of_letters[i] == letters_in_search_term[index_of_interest]:
            if index_of_found_letter == None:
                index_of_found_letter = i
            if index_of_found_letter == i or index_of_found_letter == i - 1:
                index_of_interest += 1
                index_of_found_letter += 1
            if index_of_interest == len(letters_in_search_term) - 1:
                count += 1
                index_of_interest = 0
                index_of_found_letter = None
    return count

def get_count_of_word_horizontally(row_of_letters: tuple[str], search_term: str) -> int:
    letters_in_search_term = list(search_term)
    reversed_letters_in_search_term = letters_in_search_term.copy()
    reversed_letters_in_search_term.reverse()
    count = __get_count_of_word_in_row(row_of_letters, letters_in_search_term)
    count += __get_count_of_word_in_row(row_of_letters, reversed_letters_in_search_term)
    return count

def get_column_of_letters_from_word_search(word_search: list[tuple[str]], column_index: int) -> list[str]:
    if column_index > len(word_search) - 1:
        raise IndexError
    column_of_letters = []
    for i in range(len(word_search)):
        column_of_letters.append(word_search[i][column_index])
    return column_of_letters

def get_count_of_word_in_word_search(word_search: list[tuple[str]], search_term: str) -> int:
    pass
