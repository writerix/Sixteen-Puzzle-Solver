import unittest
import io
import contextlib
import solver

class TestNode(unittest.TestCase):
    def setUp(self):
        self.scrambled_tiles = solver.Node([[1,2,3,16],[5,6,7,4],[9,10,11,8],[13,14,15,12]], ['Starting position.'])
        self.ordered_tiles = solver.Node([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], ['Starting position.', 'Column 4 up.'])
        
        solver.solved = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
    
    #flat_state
    def test_flat_scrambled(self):
        self.assertEqual(self.scrambled_tiles.flat_state(), (1,2,3,16,5,6,7,4,9,10,11,8,13,14,15,12))
    
    def test_flat_ordered(self):
        self.assertEqual(self.ordered_tiles.flat_state(), (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
    
    def test_flat_llon(self):
        self.assertEqual(self.scrambled_tiles.flat_state([[5,6,7,8],[9,10,11,12],[13,14,15,16],[1,2,3,4]]), (5,6,7,8,9,10,11,12,13,14,15,16,1,2,3,4))
    
    #is_solved
    def test_solved_scrambled(self):
        self.assertFalse(self.scrambled_tiles.is_solved())
    
    def test_solved_ordered(self):
        self.assertTrue(self.ordered_tiles.is_solved())
    
    #gen_next_nodes
    def test_gen_next_nodes(self):
        self.scrambled_tiles.gen_next_nodes()
        self.assertEqual(len(solver.visited), len(self.scrambled_tiles.flat_state()), 'n*n next states == n*n tiles')

class TestHelperFunctions(unittest.TestCase):
    def test_chunk(self):
        self.assertEqual(list(solver.chunk([1,2,3], 1)), [[1],[2],[3]])
        self.assertEqual(list(solver.chunk([1,2,3,4], 2)), [[1,2],[3,4]])
        self.assertEqual(list(solver.chunk([1,2,3], 3)), [[1,2,3]])
    
    def test_play_solution(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            solver.play_solution([[1,2],[3,4]])
        self.assertEqual(stdout.getvalue(), '[1, 2]\n[3, 4]\n')
        
        stdout.truncate(0)
        stdout.seek(0)
        with contextlib.redirect_stdout(stdout):
            solver.play_solution([[1,4],[3,2]], ['Starting position.', 'Column 2 down.'])
        self.assertEqual(stdout.getvalue(), 'Starting position.\n[1, 4]\n[3, 2]\nColumn 2 down.\n[1, 2]\n[3, 4]\n')

if __name__ == '__main__':
    unittest.main()