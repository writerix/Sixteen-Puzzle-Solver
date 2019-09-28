import itertools
from collections import deque

import sys

import rotations

visited = set()
search = deque([])


class Node:
    """
    Represents a node in the search for solution to nxn puzzle.
    """
    def __init__(self, state, history):
        self.state = state
        self.history = history

    def flat_state(self, llon=None):
        if llon is None:
            llon = self.state
        return tuple(itertools.chain.from_iterable(llon))

    def gen_next_nodes(self):
        for i in range(len(self.state)):
            #column down
            cd_llon = rotations.col_down(self.state, i)
            if self.flat_state(cd_llon) not in visited:
                visited.add(self.flat_state(cd_llon))
                copy_history = self.history[:]
                copy_history.append('Column {} down.'.format(i + 1))
                search.append(Node(cd_llon, copy_history))
            
            #column up
            cu_llon = rotations.col_up(self.state, i)
            if self.flat_state(cu_llon) not in visited:
                visited.add(self.flat_state(cu_llon))
                copy_history = self.history[:]
                copy_history.append('Column {} up.'.format(i + 1))
                search.append(Node(cu_llon, copy_history))

            #row right
            rr_llon = rotations.row_right(self.state, i)
            if self.flat_state(rr_llon) not in visited:
                visited.add(self.flat_state(rr_llon))
                copy_history = self.history[:]
                copy_history.append('Row {} right.'.format(i + 1))
                search.append(Node(rr_llon, copy_history))

            #row left
            rl_llon = rotations.row_left(self.state, i)
            if self.flat_state(rl_llon) not in visited:
                visited.add(self.flat_state(rl_llon))
                copy_history = self.history[:]
                copy_history.append('Row {} left.'.format(i + 1))
                search.append(Node(rl_llon, copy_history))
                
    def is_solved(self):
        return self.flat_state(self.state) == solved
    
    def __repr__(self):
        return repr((self.state, self.history))

        
def chunk(original, chunk_size):
    """
    Yields lists composed of the original's items.
    """
    for i in range(0, len(original), chunk_size):
        yield original[i: i + chunk_size]

def play_solution(matrix, moves=None):
    if moves is None:
        print(*matrix, sep='\n')
    else:
        for step in moves:
            if step != 'Starting position.':
                components = step.split()
                if components[0] == 'Row' and components[2] == 'left.':
                    matrix = rotations.row_left(matrix, int(components[1]) - 1)
                elif components[0] == 'Row' and components[2] == 'right.':
                    matrix = rotations.row_right(matrix, int(components[1]) - 1)
                elif components[0] == 'Column' and components[2] == 'up.':
                    matrix = rotations.col_up(matrix, int(components[1]) - 1)
                else:
                    matrix = rotations.col_down(matrix, int(components[1]) - 1)
            print(step)
            print(*matrix, sep='\n')
                    

if __name__ == '__main__':
    row_size = int(sys.argv[1])#size of rows == number of columns
    verbose = False
    if '-v' in sys.argv or '--verbose' in sys.argv[1:]:
        verbose = True
        tiles = list(filter(lambda x: x not in ('-v', '--verbose'), sys.argv[2:]))
    else:
        tiles = sys.argv[2:]
    solved = tuple(sorted(map(int, tiles)))
    start = Node(list(chunk(list(map(int, tiles)), row_size)), ['Starting position.'])
    
    if start.is_solved():
        if verbose:
            play_solution(start.state)
        print('Puzzle is already solved.')
    else:
        visited.add(start.flat_state())
        start.gen_next_nodes()
        next_node = search.popleft()
        while next_node.is_solved() is False:
            next_node.gen_next_nodes()
            next_node = search.popleft()
        if verbose:
            play_solution(start.state, next_node.history)
        else:
            print(*next_node.history, sep='\n')
