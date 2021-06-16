# Name:         Sankalp Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   AlphaBits
# Term:         Winter 2021

import unittest

import alphabits
from alphabits import HuffmanNode as H  # only allowed use of from ... import


class TestCreateTree(unittest.TestCase):

    def test_create_tree_1(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.create_tree("DEADBEEFCAFE"), root)

    def test_create_tree_2(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("R", 2, None, None))))
        self.assertEqual(alphabits.create_tree("DEADBEERCARE"), root)

    def test_create_tree_3(self):
        root = None
        self.assertEqual(alphabits.create_tree(''), root)

    def test_create_tree_4(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("P", 2, None, None))))
        self.assertEqual(alphabits.create_tree("DEADBEEPCAPE"), root)

    def test_create_tree_5(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("L", 2, None, None))))
        self.assertEqual(alphabits.create_tree("DEADBEELCALE"), root)



class TestLowestVal(unittest.TestCase):

    def test_lowest_val_1(self):
        vals = [H('D', 2, None, None), H('E', 4, None, None),
                H('A', 2, None, None), H('B', 1, None, None),
                H('F', 2, None, None), H('C', 1, None, None)]

        self.assertEqual(alphabits.lowest_val(vals), H("B", 1, None, None))

    def test_lowest_val_2(self):
        vals = [H('D', 2, None, None), H('E', 4, None, None),
                H('A', 1, None, None), H('B', 1, None, None),
                H('F', 2, None, None), H('C', 1, None, None)]

        self.assertEqual(alphabits.lowest_val(vals), H("A", 1, None, None))

    def test_lowest_val_3(self):
        vals = [H('D', 2, None, None), H('E', 4, None, None),
                H('A', 3, None, None), H('B', 2, None, None),
                H('F', 2, None, None), H('C', 1, None, None)]

        self.assertEqual(alphabits.lowest_val(vals), H("C", 1, None, None))

    def test_lowest_val_4(self):
        vals = [H('D', 2, None, None), H('E', 4, None, None),
                H('A', 3, None, None), H('B', 2, None, None),
                H('F', 2, None, None), H('C', 3, None, None)]

        self.assertEqual(alphabits.lowest_val(vals), H("B", 2, None, None))

    def test_lowest_val_5(self):
        vals = [H('D', 2, None, None), H('E', 4, None, None),
                H('A', 3, None, None), H('B', 5, None, None),
                H('F', 2, None, None), H('C', 9, None, None)]

        self.assertEqual(alphabits.lowest_val(vals), H("D", 2, None, None))

class TestEncode(unittest.TestCase):

    def test_encode_1(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("BE", root), "10100")

    def test_encode_2(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("E", root), "0")

    def test_encode_3(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("D", root), "110")

    def test_encode_4(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("A", root), "100")

    def test_encode_5(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("C", root), "1011")


class TestCharLeaf(unittest.TestCase):

    def test_char_leaf_1(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))

        self.assertEqual(alphabits.char_leaf(root, 'B', ''), "1010")

    def test_char_leaf_2(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))

        self.assertEqual(alphabits.char_leaf(root, 'E', ''), '0')

    def test_char_leaf_3(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))

        self.assertEqual(alphabits.char_leaf(root, 'A', ''), '100')

    def test_char_leaf_4(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))

        self.assertEqual(alphabits.char_leaf(root, 'C', ''), '1011')

    def test_char_leaf_5(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))

        self.assertEqual(alphabits.char_leaf(root, 'D', ''), '110')

class TestDecode(unittest.TestCase):

    def test_decode_1(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("10100", root), "BE")

    def test_decode_2(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("1010", root), "B")

    def test_decode_3(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("100", root), "A")

    def test_decode_4(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("0", root), "E")

    def test_decode_5(self):
        root = None
        self.assertEqual(alphabits.decode(None, root), '')


if __name__ == "__main__":
    unittest.main()
