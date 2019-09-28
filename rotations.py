from copy import deepcopy

#Functions to perform horizontal and vertical rotations
#on lists (1D rows) and lists of lists (2D matrices)


def rotate_row(row, amount):
    """Rotates a list, tuple, string, or other sliceable
    by a specified amount. A negative amount rotates left,
    positive amount to the right.
    
    Note: for empty list or single item lists
    rotation doesn't change the list.
    """
    if len(row) <= 1:
        return row
    amount *= -1
    if amount >= 0:
        amount = amount % len(row)
    else:
        amount = amount % (-1 * len(row))
    return row[amount:] + row[:amount]


def row_right(matrix, row_num):
    copy_matrix = deepcopy(matrix)
    copy_matrix[row_num] = rotate_row(copy_matrix[row_num], 1)
    return copy_matrix


def row_left(matrix, row_num):
    copy_matrix = deepcopy(matrix)
    copy_matrix[row_num] = rotate_row(copy_matrix[row_num], -1)
    return copy_matrix


def col_up(matrix, col_num):
    copy_matrix = deepcopy(matrix)
    #empty list or single row
    #doesn't change with col_numumn rotation
    if len(copy_matrix) <= 1:
        return copy_matrix
    bottom_val = copy_matrix[0][col_num]

    for i in range(len(copy_matrix) - 1):
        copy_matrix[i][col_num] = copy_matrix[i + 1][col_num]
    copy_matrix[-1][col_num] = bottom_val
    return copy_matrix


def col_down(matrix, col_num):
    copy_matrix = deepcopy(matrix)
    #empty list or single row
    #doesn't change with col_numumn rotation
    if len(copy_matrix) <= 1:
        return copy_matrix
    top_val = copy_matrix[-1][col_num]

    for i in range(len(copy_matrix) - 1, 0, -1):
        copy_matrix[i][col_num] = copy_matrix[i - 1][col_num]
    copy_matrix[0][col_num] = top_val
    return copy_matrix
