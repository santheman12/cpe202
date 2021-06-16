# Name:         Sankalp Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set V
# Term:         Winter 2021

from typing import List, Optional, Tuple


class ListNode:

    def __init__(self, val: int, ref: Optional["ListNode"]) -> None:
        self.val = val
        self.ref = ref

    def __eq__(self, other: Optional["ListNode"]) -> bool:
        if other is None:
            return False
        return self.val == other.val and self.ref == other.ref

    def __repr__(self) -> str:
        if self.ref is None:
            return str(self.val)
        return str(self.val) + " " + str(self.ref)




class Queue:

    def __init__(self, head: Optional[ListNode]) -> None:
        """
        An instance of Queue has two attributes.

            head: A reference to the first ListNode in the queue.
            tail: A reference to the final ListNode in the queue.

        >>> queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        >>> queue.head
        ListNode(1, ListNode(2, ListNode(3, None)))
        >>> queue.tail
        ListNode(3, None)
        """
        self.head = head

        temp = head

        if temp is None:
            self.tail = None
        else:
            while temp.ref is not None:
                temp = temp.ref
            self.tail = temp

    def __eq__(self, other: "Queue") -> bool:
        """
        Return True if both Queue objects maintain references to the same
        sequence of ListNode objects and False otherwise.

        >>> qx = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        >>> qy = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        >>> qz = Queue(ListNode(3, ListNode(2, ListNode(1, None))))
        >>> qx == qy
        True
        >>> qx == qz
        False
        """
        if other is None:
            return False

        return self.head == other.head and self.tail == other.tail

    def enqueue(self, val: int) -> None:
        """
        Add the given integer as a ListNode to the tail of the queue. This
        function mutates the calling Queue object in-place and does not return
        a value.

        >>> queue = Queue(ListNode(1, ListNode(2, None)))
        >>> queue.enqueue(3)
        >>> queue.head
        ListNode(1, ListNode(2, ListNode(3, None)))
        >>> queue.tail
        ListNode(3, None)
        """

        x = ListNode(val, None)

        if self.tail is None or self.head is None:
            self.head = x
            self.tail = x
        else:
            self.tail.ref = x
            self.tail = self.tail.ref

    def dequeue(self) -> ListNode:
        """
        Remove the ListNode at the head of the queue and return it with its
        reference set to None. If the queue is empty, raise a ValueError. This
        function mutates the calling Queue object.

        >>> queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
        >>> queue.dequeue()
        ListNode(1, None)
        >>> queue.head
        ListNode(2, ListNode(3, None))
        >>> queue.tail
        ListNode(3, None)
        """

        if self.head is None:
            raise ValueError
        else:
            temp_head = ListNode(self.head.val, None)
            self.head = self.head.ref
            return temp_head


def size(queue: Queue) -> int:
    """
    Return the number of ListNodes in the given queue. The queue must contain
    its original ListNodes in the same order at the end of the procedure.

    >>> queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
    >>> size(queue)
    3
    """

    if queue is None:
        return 0

    counter = 0
    head = Queue(None)
    while queue.head is not None:
        if head.head is None:
            head = Queue(ListNode(queue.head.val, None))
        else:
            head.enqueue(queue.head.val)
        queue.dequeue()
        counter += 1

    while head.head is not None:
        queue.enqueue(head.head.val)
        head.dequeue()

    print(queue.head)

    return counter


def dequeue_all(queue: Queue, val: int) -> int:
    """
    Using dequeue and enqueue operations, remove all ListNodes from the queue
    that contain the given integer value and return the number of nodes removed.
    All other ListNodes must be in the queue in their original order at the end
    of the procedure.

    >>> queue = Queue(ListNode(1, ListNode(2, ListNode(1, ListNode(3, None)))))
    >>> dequeue_all(queue, 1)
    2
    >>> queue.head
    ListNode(2, ListNode(3, None))
    """

    if queue is None:
        return 0

    counter = 0

    head = Queue(None)
    while queue.head is not None:
        if queue.head.val != val:
            if head.head is None:
                head = Queue(ListNode(queue.head.val, None))
            else:
                head.enqueue(queue.head.val)
            queue.dequeue()
        else:
            counter += 1
            queue.dequeue()

    print(head)
    while head.head is not None:
        queue.enqueue(head.head.val)
        head.dequeue()
        print(queue.tail)

    return counter


