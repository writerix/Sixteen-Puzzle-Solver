import math


def extract_bits(store, r_position, spread):
    extract = store >> r_position
    spread_mask = -1 << spread
    spread_mask = ~spread_mask
    return extract & spread_mask


def set_bits(store, bit_val, r_position, spread):
    """

    :param store: integer pre-manipulation
    :param bit_val: value of the bits to be set
    :param r_position: zero-based indexing position of the right-most bit impacted by the manipulation
    :param spread: how many bits are to be changed. Note: a spread of zero will result in return equal to input.
    :return: integer with bits set
    """
    spread_store_mask = (-1 << spread + r_position) | (1 << r_position) - 1
    store = store & spread_store_mask
    bit_val = bit_val & ((2**spread) - 1)# resize bit_val to fit in spread
    bit_val = bit_val << r_position
    store = store | bit_val
    return store

def row_left(store, rows, cols, row_num):
    """

    :param store: integer representing the state of the puzzle grid. Values are stored as one less than puzzle value.
    To extract the puzzle grid in list of list of integer form, see extract_store.
    :param rows: number of rows in the puzzle. One-based indexing.
    :param cols: number of columns in the puzzle. One-based indexing.
    :param row_num: the row number that is being rotated left. One-based indexing.
    :return: integer representing the puzzle grid after the row left rotation is completed.
    """
    bit_chunk_size = math.ceil(math.log2(rows * cols))
    row_value = extract_bits(store, (rows - row_num) * cols * bit_chunk_size, cols * bit_chunk_size)
    rotated_chunk = extract_bits(row_value, (cols - 1) * bit_chunk_size, bit_chunk_size)
    row_value = row_value << bit_chunk_size
    row_value = row_value | rotated_chunk
    return set_bits(store, row_value, (rows - row_num) * cols * bit_chunk_size, cols * bit_chunk_size)

def row_right(store, rows, cols, row_num):
    """

    :param store: integer representing the state of the puzzle grid. Values are stored as one less than puzzle value.
    To extract the puzzle grid in list of list of integer form, see extract_store.
    :param rows: number of rows in the puzzle. One-based indexing.
    :param cols: number of columns in the puzzle. One-based indexing.
    :param row_num: the row number that is being rotated left. One-based indexing.
    :return: integer representing the puzzle grid after the row right rotation is completed.
    """
    bit_chunk_size = math.ceil(math.log2(rows * cols))
    row_value = extract_bits(store, (rows - row_num) * cols * bit_chunk_size, cols * bit_chunk_size)
    rotated_chunk = extract_bits(row_value, 0, bit_chunk_size)
    row_value = row_value >> bit_chunk_size
    row_value = row_value | (rotated_chunk << (bit_chunk_size * (cols - 1)))
    return set_bits(store, row_value, (rows - row_num) * cols * bit_chunk_size, cols * bit_chunk_size)

def col_up(store, rows, cols, col_num):
    """

    :param store: integer representing the state of the puzzle grid. Values are stored as one less than puzzle value.
    To extract the puzzle grid in list of list of integer form, see extract_store.
    :param rows: number of rows in the puzzle. One-based indexing.
    :param cols: number of columns in the puzzle. One-based indexing.
    :param col_num: the column number that is being rotated up. One-based indexing.
    :return: integer representing the puzzle grid after the column up rotation is completed.
    """
    bit_chunk_size = math.ceil(math.log2(rows * cols))
    # extract and save column's top value that will become the bottom value
    future_bottom_chunk = extract_bits(store, ((rows * cols) - col_num) * bit_chunk_size, bit_chunk_size)

    for i in range(rows - 1):
        chunk = extract_bits(store, (((rows - i - 1) * cols) - col_num) * bit_chunk_size, bit_chunk_size)
        store = set_bits(store, chunk, (((rows - i) * cols) - col_num) * bit_chunk_size, bit_chunk_size)

    store = set_bits(store, future_bottom_chunk, (cols - col_num) * bit_chunk_size, bit_chunk_size)
    return store

def col_down(store, rows, cols, col_num):
    """

    :param store: integer representing the state of the puzzle grid. Values are stored as one less than puzzle value.
    To extract the puzzle grid in list of list of integer form, see extract_store.
    :param rows: number of rows in the puzzle. One-based indexing.
    :param cols: number of columns in the puzzle. One-based indexing.
    :param col_num: the column number that is being rotated down. One-based indexing.
    :return: integer representing the puzzle grid after the column down rotation is completed.
    """
    bit_chunk_size = math.ceil(math.log2(rows * cols))
    # extract and save column's bottom value that will become the top value
    future_top_chunk = extract_bits(store, (cols - col_num) * bit_chunk_size, bit_chunk_size)

    for i in range(rows - 1):
        chunk = extract_bits(store, (((i + 1) * cols) + cols - col_num) * bit_chunk_size, bit_chunk_size)
        store = set_bits(store, chunk, ((i * cols) + cols - col_num) * bit_chunk_size, bit_chunk_size)

    store = set_bits(store, future_top_chunk, ((rows * cols) - col_num) * bit_chunk_size, bit_chunk_size)
    return store


def extract_store(store, rows, cols):
    """
    :param store: integer representing the state of the puzzle grid. Values are stored as one less than puzzle value.
    :param rows: number of rows in the puzzle. One-based indexing.
    :param cols: cols: number of columns in the puzzle. One-based indexing.
    :return: list of list of integers representing the state of the puzzle grid.
    """
    max_val = rows * cols
    bit_chunk_size = math.ceil(math.log2(max_val))
    extract = []
    r_offset = ((rows * cols) - 1) * bit_chunk_size
    for i in range(rows):
        extract.append([])
        for j in range(cols):
            extract[i].append(extract_bits(store, r_offset, bit_chunk_size) + 1)
            r_offset -= bit_chunk_size
    return extract

def compact_store(values):
    """
    :param values: list of list of integers
    :return: integer compactly representing the input values
    """
    store = 0
    max_val = len(values) * len(values[0])
    bit_chunk_size = math.ceil(math.log2(max_val))
    for value in values:
        for num in value:
            store = store << bit_chunk_size
            store = store | (num - 1)
    return store


