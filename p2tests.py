# Name:         Sankalp Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set II
# Term:         Winter 2021

import unittest

import pset2
from pset2 import StackNode  # only allowed use of from ... import


class TestPush(unittest.TestCase):

    def test_push_1(self):
        top = StackNode(2, StackNode(3, None))
        top = pset2.push(top, StackNode(1, None))
        self.assertEqual(top, StackNode(1, StackNode(2, StackNode(3, None))))

    def test_push_2(self):
        top = StackNode(2, None)
        top = pset2.push(top, StackNode(1, None))
        self.assertEqual(top, StackNode(1, StackNode(2, None)))

    def test_push_3(self):
        top = None
        top = pset2.push(top, StackNode(1, None))
        self.assertEqual(top, StackNode(1, None))

    def test_push_4(self):
        top = StackNode(2, None)
        top = pset2.push(top, None)
        self.assertEqual(top, StackNode(2, None))

    def test_push_5(self):
        top = None
        top = pset2.push(top, None)
        self.assertEqual(top, None)


class TestPop(unittest.TestCase):

    def test_pop_1(self):
        top = StackNode(1, StackNode(2, StackNode(3, None)))
        node, top = pset2.pop(top)
        self.assertEqual(node.val, 1)
        self.assertEqual(node.ref, None)
        self.assertEqual(top, StackNode(2, StackNode(3, None)))

    def test_pop_2(self):
        top = StackNode(9, StackNode(2, None))
        node, top = pset2.pop(top)
        self.assertEqual(node.val, 9)
        self.assertEqual(node.ref, None)
        self.assertEqual(top, StackNode(2,None))

    def test_pop_3(self):
        top = StackNode(9, None)
        node, top = pset2.pop(top)
        self.assertEqual(node.val, 9)
        self.assertEqual(node.ref, None)
        self.assertEqual(top, None)

    def test_pop_4(self):
        top = StackNode(9, StackNode(11, StackNode(12, StackNode(13, StackNode(14, StackNode(15, None))))))
        node, top = pset2.pop(top)
        self.assertEqual(node.val, 9)
        self.assertEqual(node.ref, None)
        self.assertEqual(top, StackNode(11, StackNode(12, StackNode(13, StackNode(14, StackNode(15, None))))))

    def test_pop_5(self):
        top = StackNode(5, StackNode(6, StackNode(7, None)))
        node, top = pset2.pop(top)
        self.assertEqual(node.val, 5)
        self.assertEqual(node.ref, None)
        self.assertEqual(top, StackNode(6, StackNode(7, None)))




class TestMove(unittest.TestCase):

    def test_move_1(self):
        top = StackNode(1, StackNode(2, StackNode(3, None)))
        self.assertEqual(pset2.move(top, None),
                         (StackNode(2, StackNode(3, None)), StackNode(1, None)))

    def test_move_2(self):
        top = StackNode(4, StackNode(6, None))
        self.assertEqual(pset2.move(top, None),
                         (StackNode(6, None), StackNode(4, None)))

    def test_move_3(self):
        top = StackNode(1, StackNode(2, None))
        self.assertEqual(pset2.move(top, None),
                         (StackNode(2, None), StackNode(1, None)))

    def test_move_4(self):
        top = StackNode(5, StackNode(6, StackNode(7, StackNode(8, StackNode(9, StackNode(10, None))))))
        self.assertEqual(pset2.move(top, None),
                         (StackNode(6, StackNode(7, StackNode(8, StackNode(9, StackNode(10, None))))), StackNode(5, None)))

    def test_move_5(self):
        top = StackNode(1000, StackNode(24, None))
        self.assertEqual(pset2.move(top, None),
                         (StackNode(24, None), StackNode(1000, None)))