def flip(queue: Queue) -> None:
    """
    Reverse the ListNodes of the given queue such that the original tail node
    becomes the head and vice versa. This function mutates the queue.

    >>> queue = Queue(ListNode(1, ListNode(2, ListNode(3, None))))
    >>> flip(queue)
    >>> queue.head
    ListNode(3, ListNode(2, ListNode(1, None)))
    >>> queue.tail
    ListNode(1, None)
    """

    head = Queue(None)
    while queue.head is not None:
        head = Queue(ListNode(queue.head.val, head.head))
        queue.dequeue()
    print(head)
    while head.head is not None:
        queue.enqueue(head.head.val)
        head.dequeue()


def sift_up(heap: List[int], index: int) -> List[int]:
    """
    Return a max-heap that has undergone a sift-up operation for the value at
    the given index.

    >>> sift_up([7, 6, 5, 4, 3, 2, 8], 6)
    [8, 6, 7, 4, 3, 2, 5]
    """

    while index != 0:
        parent = (index - 1) // 2
        if heap[index] > heap[parent]:
            heap[parent], heap[index] = heap[index], heap[parent]
        index = parent
    return heap


def sift_down(heap: List[int], index: int) -> List[int]:
    """
    Return a max-heap in which the root of a subtree at the given index has
    been sifted down (if necessary) to maintain the Heap Property.

    >>> sift_down([1, 7, 6, 5, 4, 3, 2], 0)
    [7, 5, 6, 1, 4, 3, 2]
    """

    while(2 * index + 1) <= len(heap)-1:
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if right_child <= len(heap) - 1 and \
                heap[index] < heap[right_child] and \
                heap[right_child] >= heap[left_child]:

            heap[right_child], heap[index] = heap[index], \
                                             heap[right_child]
            index = right_child

        elif left_child <= len(heap) - 1 and \
                heap[index] < heap[left_child]:

            heap[left_child], heap[index] = heap[index], \
                                            heap[left_child]
            index = left_child
        else:
            return heap

    return heap


def heapify(ints: List[int]) -> List[int]:
    """
    Return a max-heap (represented as a list of integers) created using the
    given integers. This function must using sifting instead of insert to run
    in linear (instead of log-linear) time.

    >>> heapify([1, 2, 3, 4, 5, 6, 7])
    [7, 5, 6, 4, 2, 1, 3]


    #if (self.capacity < len(alist)):
        #self.heap = [None] * (len(alist) + 1)
    #else:
        #self.heap = [None] * (self.get_capacity() + 1)
    length = len(alist) + 1
    ints = []
    size = 0
    for i in range(1, length):
        ints[i] = alist[i - 1]
        size += 1
    print(ints)
    #        print(self.size)
    parent = size // 2
    for i in range(parent, 0, -1):
        #            print(i)
        sift_down(i)
        print(ints)
    """

    counter = len(ints)-1

    while counter != -1:
        ints = sift_down(ints, counter)
        counter -= 1

    return ints




def insert(heap: List[int], val: int) -> List[int]:
    """
    Return a max-heap with the given value added, using the sift-up operation
    to restore the Heap Property as necessary.

    >>> insert([6, 5, 4, 3, 2, 1], 7)
    [7, 5, 6, 3, 2, 1, 4]
    """

    heap.append(val)

    return sift_up(heap, len(heap)-1)


def remove(heap: List[int]) -> Tuple[int, List[int]]:
    """
    Return a tuple containing the removed value (previously at the root of the
    max-heap) along with the updated max-heap, using the sift-down operation to
    restore the Heap Property as necessary. If the heap is empty, raise a
    ValueError.

    >>> remove([7, 6, 5, 4, 3, 2, 1])
    (7, [6, 4, 5, 1, 3, 2])
    """

    if heap == []:
        raise ValueError
    else:
        temp_start = heap[0]
        if len(heap) == 1:
            heap = []
        else:
            heap[0] = heap.pop()
            sift_down(heap, 0)

    return temp_start, heap

