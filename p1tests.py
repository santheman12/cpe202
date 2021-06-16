# Name:         Sankalp Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set I
# Term:         Winter 2021

import unittest

import pset1
from pset1 import *  # only allowed use of from ... import


class TestInsert(unittest.TestCase):

    def test_insert_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.insert(head, 5, 2),
                    ListNode(1, ListNode(2, ListNode(5, ListNode(3, None)))))

    def test_insert_2(self):
        head = ListNode(9, ListNode(10, ListNode(11, ListNode(13, ListNode(14, ListNode(15, None))))))
        self.assertEqual(pset1.insert(head, 12, 3),
                         ListNode(9, ListNode(10, ListNode(11, ListNode(12, ListNode(13, ListNode(14, ListNode(15, None))))))))

    def test_insert_3(self):
        head = ListNode(6, ListNode(8, None))
        self.assertEqual(pset1.insert(head, 7, 4),
                         ListNode(6, ListNode(8, ListNode(7,None))))

    def test_insert_4(self):
        head = ListNode(2, None)
        self.assertEqual(pset1.insert(head, 3, 1),
                         ListNode(2, ListNode(3, None)))

    def test_insert_5(self):
        head = ListNode(5, ListNode(10, ListNode(15, None)))
        self.assertEqual(pset1.insert(head, 20, 3),
                         ListNode(5, ListNode(10, ListNode(15, ListNode(20, None)))))


class TestRemove(unittest.TestCase):

    def test_remove_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.remove(head, 0), ListNode(2, ListNode(3, None)))

    def test_remove_2(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.remove(head, 1), ListNode(1, ListNode(3, None)))

    def test_remove_3(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.remove(head, 2), ListNode(1, ListNode(2, None)))

    def test_remove_4(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
        self.assertEqual(pset1.remove(head, 2), ListNode(1, ListNode(2, ListNode(4, None))))

    def test_remove_5(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
        self.assertEqual(pset1.remove(head, 3), ListNode(1, ListNode(2, ListNode(3, None))))


    def test_remove_6(self):
        head = ListNode(2, None)
        self.assertEqual(pset1.remove(head, 5),
                         IndexError())

    def test_remove_7(self):
        head = None
        self.assertEqual(pset1.remove(head, 0),
                         None)





class TestIndex(unittest.TestCase):

    def test_index_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.index(head, 3), 2)

    def test_index_2(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.index(head, 1), 0)

    def test_index_3(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.index(head, 10), -1)

    def test_index_4(self):
        head = ListNode(1, ListNode(5, ListNode(2, ListNode(9, ListNode(4, ListNode(1, ListNode(2, None)))))))
        self.assertEqual(pset1.index(head, 4), 4)

    def test_index_5(self):
        head = ListNode(1, None)
        self.assertEqual(pset1.index(head, 1), 0)




class TestConcat(unittest.TestCase):

    def test_concat_1(self):
        xs = ListNode(1, ListNode(2, ListNode(3, None)))
        ys = ListNode(4, ListNode(5, None))
        self.assertEqual(pset1.concat(xs, ys),
                         ListNode(1, ListNode(2, ListNode(3, ListNode(4,
                                  ListNode(5, None))))))

    def test_concat_2(self):
        xs = ListNode(1, ListNode(2, None))
        ys = ListNode(4, ListNode(5, None))
        self.assertEqual(pset1.concat(xs, ys),
                         ListNode(1, ListNode(2, ListNode(4,
                                  ListNode(5, None)))))
    def test_concat_3(self):
        xs = ListNode(1, None)
        ys = ListNode(4, ListNode(6, None))
        self.assertEqual(pset1.concat(xs, ys),
                         ListNode(1, ListNode(4, ListNode(6, None))))

    def test_concat_4(self):
        xs = None
        ys = ListNode(4, None)
        self.assertEqual(pset1.concat(xs, ys),
                         ListNode(4, None))

    def test_concat_5(self):
        xs = ListNode(1, ListNode(2, None))
        ys = None
        self.assertEqual(pset1.concat(xs, ys),
                         ListNode(1, ListNode(2, None)))



class TestSumList(unittest.TestCase):

    def test_sum_list_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.sum_list(head), 6)

    def test_sum_list_2(self):
        head = None
        self.assertEqual(pset1.sum_list(head), 0)

    def test_sum_list_3(self):
        head = ListNode(1, None)
        self.assertEqual(pset1.sum_list(head), 1)

    def test_sum_list_4(self):
        head = ListNode(0, ListNode(1, None))
        self.assertEqual(pset1.sum_list(head), 1)

    def test_sum_list_5(self):
        head = ListNode(100, ListNode(200, ListNode(500, None)))
        self.assertEqual(pset1.sum_list(head), 800)


