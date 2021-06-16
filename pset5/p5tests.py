# Name:         Sankalp Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set V
# Term:         Winter 2021

import unittest

import pset5
from pset5 import ListNode  # only allowed uses of from ... import


class TestQueueConstructor(unittest.TestCase):

    def test_queue_constructor_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(queue.tail, ListNode(3, None))

    def test_queue_constructor_2(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, None)))
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, None)))
        self.assertEqual(queue.tail, ListNode(2, None))

    def test_queue_constructor_3(self):
        queue = pset5.Queue(ListNode(1, None))
        self.assertEqual(queue.head,
                         ListNode(1, None))
        self.assertEqual(queue.tail, ListNode(1, None))

    def test_queue_constructor_4(self):
        queue = pset5.Queue(ListNode(2, ListNode(5, ListNode(9, None))))
        self.assertEqual(queue.head,
                         ListNode(2, ListNode(5, ListNode(9, None))))
        self.assertEqual(queue.tail, ListNode(9, None))

    def test_queue_constructor_5(self):
        queue = pset5.Queue(ListNode(0, None))
        self.assertEqual(queue.head,
                         ListNode(0, None))
        self.assertEqual(queue.tail, ListNode(0, None))




class TestQueueEquals(unittest.TestCase):

    def test_queue_equals_1(self):
        qx = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        qy = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(qx, qy)

    def test_queue_equals_2(self):
        qx = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        qy = pset5.Queue(ListNode(3, ListNode(2, ListNode(1, None))))
        self.assertNotEqual(qx, qy)

    def test_queue_equals_3(self):
        qx = pset5.Queue(ListNode(4, None))
        qy = pset5.Queue(ListNode(3, ListNode(2, ListNode(1, None))))
        self.assertNotEqual(qx, qy)

    def test_queue_equals_4(self):
        qx = None
        qy = pset5.Queue(ListNode(3, ListNode(2, ListNode(1, None))))
        self.assertNotEqual(qx, qy)

    def test_queue_equals_5(self):
        qx = pset5.Queue(ListNode(3, ListNode(1, None)))
        qy = pset5.Queue(ListNode(3, ListNode(1, None)))
        self.assertEqual(qx, qy)




class TestQueueEnqueue(unittest.TestCase):

    def test_queue_enqueue_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, None)))
        queue.enqueue(3)
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(queue.tail, ListNode(3, None))

    def test_queue_enqueue_2(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, None)))
        queue.enqueue(4)
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(4, None))))
        self.assertEqual(queue.tail, ListNode(4, None))

    def test_queue_enqueue_3(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, None)))
        queue.enqueue(5)
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(5, None))))
        self.assertEqual(queue.tail, ListNode(5, None))


    def test_queue_enqueue_4(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, None)))
        queue.enqueue(9)
        self.assertEqual(queue.head,
                         ListNode(1, ListNode(2, ListNode(9, None))))
        self.assertEqual(queue.tail, ListNode(9, None))

    def test_queue_enqueue_5(self):
        queue = pset5.Queue(ListNode(2, ListNode(2, None)))
        queue.enqueue(9)
        self.assertEqual(queue.head,
                         ListNode(2, ListNode(2, ListNode(9, None))))
        self.assertEqual(queue.tail, ListNode(9, None))

class TestQueueDequeue(unittest.TestCase):

    def test_queue_dequeue_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(queue.dequeue(), ListNode(1, None))
        self.assertEqual(queue.head, ListNode(2, ListNode(3, None)))
        self.assertEqual(queue.tail, ListNode(3, None))

    def test_queue_dequeue_2(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(4, None))))
        self.assertEqual(queue.dequeue(), ListNode(1, None))
        self.assertEqual(queue.head, ListNode(2, ListNode(4, None)))
        self.assertEqual(queue.tail, ListNode(4, None))

    def test_queue_dequeue_3(self):
        queue = pset5.Queue(ListNode(1, ListNode(4, ListNode(5, None))))
        self.assertEqual(queue.dequeue(), ListNode(1, None))
        self.assertEqual(queue.head, ListNode(4, ListNode(5, None)))
        self.assertEqual(queue.tail, ListNode(5, None))

    def test_queue_dequeue_4(self):
        queue = pset5.Queue(ListNode(1, ListNode(6, ListNode(5, None))))
        self.assertEqual(queue.dequeue(), ListNode(1, None))
        self.assertEqual(queue.head, ListNode(6, ListNode(5, None)))
        self.assertEqual(queue.tail, ListNode(5, None))

    def test_queue_dequeue_5(self):
        queue = pset5.Queue(ListNode(1, ListNode(9, ListNode(5, None))))
        self.assertEqual(queue.dequeue(), ListNode(1, None))
        self.assertEqual(queue.head, ListNode(9, ListNode(5, None)))
        self.assertEqual(queue.tail, ListNode(5, None))



