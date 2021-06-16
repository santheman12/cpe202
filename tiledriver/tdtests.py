# Name:         San Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Tile Driver
# Term:         Winter 2021

import unittest

import tiledriver
from tiledriver import PuzzleState as PS  # only allowed use of from ... import


class TestMakeAdjacent(unittest.TestCase):

    def test_make_adjacent_1(self):
        state = PS((3, 2, 1, 0), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((3, 0, 1, 2), "J"), PS((3, 2, 0, 1), "L")])

    def test_make_adjacent_2(self):
        state = PS((2, 3, 1, 0), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((2, 0, 1, 3), "J"), PS((2, 3, 0, 1), "L")])

    def test_make_adjacent_3(self):
        state = PS((3, 1, 2, 0), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((3, 0, 2, 1), "J"), PS((3, 1, 0, 2), "L")])

    def test_make_adjacent_4(self):
        state = PS((3, 1, 0, 2), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((3, 1, 2, 0), "H"), PS((0, 1, 3, 2), "J")])

    def test_make_adjacent_5(self):
        state = PS((3, 0, 1, 2), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((3, 2, 1, 0), "K"), PS((0, 3, 1, 2), "L")])


class TestRightCol(unittest.TestCase):
    def test_r_col_1(self):
        state = PS((3, 2, 1, 0), "")
        self.assertEqual(tiledriver.r_col(state, 3),
                         [PS((3, 0, 1, 2), "J"), PS((3, 2, 0, 1), "L")])

    def test_r_col_2(self):
        state = PS((2, 3, 1, 0), "")
        self.assertEqual(tiledriver.r_col(state, 3),
                         [PS((2, 0, 1, 3), "J"), PS((2, 3, 0, 1), "L")])

    def test_r_col_3(self):
        state = PS((3, 1, 2, 0), "")
        self.assertEqual(tiledriver.r_col(state, 3),
                         [PS((3, 0, 2, 1), "J"), PS((3, 1, 0, 2), "L")])

    def test_r_col_4(self):
        state = PS((3, 2, 0, 1), "")
        self.assertEqual(tiledriver.r_col(state, 2),
                         [PS((0, 2, 3, 1), "J"), PS((3, 0, 2, 1), "L")])

    def test_r_col_5(self):
        state = PS((3, 0, 1, 2), "")
        self.assertEqual(tiledriver.r_col(state, 1),
                         [PS((3, 2, 1, 0), "K"), PS((0, 3, 1, 2), "L")])


class TestLeftCol(unittest.TestCase):
    def test_l_col_1(self):
        state = PS((0, 1, 3, 2), "")
        self.assertEqual(tiledriver.l_col(state, 0),
                         [PS((1, 0, 3, 2), "H"), PS((3, 1, 0, 2), "K")])

    def test_l_col_2(self):
        state = PS((0, 2, 3, 1), "")
        self.assertEqual(tiledriver.l_col(state, 0),
                         [PS((2, 0, 3, 1), "H"), PS((3, 2, 0, 1), "K")])

    def test_l_col_3(self):
        state = PS((0, 3, 2, 1), "")
        self.assertEqual(tiledriver.l_col(state, 0),
                         [PS((3, 0, 2, 1), "H"), PS((2, 3, 0, 1), "K")])

    def test_l_col_4(self):
        state = PS((1, 0, 3, 2), "")
        self.assertEqual(tiledriver.l_col(state, 1),
                         [PS((1, 3, 0, 2), "H"), PS((1, 2, 3, 0), "K")])

    def test_l_col_5(self):
        state = PS((3, 0, 1, 2), "")
        self.assertEqual(tiledriver.l_col(state, 1),
                         [PS((3, 1, 0, 2), "H"), PS((3, 2, 1, 0), "K")])


class TestMiddle(unittest.TestCase):
    def test_middle_1(self):
        state = PS((0, 1, 3, 2), "")
        self.assertEqual(tiledriver.middle(state, 0),
                         [PS((1, 0, 3, 2), "H"), PS((3, 1, 0, 2), "K"),
                          PS((2, 1, 3, 0), "L")])

    def test_middle_2(self):
        state = PS((0, 2, 3, 1), "")
        self.assertEqual(tiledriver.middle(state, 0),
                         [PS((2, 0, 3, 1), "H"), PS((3, 2, 0, 1), "K"),
                          PS((1, 2, 3, 0), "L")])

    def test_middle_3(self):
        state = PS((0, 3, 2, 1), "")
        self.assertEqual(tiledriver.middle(state, 0),
                         [PS((3, 0, 2, 1), "H"), PS((2, 3, 0, 1), "K"),
                          PS((1, 3, 2, 0), "L")])

    def test_middle_4(self):
        state = PS((1, 0, 3, 2), "")
        self.assertEqual(tiledriver.middle(state, 1),
                         [PS((1, 3, 0, 2), "H"), PS((1, 2, 3, 0), "K"),
                          PS((0, 1, 3, 2), "L")])

    def test_middle_5(self):
        state = PS((3, 0, 1, 2), "")
        self.assertEqual(tiledriver.middle(state, 1),
                         [PS((3, 1, 0, 2), "H"), PS((3, 2, 1, 0), "K"),
                          PS((0, 3, 1, 2), "L")])


class TestIsSolvable(unittest.TestCase):

    def test_is_solvable_1(self):
        self.assertTrue(tiledriver.is_solvable((3, 2, 1, 0)))

    def test_is_solvable_2(self):
        self.assertFalse(tiledriver.is_solvable((1, 2, 3, 0)))

    def test_is_solvable_3(self):
        self.assertTrue(tiledriver.is_solvable((3, 7, 1, 4, 0, 2, 6, 8, 5)))

    def test_is_solvable_4(self):
        self.assertFalse(tiledriver.is_solvable((0, 2, 1)))

    def test_is_solvable_5(self):
        self.assertFalse(tiledriver.is_solvable((1, 2, 0, 3)))


class TestSolvePuzzle(unittest.TestCase):

    def test_solve_puzzle_1(self):
        self.assertEqual(tiledriver.solve_puzzle
                        ((2, 0, 3, 1)), "KLJ")

    def test_solve_puzzle_2(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 2, 1, 0)), "JLKHJL")

    def test_solve_puzzle_3(self):
        self.assertEqual(tiledriver.solve_puzzle((0, 3, 1, 2)), "KHJL")

    def test_solve_puzzle_4(self):
        self.assertEqual(tiledriver.solve_puzzle((1, 3, 2, 0)), "JL")

    def test_solve_puzzle_5(self):
        self.assertEqual(tiledriver.solve_puzzle((1, 3, 0, 2)), "HJL")


class TestCountInversions(unittest.TestCase):
    def test_count_inversions_1(self):
        self.assertEqual(tiledriver.count_inversions((3, 2, 1, 0), 4), 6)

    def test_count_inversions_2(self):
        self.assertEqual(tiledriver.count_inversions((0, 3, 1, 2), 4), 2)

    def test_count_inversions_3(self):
        self.assertEqual(tiledriver.count_inversions((1, 3, 2, 0), 4), 4)

    def test_count_inversions_4(self):
        self.assertEqual(tiledriver.count_inversions((2, 0, 3, 1), 4), 3)

    def test_count_inversions_5(self):
        self.assertEqual(tiledriver.count_inversions((1, 3, 0, 2), 4), 3)


if __name__ == "__main__":
    unittest.main()

