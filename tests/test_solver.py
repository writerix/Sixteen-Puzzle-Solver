import unittest
import io
import contextlib
from solver import chunk, extract_solution, search, play_solution


class MyTestCase(unittest.TestCase):
    def test_chunk(self):
        self.assertEqual(list(chunk([1, 2, 3], 1)), [[1], [2], [3]])
        self.assertEqual(list(chunk([1, 2, 3, 4], 2)), [[1, 2], [3, 4]])
        self.assertEqual(list(chunk([1, 2, 3], 3)), [[1, 2, 3]])

    def test_extract_instructions_2x2(self):
        self.assertEqual(extract_solution(0, 2, 2), [], 'solved 2x2')
        self.assertEqual(extract_solution(3, 2, 2), [3], 'mixed single step 2x2')
        self.assertEqual(extract_solution(50, 2, 2), [3, 2], 'mixed multi step 2x2')
        self.assertEqual(extract_solution(322, 2, 2), [1, 4, 2], 'mixed multi step 2x2')

    def test_extract_instructions_2x3(self):
        self.assertEqual(extract_solution(0, 2, 3), [], 'solved 2x3')
        self.assertEqual(extract_solution(4, 2, 3), [4], 'mixed single step 2x3')
        self.assertEqual(extract_solution(402, 2, 3), [1, 9, 2], 'mixed multi step 2x3')
        self.assertEqual(extract_solution(267316, 2, 3), [4, 1, 4, 3, 4], 'mixed multi step 2x3')

    def test_extract_instructions_3x2(self):
        self.assertEqual(extract_solution(0, 3, 2), [], 'solved 3x2')
        self.assertEqual(extract_solution(5, 3, 2), [5], 'mixed single step 3x2')
        self.assertEqual(extract_solution(1139, 3, 2), [4, 7, 3], 'solved 3x2')
        self.assertEqual(extract_solution(29522, 3, 2), [7, 3, 5, 2], 'mixed multi step 3x2')

    def test_extract_instructions_3x3(self):
        self.assertEqual(extract_solution(0, 3, 3), [], 'solved 3x3')
        self.assertEqual(extract_solution(1, 3, 3), [1], 'mixed single step 3x3')
        self.assertEqual(extract_solution(29899403, 3, 3), [1, 12, 8, 3, 10, 8, 11], 'mixed multi step 3x3')
        self.assertEqual(extract_solution(23180844, 3, 3), [1, 6, 1, 11, 6, 2, 12], 'mixed multi step 3x3')

    def test_search_2x2(self):
        self.assertEqual(search(27, 27, 2, 2), 0, 'solved 2x2')
        self.assertIn(search(27, 147, 2, 2), (1, 6), 'left column up or down')

    def test_search_2x3(self):
        self.assertEqual(search(5349, 5349, 2, 3), 0, 'solved 2x3')
        self.assertEqual(search(5349, 41189, 2, 3), 4, 'top row right 2x3')

    def test_search_3x2(self):
        self.assertEqual(search(5349, 5349, 3, 2), 0, 'solved 3x2')
        self.assertEqual(search(5349, 13665, 3, 2), 6, 'right column down 3x2')

    def test_search_3x3(self):
        self.assertEqual(search(305419896, 305419896, 3, 3), 0, 'solved 3x3')
        self.assertEqual(search(305419896, 13193465976, 3, 3), 9, 'left column down 3x3')

    def test_play_solution(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            play_solution([], 2, 2)
        self.assertEqual(stdout.getvalue(), 'Puzzle is already solved.\n')

        stdout.truncate(0)
        stdout.seek(0)
        with contextlib.redirect_stdout(stdout):
            play_solution([2], 2, 2, 57)
        self.assertEqual(stdout.getvalue(), 'Starting position.\n[1, 4]\n[3, 2]\nColumn 2 up.\n[1, 2]\n[3, 4]\n')