class TestExpList(unittest.TestCase):

    def test_exp_list_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset1.exp_list(head, 3),
                         ListNode(1, ListNode(8, ListNode(27, None))))

    def test_exp_list_2(self):
        head = ListNode(5, ListNode(7, ListNode(10, None)))
        self.assertEqual(pset1.exp_list(head, 2),
                         ListNode(25, ListNode(49, ListNode(100, None))))

    def test_exp_list_3(self):
        head = ListNode(9, None)
        self.assertEqual(pset1.exp_list(head, 2),
                         ListNode(81, None))

    def test_exp_list_4(self):
        head = ListNode(5, ListNode(4, ListNode(4, None)))
        self.assertEqual(pset1.exp_list(head, 0),
                         ListNode(1, ListNode(1, ListNode(1, None))))

    def test_exp_list_5(self):
        head = ListNode(11, ListNode(13, ListNode(4, ListNode(0, ListNode(1, ListNode(20, ListNode(12, None)))))))
        self.assertEqual(pset1.exp_list(head, 2),
                         ListNode(121, ListNode(169, ListNode(16, ListNode(0, ListNode(1, ListNode(400, ListNode(144, None))))))))


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_1(self):
        head = ListNode(0, ListNode(1, ListNode(1, ListNode(2, ListNode(3, None)))))
        self.assertEqual(pset1.fibonacci(5), head)

    def test_fibonacci_2(self):
        head = ListNode(0, ListNode(1, ListNode(1, ListNode(2, None))))
        self.assertEqual(pset1.fibonacci(4), head)

    def test_fibonacci_3(self):
        head = ListNode(0, None)
        self.assertEqual(pset1.fibonacci(1), head)

    def test_fibonacci_4(self):
        head = None
        self.assertEqual(pset1.fibonacci(0), head)

    def test_fibonacci_5(self):
        head = ListNode(0, ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(8,  ListNode(13, None))))))))
        self.assertEqual(pset1.fibonacci(8), head)



class TestZipLists(unittest.TestCase):

    def test_zip_lists_1(self):
        xs = ListNode(1, ListNode(2, ListNode(3, None)))
        ys = ListNode(4, None)
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(1, ListNode(4, ListNode(2,
                                ListNode(3, None)))))

    def test_zip_lists_2(self):
        xs = ListNode(1, ListNode(3, ListNode(5, ListNode(7, ListNode(9, None)))))
        ys = ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10, None)))))
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7,
                      ListNode(8, ListNode(9, ListNode(10, None)))))))))))

    def test_zip_lists_3(self):
        xs = ListNode(1, ListNode(2, None))
        ys = ListNode(3, None)
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(1, ListNode(3, ListNode(2, None))))

    def test_zip_lists_4(self):
        xs = None
        ys = ListNode(2, ListNode(4, ListNode(6, None)))
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(2, ListNode(4, ListNode(6, None))))

    def test_zip_lists_5(self):
        xs = ListNode(1, ListNode(3, ListNode(5, ListNode(7, ListNode(9, None)))))
        ys = None
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(1, ListNode(3, ListNode(5, ListNode(7, ListNode(9, None))))))

    def test_zip_lists_6(self):
        xs = ListNode(2, None)
        ys = ListNode(3, ListNode(4, ListNode(6, ListNode(4, None))))
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(2, ListNode(3, ListNode(4, ListNode(6, ListNode(4, None))))))

    def test_zip_lists_7(self):
        xs = ListNode(2, ListNode(4, None))
        ys = ListNode(3, ListNode(5,None))
        self.assertEqual(pset1.zip_lists(xs, ys),
                         ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))




class TestUnzipList(unittest.TestCase):

    def test_unzip_list_1(self):
        head = ListNode(1, ListNode(4, ListNode(2, ListNode(5,
                        ListNode(3, None)))))
        unzipped = (ListNode(1, ListNode(2, ListNode(3, None))),
                    ListNode(4, ListNode(5, None)))
        self.assertEqual(pset1.unzip_list(head), unzipped)

    def test_unzip_list_2(self):
        head = ListNode(1, ListNode(4, ListNode(2, ListNode(5,None))))
        unzipped = (ListNode(1, ListNode(2, None)),
                    ListNode(4, ListNode(5, None)))
        self.assertEqual(pset1.unzip_list(head), unzipped)

    def test_unzip_list_3(self):
        head = ListNode(3, ListNode(2, None))
        unzipped = (ListNode(3, None),
                   ListNode(2, None))
        self.assertEqual(pset1.unzip_list(head), unzipped)

    def test_unzip_list_4(self):
        head = ListNode(1, ListNode(3, ListNode(5, ListNode(9, None))))
        unzipped = (ListNode(1, ListNode(5, None))), ListNode(3, ListNode(9, None)),
        self.assertEqual(pset1.unzip_list(head), unzipped)

    def test_unzip_list_5(self):
        head = ListNode(1, None)
        unzipped = (ListNode(1, None)), None,
        self.assertEqual(pset1.unzip_list(head), unzipped)


if __name__ == "__main__":
    unittest.main()
