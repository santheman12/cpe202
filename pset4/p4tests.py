# Name:         Sankalp Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set IV
# Term:         Winter 2021

import unittest

import pset4
# only allowed uses of from ... import
from pset4 import ListNode
from pset4 import TreeNode


class TestBinarySearch(unittest.TestCase):

    def test_binary_search_1(self):
        self.assertEqual(pset4.binary_search((2, 4, 6, 8, 10), 8, 0, 5), 3)

    def test_binary_search_2(self):
        self.assertEqual(pset4.binary_search((2, 4, 6, 8, 10), 7, 0, 5), -1)

    def test_binary_search_3(self):
        self.assertEqual(pset4.binary_search((1, 4, 5), 4, 0, 3), 1)

    def test_binary_search_4(self):
        self.assertEqual(pset4.binary_search((1, 4, 5, 6, 7, 8), 4, 3, 6), -1)

    def test_binary_search_5(self):
        self.assertEqual(pset4.binary_search((1, 54), 54, 1, 2), 1)


class TestSumTree(unittest.TestCase):

    def test_sum_tree_1(self):
        root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
        self.assertEqual(pset4.sum_tree(root), 6)

    def test_sum_tree_2(self):
        root = TreeNode(1, TreeNode(2, None, None), None)
        self.assertEqual(pset4.sum_tree(root), 3)

    def test_sum_tree_3(self):
        root = TreeNode(1, None, None)
        self.assertEqual(pset4.sum_tree(root), 1)

    def test_sum_tree_4(self):
        root = TreeNode(1, None, TreeNode(3, None, None))
        self.assertEqual(pset4.sum_tree(root), 4)

    def test_sum_tree_5(self):
        root = TreeNode(1, TreeNode(2, None, None), TreeNode(0, None, None))
        self.assertEqual(pset4.sum_tree(root), 3)




class TestAllBinary(unittest.TestCase):

    def test_all_binary_1(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None),
                           TreeNode(4, None, None))
        self.assertFalse(pset4.all_binary(root))

    def test_all_binary_2(self):
        root = TreeNode(2, TreeNode(3, TreeNode(4, None, None), None),
                           TreeNode(5, None, None))
        self.assertFalse(pset4.all_binary(root))

    def test_all_binary_3(self):
        root = TreeNode(3, TreeNode(4, TreeNode(5, None, None), None),
                           TreeNode(6, None, None))
        self.assertFalse(pset4.all_binary(root))

    def test_all_binary_4(self):
        root = TreeNode(4, TreeNode(5, TreeNode(6, None, None), None),
                           TreeNode(7, None, None))
        self.assertFalse(pset4.all_binary(root))

    def test_all_binary_5(self):
        root = None
        self.assertTrue(pset4.all_binary(root))


class TestFindRange(unittest.TestCase):

    def test_find_range_1(self):
        root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
        self.assertEqual(pset4.find_range(root), (1, 3))

    def test_find_range_2(self):
        root = TreeNode(2, TreeNode(3, TreeNode(4, None, None), None),
                           TreeNode(5, None, None))
        self.assertEqual(pset4.find_range(root), (2, 5))

    def test_find_range_3(self):
        root = TreeNode(3, TreeNode(4, TreeNode(5, None, None), None),
                           TreeNode(6, None, None))
        self.assertEqual(pset4.find_range(root), (3, 6))

    def test_find_range_4(self):
        root = TreeNode(4, TreeNode(5, TreeNode(6, None, None), None),
                           TreeNode(7, None, None))
        self.assertEqual(pset4.find_range(root), (4, 7))

    def test_find_range_5(self):
        root = TreeNode(6, TreeNode(7, TreeNode(8, None, None), None),
                           TreeNode(9, None, None))
        self.assertEqual(pset4.find_range(root), (6, 9))


class TestIsBST(unittest.TestCase):

    def test_is_bst_1(self):
        root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
        self.assertFalse(pset4.is_bst(root))

    def test_is_bst_2(self):
        root = TreeNode(11, TreeNode(14, None, None), TreeNode(13, None, None))
        self.assertFalse(pset4.is_bst(root))

    def test_is_bst_3(self):
        root = TreeNode(11, TreeNode(8, None, None), TreeNode(13, None, None))
        self.assertTrue(pset4.is_bst(root))

    def test_is_bst_4(self):
        root = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        self.assertTrue(pset4.is_bst(root))

    def test_is_bst_5(self):
        root = TreeNode(15, TreeNode(1, None, None), None)
        self.assertTrue(pset4.is_bst(root))




class TestToBST(unittest.TestCase):

    def test_to_bst_1(self):
        head = ListNode(2, ListNode(3, ListNode(1, None)))
        self.assertEqual(pset4.to_bst(head, None),
                         TreeNode(2, TreeNode(1, None, None),
                                     TreeNode(3, None, None)))

    def test_to_bst_2(self):
        head = ListNode(3, ListNode(4, ListNode(2, None)))
        self.assertEqual(pset4.to_bst(head, None),
                         TreeNode(3, TreeNode(2, None, None),
                                     TreeNode(4, None, None)))

    def test_to_bst_3(self):
        head = ListNode(4, ListNode(5, ListNode(3, None)))
        self.assertEqual(pset4.to_bst(head, None),
                         TreeNode(4, TreeNode(3, None, None),
                                     TreeNode(5, None, None)))

    def test_to_bst_4(self):
        head = ListNode(5, ListNode(6, ListNode(4, None)))
        self.assertEqual(pset4.to_bst(head, None),
                         TreeNode(5, TreeNode(4, None, None),
                                     TreeNode(6, None, None)))

    def test_to_bst_5(self):
        head = ListNode(6, ListNode(7, ListNode(5, None)))
        self.assertEqual(pset4.to_bst(head, None),
                         TreeNode(6, TreeNode(5, None, None),
                                     TreeNode(7, None, None)))


