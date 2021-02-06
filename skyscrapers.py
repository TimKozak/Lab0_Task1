"""
Tim Kozak, UCU IT&BA, Lab0
GitHub link: https://github.com/TimKozak/Lab0_Task1.git
"""


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
    """
    output_list = []
    with open(path, encoding="utf-8", mode="r") as board:
        for line in board:
            line = line.strip("\n")
            output_list.append(line)

    return output_list


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint
    is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    counter = 0
    tracker = 0

    for digit in input_line[1:-1]:
        num = int(digit)

        if num > tracker:
            counter += 1
            tracker = num

    if counter == pivot:
        return True

    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?'
    present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', \
    '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', \
    '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board:
        if "?" in line:
            return False

    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', \
    '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:-1]
    for line in board:

        line = line[1:-1]

        for num in line:
            if line.count(num) > 1:
                return False

    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    board = board[1:-1]

    for line in board:

        if line[-1] != "*":
            check_line = line[::-1]
            pivot = int(check_line[0])
            if not left_to_right_check(check_line, pivot):
                return False

        if line[0] != "*":
            check_line = line
            pivot = int(check_line[0])
            if not left_to_right_check(check_line, pivot):
                return False

    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness
    (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in
    one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', \
    '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', \
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412453*', '423145*', \
    '*542315', '*35214*', '*41532*', '*2*1***'])
    False
    """
    inverted_board = []
    inverted_string = ""

    for idx in range(len(board)):
        for string in board:
            inverted_string += string[idx]

        inverted_board.append(inverted_string)
        inverted_string = ""

    output = check_horizontal_visibility(
        inverted_board) and check_uniqueness_in_rows(inverted_board)

    return output


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    board = read_input(input_path)
    if check_not_finished_board(board) and \
            check_uniqueness_in_rows(board) and \
            check_horizontal_visibility(board) and \
            check_columns(board):

        return True

    return False


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