class TestFlipStack(unittest.TestCase):

    def test_flip_stack_1(self):
        top = StackNode(1, StackNode(2, StackNode(3, None)))
        self.assertEqual(pset2.flip_stack(top),
                         StackNode(3, StackNode(2, StackNode(1, None))))

    def test_flip_stack_2(self):
        top = StackNode(1, StackNode(2, None))
        self.assertEqual(pset2.flip_stack(top),
                         StackNode(2, StackNode(1, None)))

    def test_flip_stack_3(self):
        top = StackNode(1, None)
        self.assertEqual(pset2.flip_stack(top),
                         StackNode(1, None))

    def test_flip_stack_4(self):
        top = None
        self.assertEqual(pset2.flip_stack(top),
                         None)

    def test_flip_stack_5(self):
        top = StackNode(9, None)
        self.assertEqual(pset2.flip_stack(top),
                         StackNode(9, None))

    def test_flip_stack_6(self):
        top = StackNode(1, StackNode(8, StackNode(3, None)))
        self.assertEqual(pset2.flip_stack(top),
                         StackNode(3, StackNode(8, StackNode(1, None))))

    def test_flip_stack_7(self):
        top = StackNode(6, StackNode(7, StackNode(8, StackNode(9, StackNode(10, None)))))
        self.assertEqual(pset2.flip_stack(top),
                         StackNode(10, StackNode(9, StackNode(8, StackNode(7, StackNode(6, None))))))



class TestConcat(unittest.TestCase):

    def test_concat_1(self):
        xs = StackNode(1, StackNode(2, StackNode(3, None)))
        ys = StackNode(4, StackNode(5, None))
        self.assertEqual(pset2.concat(xs, ys),
                         StackNode(1, StackNode(2, StackNode(3,
                                      StackNode(4, StackNode(5, None))))))

    def test_concat_2(self):
        xs = StackNode(1, StackNode(3, None))
        ys = StackNode(4, StackNode(5, None))
        self.assertEqual(pset2.concat(xs, ys),
                         StackNode(1, StackNode(3,
                                      StackNode(4, StackNode(5, None)))))
    def test_concat_3(self):
        xs = StackNode(1, None)
        ys = StackNode(4, StackNode(5, None))
        self.assertEqual(pset2.concat(xs, ys),
                         StackNode(1,
                                      StackNode(4, StackNode(5, None))))

    def test_concat_4(self):
        xs = StackNode(1, StackNode(3, None))
        ys = StackNode(4, None)
        self.assertEqual(pset2.concat(xs, ys),
                         StackNode(1,
                                      StackNode(3, StackNode(4, None))))

    def test_concat_5(self):
        xs = None
        ys = None
        self.assertEqual(pset2.concat(xs, ys),
                         None)



class TestPopAll(unittest.TestCase):

    def test_pop_all_1(self):
        top = StackNode(1, StackNode(2, StackNode(1, StackNode(3, None))))
        self.assertEqual(pset2.pop_all(top, 1),
                         StackNode(2, StackNode(3, None)))

    def test_pop_all_2(self):
        top = StackNode(1, StackNode(5, None))
        self.assertEqual(pset2.pop_all(top, 5),
                         StackNode(1, None))

    def test_pop_all_3(self):
        top = StackNode(1, None)
        self.assertEqual(pset2.pop_all(top, 1),
                         None)

    def test_pop_all_4(self):
        top = StackNode(1, StackNode(1, StackNode(1, StackNode(3, None))))
        self.assertEqual(pset2.pop_all(top, 2),
                         StackNode(1, StackNode(1, StackNode(1, StackNode(3, None)))))

    def test_pop_all_5(self):
        top = None
        self.assertEqual(pset2.pop_all(top, 2),
                         None)



