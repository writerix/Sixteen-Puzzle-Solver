import sys
import math
import grid_operations as go
from collections import deque, namedtuple


def extract_solution(instructions, rows, cols):
    instruction_size = math.ceil(math.log2((2 * (rows + cols)) + 1))
    steps = []
    r_pos = 0
    single_step = go.extract_bits(instructions, r_pos, instruction_size)
    while single_step != 0:
        steps.append(single_step)
        r_pos += instruction_size
        single_step = go.extract_bits(instructions, r_pos, instruction_size)
    return steps[::-1]


def search(solved_state, start_state, rows, cols):
    Node = namedtuple('Node', ('state', 'history'))
    next_node = Node(start_state, 0)
    puzzle_solved = False
    visited = set()
    visited.add(start_state)
    search = deque([next_node])

    instruction_size = math.ceil(math.log2((2 * (rows + cols)) + 1))

    while puzzle_solved is False:
        next_node = search.popleft()
        if next_node.state == solved_state:
            puzzle_solved = True
            break
        # generate new nodes to search
        for i in range(1, cols + 1):
            up_state = go.col_up(next_node.state, rows, cols, i)
            if up_state not in visited:
                visited.add(up_state)
                up_history = next_node.history << instruction_size
                up_history = up_history | i
                search.append(Node(up_state, up_history))

            down_state = go.col_down(next_node.state, rows, cols, i)
            if down_state not in visited:
                visited.add(down_state)
                down_history = next_node.history << instruction_size
                down_history = down_history | (cols + cols + rows + 1 - i)
                search.append(Node(down_state, down_history))

        for i in range(1, rows + 1):
            right_state = go.row_right(next_node.state, rows, cols, i)
            if right_state not in visited:
                visited.add(right_state)
                right_history = next_node.history << instruction_size
                right_history = right_history | (cols + i)
                search.append(Node(right_state, right_history))

            left_state = go.row_left(next_node.state, rows, cols, i)
            if left_state not in visited:
                visited.add(left_state)
                left_history = next_node.history << instruction_size
                left_history = left_history | (cols + cols + rows + rows + 1 - i)
                search.append(Node(left_state, left_history))

    return next_node.history


def play_solution(steps, rows, cols, state=None):
    if len(steps) == 0:
        print('Puzzle is already solved.')
    else:
        print('Starting position.')
    if state is not None:
        print(*go.extract_store(state, rows, cols), sep='\n')
    for step in steps:
        if step <= cols:
            print('Column {} up.'.format(step))
            if state is not None:
                state = go.col_up(state, rows, cols, step)
        elif step - cols <= rows:
            print('Row {} right.'.format(step - cols))
            if state is not None:
                state = go.row_right(state, rows, cols, step - cols)
        elif step - cols - rows <= cols:
            print('Column {} down'.format(cols + cols + rows + 1 - step))
            if state is not None:
                state = go.col_down(state, rows, cols, (cols + cols + rows + 1 - step))
        else:
            print('Row {} left.'.format(cols + cols + rows + rows + 1 - step))
            if state is not None:
                state = go.row_left(state, rows, cols, (cols + cols + rows + rows + 1 - step))
        if state is not None:
            print(*go.extract_store(state, rows, cols), sep='\n')


def chunk(original, chunk_size):
    """
    Yields lists composed of the original's items.
    """
    for i in range(0, len(original), chunk_size):
        yield original[i: i + chunk_size]


if __name__ == '__main__':
    row_size = int(sys.argv[1])  # size of rows == number of columns
    verbose = False
    if '-v' in sys.argv or '--verbose' in sys.argv:
        verbose = True
        tile_input = list(filter(lambda x: x not in ('-v', '--verbose'), sys.argv[2:]))
    else:
        tile_input = sys.argv[2:]
    tile_input = list(map(int, tile_input))
    tiles = list(chunk(tile_input, row_size))
    start_state = go.compact_store(tiles)
    solved_state = go.compact_store(list(chunk(sorted(tile_input), row_size)))
    try:
        solution = search(solved_state, start_state, len(tiles), row_size)
    except IndexError:
        sys.exit("No solution found.")
    steps = extract_solution(solution, len(tiles), row_size)
    if verbose:
        play_solution(steps, len(tiles), row_size, start_state)
    else:
        play_solution(steps, len(tiles), row_size)

