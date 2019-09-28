import unittest
import rotations

class TestRotations(unittest.TestCase):
    #rotate_row
    def test_rotate_row(self):
        self.assertEqual(rotations.rotate_row([], 1), [], 'Rotations shouldn\'t change an empty list.')
        self.assertEqual(rotations.rotate_row([3], -1), [3], 'Rotations shouldn\'t change a single item list.')
        self.assertEqual(rotations.rotate_row([1,2,3], 0), [1,2,3], 'Rotation by zero shouldn\'t change a list.')
    
        self.assertEqual(rotations.rotate_row([1,2,3], -1), [2,3,1])
        self.assertEqual(rotations.rotate_row([1,2], -5), [2,1])
        self.assertEqual(rotations.rotate_row((1,2), -5), (2,1))
        
        self.assertEqual(rotations.rotate_row([1,2,3,4], 1), [4,1,2,3])
        self.assertEqual(rotations.rotate_row([1,2,3], 5), [2,3,1])
        self.assertEqual(rotations.rotate_row('123', 5), '231')

    #row_right
    def test_row_right(self):
        self.assertEqual(rotations.row_right([[1]], 0), [[1]])
        self.assertEqual(rotations.row_right([[1,2],[3,4]], 1), [[1,2],[4,3]])
        self.assertEqual(rotations.row_right([[1,2,3],[4,5,6],[7,8,9]], 2), [[1,2,3],[4,5,6],[9,7,8]])
    
    #row_left
    def test_row_left(self):
        self.assertEqual(rotations.row_left([[1]], 0), [[1]])
        self.assertEqual(rotations.row_left([[1,2],[3,4]], 1), [[1,2],[4,3]])
        self.assertEqual(rotations.row_left([[1,2,3],[4,5,6],[7,8,9]], 2), [[1,2,3],[4,5,6],[8,9,7]])
    
    #col_up
    def test_col_up(self):
        self.assertEqual(rotations.col_up([[]], 0), [[]])
        self.assertEqual(rotations.col_up([[1]], 0), [[1]])
        self.assertEqual(rotations.col_up([[1,2],[3,4]], 1), [[1,4],[3,2]])
        self.assertEqual(rotations.col_up([[1,2,3],[4,5,6],[7,8,9]], 2), [[1,2,6],[4,5,9],[7,8,3]])
    
    #col_down
    def test_col_down(self):
        self.assertEqual(rotations.col_down([[]], 0), [[]])
        self.assertEqual(rotations.col_down([[1]], 0), [[1]])
        self.assertEqual(rotations.col_down([[1,2],[3,4]], 1), [[1,4],[3,2]])
        self.assertEqual(rotations.col_down([[1,2,3],[4,5,6],[7,8,9]], 2), [[1,2,9],[4,5,3],[7,8,6]])

if __name__ == '__main__':
    unittest.main()