import unittest
import grid_operations as go


class TestGrid(unittest.TestCase):

    def test_extract_bits(self):
        # bin(15) = '0b1111'
        self.assertEqual(go.extract_bits(15, 0, 0), 0)
        self.assertEqual(go.extract_bits(15, 0, 1), 1)
        self.assertEqual(go.extract_bits(15, 0, 2), 3)
        self.assertEqual(go.extract_bits(15, 0, 3), 7)
        self.assertEqual(go.extract_bits(15, 0, 4), 15)

        self.assertEqual(go.extract_bits(15, 4, 4), 0)
        self.assertEqual(go.extract_bits(15, 3, 4), 1)
        self.assertEqual(go.extract_bits(15, 2, 4), 3)
        self.assertEqual(go.extract_bits(15, 1, 4), 7)

        # bin(42) = '0b101010'
        self.assertEqual(go.extract_bits(42, 0, 0), 0)
        self.assertEqual(go.extract_bits(42, 0, 1), 0)
        self.assertEqual(go.extract_bits(42, 0, 2), 2)

        self.assertEqual(go.extract_bits(42, 1, 0), 0)
        self.assertEqual(go.extract_bits(42, 1, 1), 1)
        self.assertEqual(go.extract_bits(42, 1, 2), 1)
        self.assertEqual(go.extract_bits(42, 1, 3), 5)

    def test_set_bits(self):
        self.assertEqual(go.set_bits(0, 3, 0, 0), 0)
        self.assertEqual(go.set_bits(0, 3, 0, 1), 1)
        self.assertEqual(go.set_bits(0, 3, 1, 1), 2)
        self.assertEqual(go.set_bits(0, 3, 0, 2), 3)
        self.assertEqual(go.set_bits(0, 3, 2, 2), 12)

        self.assertEqual(go.set_bits(10, 2, 0, 0), 10)
        self.assertEqual(go.set_bits(10, 2, 0, 2), 10)
        self.assertEqual(go.set_bits(10, 2, 1, 2), 12)
        self.assertEqual(go.set_bits(10, 2, 1, 4), 4)

    def test_row_left_2x2(self):
        self.assertEqual(go.row_left(27, 2, 2, 1), 75, 'solved 2x2 top row left')
        self.assertEqual(go.row_left(27, 2, 2, 2), 30, 'solved 2x2 bottom row left')
        self.assertEqual(go.row_left(30, 2, 2, 2), 27, 'mixed into solved bottom row left')

    def test_row_left_2x3(self):
        self.assertEqual(go.row_left(5349, 2, 3, 1), 41189, 'solved 2x3 top row left')
        self.assertEqual(go.row_left(41189, 2, 3, 2), 41259, 'mixed 2x3 bottom row left')
        self.assertEqual(go.row_left(5468, 2, 3, 2), 5349, 'mixed into solved 2x3 bottom row left')

    def test_row_left_3x2(self):
        self.assertEqual(go.row_left(5349, 3, 2, 1), 34021, 'solved 3x2 top row left')
        self.assertEqual(go.row_left(34021, 3, 2, 1), 5349, 'mixed into solved 3x2 top row left')
        self.assertEqual(go.row_left(5349, 3, 2, 2), 5797, 'solved 3x2 middle row left')
        self.assertEqual(go.row_left(5349, 3, 2, 3), 5356, 'solved 3x2 bottom row left')

    def test_row_left_3x3(self):
        self.assertEqual(go.row_left(305419896, 3, 3, 1), 4835268216, 'solved 3x3 top row left')
        self.assertEqual(go.row_left(305419896, 3, 3, 2), 306525816, 'solved 3x3 middle row left')
        self.assertEqual(go.row_left(305420391, 3, 3, 3), 305419896, 'mixed into solved bottom row left')

    def test_row_right_2x2(self):
        self.assertEqual(go.row_right(27, 2, 2, 1), 75, 'solved 2x2 top row right')
        self.assertEqual(go.row_right(27, 2, 2, 2), 30, 'solved 2x2 bottom row right')
        self.assertEqual(go.row_right(30, 2, 2, 2), 27, 'mixed into solved bottom row right')

    def test_row_right_2x3(self):
        self.assertEqual(go.row_right(5349, 2, 3, 1), 66277, 'solved 2x3 top row right')
        self.assertEqual(go.row_right(41189, 2, 3, 1), 5349, 'mixed into solved 2x3 top row right')
        self.assertEqual(go.row_right(5349, 2, 3, 2), 5468, 'solved 2x3 bottom row right')

    def test_row_right_3x2(self):
        self.assertEqual(go.row_right(5349, 3, 2, 1), 34021, 'solved 3x2 top row right')
        self.assertEqual(go.row_right(34021, 3, 2, 1), 5349, 'mixed into solved 3x2 top row right')
        self.assertEqual(go.row_right(5349, 3, 2, 2), 5797, 'solved 3x2 middle row right')
        self.assertEqual(go.row_right(5349, 3, 2, 3), 5356, 'solved 3x2 bottom row right')

    def test_row_right_3x3(self):
        self.assertEqual(go.row_right(305419896, 3, 3, 1), 8610141816, 'solved 3x3 top row right')
        self.assertEqual(go.row_right(306525816, 3, 3, 2), 305419896, 'mixed into solved 3x3 middle row right')
        self.assertEqual(go.row_right(305419896, 3, 3, 3), 305420391, 'solved 3x3 bottom row right')

    def test_col_up_2x2(self):
        self.assertEqual(go.col_up(27, 2, 2, 1), 147, 'solved 2x2 left column up')
        self.assertEqual(go.col_up(27, 2, 2, 2), 57, 'solved 2x2 right column up')
        self.assertEqual(go.col_up(57, 2, 2, 2), 27, 'mixed into solved 2x2 right column up')

    def test_col_up_2x3(self):
        self.assertEqual(go.col_up(5349, 2, 3, 1), 103461, 'solved 2x3 left column up')
        self.assertEqual(go.col_up(5349, 2, 3, 2), 17613, 'solved 2x3 middle column up')
        self.assertEqual(go.col_up(6882, 2, 3, 3), 5349, 'mixed into solved 2x3, right column up')

    def test_col_up_3x2(self):
        self.assertEqual(go.col_up(5349, 3, 2, 1), 71877, 'solved 3x2 left column up')
        self.assertEqual(go.col_up(5349, 3, 2, 2), 13665, 'solved 3x2 right column up')
        self.assertEqual(go.col_up(135381, 3, 2, 1), 5349, 'mixed into solved 3x2 left column up')

    def test_col_up_3x3(self):
        self.assertEqual(go.col_up(305419896, 3, 3, 1), 13193465976, 'solved 3x3 left column up')
        self.assertEqual(go.col_up(1915835976, 3, 3, 2), 305419896, 'mixed 3x3 into solved middle column up')
        self.assertEqual(go.col_up(305419896, 3, 3, 3), 355763826, 'solved 3x3 right column up')

    def test_col_down_2x2(self):
        self.assertEqual(go.col_down(27, 2, 2, 1), 147, 'solved 2x2 left column down')
        self.assertEqual(go.col_down(27, 2, 2, 2), 57, 'solved 2x2 right column down')
        self.assertEqual(go.col_down(57, 2, 2, 2), 27, 'mixed into solved 2x2 right column down')

    def test_col_down_2x3(self):
        self.assertEqual(go.col_down(5349, 2, 3, 1), 103461, 'solved 2x3 left column down')
        self.assertEqual(go.col_down(5349, 2, 3, 2), 17613, 'solved 2x3 middle column down')
        self.assertEqual(go.col_down(6882, 2, 3, 3), 5349, 'mixed into solved 2x3, right column down')

    def test_col_down_3x2(self):
        self.assertEqual(go.col_down(5349, 3, 2, 1), 135381, 'solved 3x2 left column down')
        self.assertEqual(go.col_down(5349, 3, 2, 2), 21603, 'solved 3x2 right column down')
        self.assertEqual(go.col_down(13665, 3, 2, 2), 5349, 'mixed into solved 3x2 right column down')

    def test_col_down_3x3(self):
        self.assertEqual(go.col_down(305419896, 3, 3, 1), 26072077176, 'solved 3x3 left column down')
        self.assertEqual(go.col_down(305419896, 3, 3, 2), 1915835976, 'solved 3x3 middle column down')
        self.assertEqual(go.col_down(355763826, 3, 3, 3), 305419896, 'mixed into solved 3x3 right column down')

    def test_extract_store(self):
        self.assertEqual(go.extract_store(27, 2, 2), [[1, 2], [3, 4]])
        self.assertEqual(go.extract_store(5419, 2, 3), [[1, 2, 3], [5, 6, 4]])
        self.assertEqual(go.extract_store(135381, 3, 2), [[5, 2], [1, 4], [3, 6]])
        self.assertEqual(go.extract_store(306525816, 3, 3), [[1, 2, 3], [5, 6, 4], [7, 8, 9]])

    def test_compact_store(self):
        self.assertEqual(go.compact_store([[1, 2], [3, 4]]), 27)
        self.assertEqual(go.compact_store([[2, 1], [3, 4]]), 75)
        self.assertEqual(go.compact_store([[1, 2, 3], [4, 5, 6]]), 5349)
        self.assertEqual(go.compact_store([[2, 3, 1], [4, 5, 6]]), 41189)
        self.assertEqual(go.compact_store([[3, 2], [5, 4], [1, 6]]), 71877)
        self.assertEqual(go.compact_store([[1, 6], [3, 2], [5, 4]]), 21603)
        self.assertEqual(go.compact_store([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 305419896)
        self.assertEqual(go.compact_store([[2, 3, 1], [4, 5, 6], [7, 8, 9]]), 4835268216)