class TestZipStacks(unittest.TestCase):

    def test_zip_stacks_1(self):
        xs = StackNode(1, StackNode(2, StackNode(3, None)))
        ys = StackNode(4, None)
        self.assertEqual(pset2.zip_stacks(xs, ys),
                         StackNode(1, StackNode(4, StackNode(2,
                                                             StackNode(3, None)))))

    def test_zip_stacks_2(self):
        xs = StackNode(5, None)
        ys = StackNode(1, StackNode(2, None))
        self.assertEqual(pset2.zip_stacks(xs, ys),
                         StackNode(5, StackNode(1, StackNode(2,
                                                             None))))

    def test_zip_stacks_3(self):
        xs = StackNode(1, StackNode(3, StackNode(5, StackNode(7, StackNode(9, StackNode(11, None))))))
        ys = StackNode(2, StackNode(4, StackNode(6, StackNode(8, StackNode(10, StackNode(12, None))))))
        self.assertEqual(pset2.zip_stacks(xs, ys),
                         StackNode(1, StackNode(2, StackNode(3, StackNode(4, StackNode(5, StackNode(6, StackNode(7,
                         StackNode(8, StackNode(9, StackNode(10, StackNode(11, StackNode(12, None)))))))))))))

    def test_zip_stacks_4(self):
        xs = None
        ys = StackNode(4, None)
        self.assertEqual(pset2.zip_stacks(xs, ys),
                         StackNode(4, None))

    def test_zip_stacks_5(self):
        xs = None
        ys = None
        self.assertEqual(pset2.zip_stacks(xs, ys),
                         None)


class TestUnzipStack(unittest.TestCase):

    def test_unzip_stack_1(self):
        top = StackNode(1, StackNode(4, StackNode(2,
                                        StackNode(5, StackNode(3, None)))))
        self.assertEqual(pset2.unzip_stack(top),
                         (StackNode(1, StackNode(2, StackNode(3, None))),
                          StackNode(4, StackNode(5, None))))

    def test_unzip_stack_2(self):
        top = StackNode(1, StackNode(4, None))
        self.assertEqual(pset2.unzip_stack(top),
                         (StackNode(1, None),
                          StackNode(4, None)))

    def test_unzip_stack_3(self):
        top = StackNode(1, None)
        self.assertEqual(pset2.unzip_stack(top),
                         (StackNode(1, None),
                          None))

    def test_unzip_stack_4(self):
        top = None
        self.assertEqual(pset2.unzip_stack(top),
                        (None, None))

    def test_unzip_stack_5(self):
        top = StackNode(14, StackNode(42, StackNode(24, StackNode(52, StackNode(37, None)))))
        self.assertEqual(pset2.unzip_stack(top),
                         (StackNode(14, StackNode(24, StackNode(37, None))),
                          StackNode(42, StackNode(52, None))))



class TestSortStack(unittest.TestCase):

    def test_sort_stack_1(self):
        top = StackNode(11, StackNode(423, StackNode(52, StackNode(5, StackNode(9, StackNode(8, None))))))
        self.assertEqual(pset2.sort_stack(top),
                         StackNode(5, StackNode(8, StackNode(9, StackNode(11, StackNode(52, StackNode(423, None)))))))
    def test_sort_stack_2(self):
        top = StackNode(5, StackNode(1, StackNode(8, None)))
        self.assertEqual(pset2.sort_stack(top),
                         StackNode(1, StackNode(5, StackNode(8, None))))
    def test_sort_stack_3(self):
        top = StackNode(4, None)
        self.assertEqual(pset2.sort_stack(top),
                         StackNode(4, None))
    def test_sort_stack_4(self):
        top = StackNode(4, StackNode(4, StackNode(4, None)))
        self.assertEqual(pset2.sort_stack(top),
                         StackNode(4, StackNode(4, StackNode(4, None))))
    def test_sort_stack_5(self):
        top = StackNode(5244, StackNode(24, StackNode(24, StackNode(81, None))))
        self.assertEqual(pset2.sort_stack(top),
                         StackNode(24, StackNode(24, StackNode(81, StackNode(5244, None)))))


if __name__ == "__main__":
    unittest.main()