class TestSize(unittest.TestCase):

    def test_size_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        self.assertEqual(pset5.size(queue), 3)

    def test_size_2(self):
        queue = pset5.Queue(ListNode(1, None))
        self.assertEqual(pset5.size(queue), 1)

    def test_size_3(self):
        queue = None
        self.assertEqual(pset5.size(queue), 0)

    def test_size_4(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, None)))
        self.assertEqual(pset5.size(queue), 2)

    def test_size_5(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(2,
                                        ListNode(2, None)))))
        self.assertEqual(pset5.size(queue), 4)


class TestDequeueAll(unittest.TestCase):

    def test_dequeue_all_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(1,
                                                    ListNode(3, None)))))
        self.assertEqual(pset5.dequeue_all(queue, 1), 2)
        self.assertEqual(queue.head, ListNode(2, ListNode(3, None)))

    def test_dequeue_all_2(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(1,
                                                    ListNode(3, None)))))
        self.assertEqual(pset5.dequeue_all(queue, 2), 1)
        self.assertEqual(queue.head, ListNode(1, ListNode(1,
                                                ListNode(3, None))))

    def test_dequeue_all_3(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(1,
                                                    ListNode(3, None)))))
        self.assertEqual(pset5.dequeue_all(queue, 3), 1)
        self.assertEqual(queue.head, ListNode(1, ListNode(2,
                                            ListNode(1, None))))

    def test_dequeue_all_4(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, None)))
        self.assertEqual(pset5.dequeue_all(queue, 2), 1)
        self.assertEqual(queue.head, ListNode(1, None))

    def test_dequeue_all_5(self):
        queue = pset5.Queue(ListNode(2, ListNode(2, None)))
        self.assertEqual(pset5.dequeue_all(queue, 2), 2)
        self.assertEqual(queue.head, None)




class TestQueueFlip(unittest.TestCase):

    def test_flip_1(self):
        queue = pset5.Queue(ListNode(1, ListNode(2,
                                    ListNode(3, None))))
        pset5.flip(queue)
        self.assertEqual(queue.head,
                         ListNode(3, ListNode(2, ListNode(1, None))))
        self.assertEqual(queue.tail, ListNode(1, None))

    def test_flip_2(self):
        queue = pset5.Queue(ListNode(1, ListNode(2, ListNode(3,
                                            ListNode(4, None)))))
        pset5.flip(queue)
        self.assertEqual(queue.head,
                         ListNode(4, ListNode(3,
                                    ListNode(2, ListNode(1, None)))))
        self.assertEqual(queue.tail, ListNode(1, None))

    def test_flip_3(self):
        queue = pset5.Queue(ListNode(1, None))
        pset5.flip(queue)
        self.assertEqual(queue.head,
                         ListNode(1, None))
        self.assertEqual(queue.tail, ListNode(1, None))

    def test_flip_4(self):
        queue = pset5.Queue(ListNode(5, ListNode(6, None)))
        pset5.flip(queue)
        self.assertEqual(queue.head,
                         ListNode(6, ListNode(5, None)))
        self.assertEqual(queue.tail, ListNode(5, None))

    def test_flip_5(self):
        queue = pset5.Queue(ListNode(8, ListNode(5,
                                ListNode(1, ListNode(7, None)))))
        pset5.flip(queue)
        self.assertEqual(queue.head,
                         ListNode(7, ListNode(1, ListNode(5,
                                        ListNode(8, None)))))
        self.assertEqual(queue.tail, ListNode(8, None))



class TestSiftUp(unittest.TestCase):

    def test_sift_up_1(self):
        self.assertEqual(pset5.sift_up([7, 6, 5, 4, 3, 2, 8], 6),
                         [8, 6, 7, 4, 3, 2, 5])

    def test_sift_up_2(self):
        self.assertEqual(pset5.sift_up([8, 7, 6, 5, 4, 3, 9], 6),
                         [9, 7, 8, 5, 4, 3, 6])

    def test_sift_up_3(self):
        self.assertEqual(pset5.sift_up([9, 8, 7, 6, 5, 4, 10], 6),
                         [10, 8, 9, 6, 5, 4, 7])

    def test_sift_up_4(self):
        self.assertEqual(pset5.sift_up([10, 9, 8, 7, 6, 5, 11], 6),
                         [11, 9, 10, 7, 6, 5, 8])

    def test_sift_up_5(self):
        self.assertEqual(pset5.sift_up([11, 10, 9, 8, 7, 6, 12], 6),
                         [12, 10, 11, 8, 7, 6, 9])