class TestInsert(unittest.TestCase):

    def test_insert_1(self):
        root = TreeNode(2, None, None)
        self.assertEqual(pset4.insert(root, 1),
                         TreeNode(2, TreeNode(1, None, None), None))

    def test_insert_2(self):
        root = TreeNode(2, TreeNode(1, None, None), None)
        self.assertEqual(pset4.insert(root, 3),
                         TreeNode(2, TreeNode(1, None, None),
                                     TreeNode(3, None, None)))

    def test_insert_3(self):
        root = TreeNode(3, TreeNode(2, None, None), None)
        self.assertEqual(pset4.insert(root, 4),
                         TreeNode(3, TreeNode(2, None, None),
                                     TreeNode(4, None, None)))

    def test_insert_4(self):
        root = TreeNode(4, TreeNode(3, None, None), None)
        self.assertEqual(pset4.insert(root, 5),
                         TreeNode(4, TreeNode(3, None, None),
                                     TreeNode(5, None, None)))

    def test_insert_5(self):
        root = TreeNode(5, TreeNode(4, None, None), None)
        self.assertEqual(pset4.insert(root, 6),
                         TreeNode(5, TreeNode(4, None, None),
                                     TreeNode(6, None, None)))




class TestRemove(unittest.TestCase):

    def test_remove_1(self):
        root = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        self.assertEqual(pset4.remove(root, 1),
                         TreeNode(2, None, TreeNode(3, None, None)))

    def test_remove_2(self):
        root = TreeNode(3, TreeNode(2, None, None), TreeNode(4, None, None))
        self.assertEqual(pset4.remove(root, 2),
                         TreeNode(3, None, TreeNode(4, None, None)))

    def test_remove_3(self):
        root = TreeNode(4, TreeNode(3, None, None), TreeNode(5, None, None))
        self.assertEqual(pset4.remove(root, 3),
                         TreeNode(4, None, TreeNode(5, None, None)))

    def test_remove_4(self):
        root = TreeNode(5, TreeNode(4, None, None), TreeNode(6, None, None))
        self.assertEqual(pset4.remove(root, 4),
                         TreeNode(5, None, TreeNode(6, None, None)))

    def test_remove_5(self):
        root = TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None))
        self.assertEqual(pset4.remove(root, 5),
                         TreeNode(6, None, TreeNode(7, None, None)))




class TestRakeLeaves(unittest.TestCase):

    def test_rake_leaves_1(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4, None, None),
                                      TreeNode(5, None, None)),
                           TreeNode(3, None, None))
        self.assertEqual(pset4.rake_leaves(root, None),
                         ListNode(4, ListNode(5, ListNode(3, None))))


    def test_rake_leaves_2(self):
        root = TreeNode(2, TreeNode(3, TreeNode(5, None, None),
                                    TreeNode(6, None, None)),
                        TreeNode(4, None, None))
        self.assertEqual(pset4.rake_leaves(root, None),
                         ListNode(5, ListNode(6, ListNode(4, None))))

    def test_rake_leaves_3(self):
        root = TreeNode(3, TreeNode(4, TreeNode(6, None, None),
                                    TreeNode(7, None, None)),
                        TreeNode(5, None, None))
        self.assertEqual(pset4.rake_leaves(root, None),
                         ListNode(6, ListNode(7, ListNode(5, None))))

    def test_rake_leaves_4(self):
        root = TreeNode(4, TreeNode(5, TreeNode(7, None, None),
                                    TreeNode(8, None, None)),
                        TreeNode(6, None, None))
        self.assertEqual(pset4.rake_leaves(root, None),
                         ListNode(7, ListNode(8, ListNode(6, None))))

    def test_rake_leaves_5(self):
        root = TreeNode(5, TreeNode(6, TreeNode(8, None, None),
                                    TreeNode(9, None, None)),
                        TreeNode(7, None, None))
        self.assertEqual(pset4.rake_leaves(root, None),
                         ListNode(8, ListNode(9, ListNode(7, None))))



class TestOrderList(unittest.TestCase):

    def test_order_list_1(self):
        root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
        self.assertEqual(pset4.order_list(root, "inorder", None),
                         ListNode(2, ListNode(1, ListNode(3, None))))


    def test_order_list_2(self):
        root = TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None))
        self.assertEqual(pset4.order_list(root, "inorder", None),
                         ListNode(3, ListNode(2, ListNode(4, None))))

    def test_order_list_3(self):
        root = TreeNode(3, TreeNode(4, None, None), TreeNode(5, None, None))
        self.assertEqual(pset4.order_list(root, "inorder", None),
                         ListNode(4, ListNode(3, ListNode(5, None))))

    def test_order_list_4(self):
        root = TreeNode(4, TreeNode(5, None, None), TreeNode(6, None, None))
        self.assertEqual(pset4.order_list(root, "inorder", None),
                         ListNode(5, ListNode(4, ListNode(6, None))))

    def test_order_list_5(self):
        root = TreeNode(5, TreeNode(6, None, None), TreeNode(7, None, None))
        self.assertEqual(pset4.order_list(root, "inorder", None),
                         ListNode(6, ListNode(5, ListNode(7, None))))

if __name__ == "__main__":
    unittest.main()