class TestSiftDown(unittest.TestCase):

    def test_sift_down_1(self):
        self.assertEqual(pset5.sift_down([1, 7, 6, 5, 4, 3, 2], 0),
                         [7, 5, 6, 1, 4, 3, 2])

    def test_sift_down_2(self):
        self.assertEqual(pset5.sift_down([1, 8, 6, 5, 4, 3, 2], 0),
                         [8, 5, 6, 1, 4, 3, 2])

    def test_sift_down_3(self):
        self.assertEqual(pset5.sift_down([1, 9, 6, 5, 4, 3, 2], 0),
                         [9, 5, 6, 1, 4, 3, 2])

    def test_sift_down_4(self):
        self.assertEqual(pset5.sift_down([1, 10, 6, 5, 4, 3, 2], 0),
                         [10, 5, 6, 1, 4, 3, 2])

    def test_sift_down_5(self):
        self.assertEqual(pset5.sift_down([1, 11, 6, 5, 4, 3, 2], 0),
                         [11, 5, 6, 1, 4, 3, 2])




class TestHeapify(unittest.TestCase):

    def test_heapify_1(self):
        self.assertEqual(pset5.heapify([1, 2, 3, 4, 5, 6, 7]),
                         [7, 5, 6, 4, 2, 1, 3])

    def test_heapify_2(self):
        self.assertEqual(pset5.heapify([1, 2, 3, 4, 5, 6, 8]),
                         [8, 5, 6, 4, 2, 1, 3])

    def test_heapify_3(self):
        self.assertEqual(pset5.heapify([1, 2, 3, 4, 5, 6, 9]),
                         [9, 5, 6, 4, 2, 1, 3])

    def test_heapify_4(self):
        self.assertEqual(pset5.heapify([1, 2, 3, 4, 5, 6, 10]),
                         [10, 5, 6, 4, 2, 1, 3])

    def test_heapify_5(self):
        self.assertEqual(pset5.heapify([1, 2, 3, 4, 5, 6, 11]),
                         [11, 5, 6, 4, 2, 1, 3])




class TestInsert(unittest.TestCase):

    def test_insert_1(self):
        self.assertEqual(pset5.insert([6, 5, 4, 3, 2, 1], 7),
                         [7, 5, 6, 3, 2, 1, 4])
    def test_insert_2(self):
        self.assertEqual(pset5.insert([6, 5, 4, 3, 2, 1], 9),
                         [9, 5, 6, 3, 2, 1, 4])

    def test_insert_3(self):
        self.assertEqual(pset5.insert([6, 5, 4, 3, 2, 1], 11),
                         [11, 5, 6, 3, 2, 1, 4])

    def test_insert_4(self):
        self.assertEqual(pset5.insert([6, 5, 4, 3, 2, 1], 14),
                         [14, 5, 6, 3, 2, 1, 4])
    def test_insert_5(self):
        self.assertEqual(pset5.insert([], 15),
                         [15])



class TestRemove(unittest.TestCase):

    def test_remove_1(self):
        self.assertEqual(pset5.remove([7, 6, 5, 4, 3, 2, 1]),
                         (7, [6, 4, 5, 1, 3, 2]))

    def test_remove_2(self):
        self.assertEqual(pset5.remove([9, 6, 5, 4, 3, 2, 1]),
                         (9, [6, 4, 5, 1, 3, 2]))

    def test_remove_3(self):
        self.assertEqual(pset5.remove([10, 6, 5, 4, 3, 2, 1]),
                         (10, [6, 4, 5, 1, 3, 2]))

    def test_remove_4(self):
        self.assertEqual(pset5.remove([13, 6, 5, 4, 3, 2, 1]),
                         (13, [6, 4, 5, 1, 3, 2]))

    def test_remove_5(self):
        self.assertEqual(pset5.remove([14, 6, 5, 4, 3, 2, 1]),
                         (14, [6, 4, 5, 1, 3, 2]))

if __name__ == "__main__":
    unittest.main()
