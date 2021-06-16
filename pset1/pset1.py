# Name:         Sankalp Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set I
# Term:         Winter 2021

from typing import Optional, Tuple


# do not modify this class
class ListNode:

    def __init__(self, val: int, ref: Optional["ListNode"]) -> None:
        self.val = val
        self.ref = ref
        self.length = 0

    def __eq__(self, other: "ListNode") -> bool:
        """
        Return True if the two given lists have the same number of ListNodes and
        the same Node val at each respective position and False otherwise.

        >>> xs = ListNode(1, ListNode(2, ListNode(3, None)))
        >>> ys = ListNode(1, ListNode(2, ListNode(4, None)))
        >>> xs == ys
        False
        """
        while self is not None and other is not None:
            if self.val != other.val:
                return False
            self = self.ref
            other = other.ref
        return self is None and other is None

    def __repr__(self) -> str:
        """
        Return a string representation of the linked list. String
        representations of objects are useful for reading test suite errors.

        >>> xs = ListNode(1, ListNode(2, ListNode(3, None)))
        >>> str(xs)
        "1-2-3"
        """
        list_str = str(self.val)
        while True:
            self = self.ref
            if self is None:
                return list_str
            list_str += "-" + str(self.val)

def length(head):
    count = 0
    node = head
    while node is not None:
        count += 1  # count = count+1
        node = node.ref
    return count



def insert(head: Optional[ListNode], val: int, index: int) -> ListNode:
    """
    Return the head of a linked list with a ListNode containing val at position
    index in the list. If index is outside the bounds of the list (including if
    the initial list is empty), the new ListNode should be appended to the end.

    >>> head = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> insert(head, 4, 0)
    ListNode(4, ListNode(1, ListNode(2, ListNode(3, None))))
    """


    new_head = head
    if index > length(head):
        while (new_head.ref != None):
            new_head = new_head.ref
        new_head.ref = ListNode(val, None)
        return head
    if index == 0:
        return ListNode(val, head)
    while index != 1:
        head = head.ref
        index -= 1
    head.ref = ListNode(val, head.ref)
    return new_head



def remove(head: Optional[ListNode], index: int) -> Optional[ListNode]:
    """
    Return the head of a linked list with the ListNode at position index
    removed. If index is outside the bounds of the list, raise an IndexError.

    >>> head = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> remove(head, 0)
    ListNode(2, ListNode(3, None))
    """

    for i in range(100):
        test_head = ListNode(0, None)

    if index > length(head):
        print('hi')
        IndexError()

    if head == None or head.val == None:
        return None

    new_head = head
    list_length = length(head)
    if index == 0:
        head = head.ref
        return head
    if index == 1 and list_length == 2:
        head.ref = None
        return head

    if index == length(head)-1:
        while new_head.ref.ref != None:
            new_head = new_head.ref
        new_head.ref = None
        return head
    else:
        for i in range(0, index-1):
            new_head = new_head.ref
        new_head.ref = new_head.ref.ref

        return head


def index(head: Optional[ListNode], val: int) -> int:
    """
    Return the position of the ListNode containing val. If such a node does not
    exist, return -1.

    >>> head = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> index(head, 3)
    2
    """
    new_head = head
    counter = 0
    for i in range(length(head)):
        if(new_head.val != val):
            new_head = new_head.ref
            counter += 1
        else:
            return counter
    return -1


def concat(xs: Optional[ListNode],
           ys: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return the head of a linked list that represents the concatenation of the
    given lists, such that xs comes before ys.

    >>> xs = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> ys = ListNode(4, ListNode(5, None))
    >>> concat(xs, ys)
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    """

    if xs == None or xs.val == None:
        return ys

    if ys == None or ys.val == None:
        return xs

    new_head = xs
    temp_pos = new_head
    temp_head = ys

    while new_head.ref != None:
        new_head = new_head.ref
    while temp_head != None:
        new_head.ref = temp_head
        temp_head = temp_head.ref
        new_head = new_head.ref
    return temp_pos



def sum_list(head: Optional[ListNode]) -> int:
    """
    Return the sum of all integers in each ListNode in the list. If the list is
    empty, return 0.

    >>> head = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> sum_list(head)
    6
    """

    if head == None or head.val == None:
        return 0

    total = 0
    while head.ref != None:
        total += head.val
        head = head.ref
    total+=head.val

    return total


def exp_list(head: Optional[ListNode], exp: int) -> Optional[ListNode]:
    """
    Return the head of a linked list in which the integer in each ListNode has
    been raised to the exp power.

    >>> head = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> exp_list(head, 3)
    ListNode(1, ListNode(8, ListNode(27, None)))
    """

    if head == None or head.val == None:
        return None


    new_head = head

    while new_head.ref != None:
        new_head.val = new_head.val ** exp
        new_head = new_head.ref
    new_head.val = new_head.val ** exp
    return head



def fibonacci(n: int) -> ListNode:
    """
    Return a the head of a linked list representing the Fibonacci Sequence up
    to the given number of n places. Each integer in this sequence is the sum
    of the previous two integers (except for the first two integers, 0 and 1,
    which are base values not derived from adding other integers). Assume n is
    non-negative; if it is zero, return an empty list.

    >>> fibonacci(5)
    ListNode(0, ListNode(1, ListNode(1, ListNode(2, ListNode(3, None)))))
    """
    if n == 0:
        # empty_list = ListNode(None, None)
        return None

    if(n == 1):
        return ListNode(0, None)



    # fib_nums = [0, 1]
    x = False
    temp_node1 = ListNode(0, None)
    temp_node1.ref = ListNode(1, None)
    temp_node = temp_node1
    temp_node = temp_node.ref

    first_num = 0
    second_num = 1
    total = 0
    for i in range(n-2):
        total = first_num + second_num
        temp_node.ref = ListNode(total, None)
        temp_node = temp_node.ref
        first_num, second_num = second_num, total
    temp_node2 = temp_node1
    # this is to not include the last value
    #for i in range(length(head=temp_node2) - 2):
     #   temp_node2 = temp_node2.ref
    #temp_node2.ref = None

    return temp_node1




def zip_lists(xs: Optional[ListNode],
              ys: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return the head of a linked list that represents the pair-wise combination
    of the given linked lists. If one list runs out of ListNodes, append the
    remainder of the other list.

    >>> xs = ListNode(1, ListNode(2, ListNode(3, None)))
    >>> ys = ListNode(4, None)
    >>> zip_lists(xs, ys)
    ListNode(1, ListNode(4, ListNode(2, ListNode(3, None))))
    """

    # the specific if cases
    x = 0
    if xs == None and ys == None:
        return None
    if xs == None or xs.val == None:
        return ys
    if ys == None or ys.val == None:
        return xs

    if length(xs) == 1:
        temp_head = xs
        temp_head.ref = ys
        return temp_head


    if length(ys) == 1:
        temp_head = xs
        xs.ref = ListNode(ys.val, xs.ref)
        return temp_head


    # create duplicates to modify
    temp_node1 = ListNode(xs.val, None)
    head = temp_node1

    # increment x to alter between the two lists
    x += 1
    xs = xs.ref

    # alternate lists and add a node from each to a temp list (head)
        # print(counter)
    print(head)
    print(xs)
    print(ys)
    print(x)
    for i in range(length(xs) + length(ys)):
        if x % 2 == 0:
            print('adding x')
            if(length(xs) == 0):
                break
            head.ref = xs
            xs = xs.ref
            head = head.ref
            x += 1
        else:
            print('adding y')

            head.ref = ys
            ys = ys.ref
            head = head.ref
            x += 1
    return temp_node1


def unzip_list(head: Optional[ListNode]
) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    """
    Return a 2-tuple of heads of linked lists that represents the pair-wise
    separation of the given linked lists. This operation is the inverse of
    zip_lists.

    >>> head = ListNode(1, ListNode(4, ListNode(2, \
                                       ListNode(5, ListNode(3, None)))))
    >>> unzip_list(head)
    (ListNode(1, ListNode(2, ListNode(3, None))), \
     ListNode(4, ListNode(5, None)))
    """

    if (length(head) == 0):
        return (None, None)

    if(length(head) == 1):
        return (head, None)

    if(head == None):
        return None

    new_head = head
    counter = 0
    xs = ListNode(None,None)
    ys = ListNode(None,None)
    new_head1 = xs
    new_head2 = ys
    xs.val = new_head.val
    new_head = new_head.ref
    # counter += 1
    ys.val = new_head.val
    new_head = new_head.ref
    if length(xs) == 1 and length(ys) == 1 and length(head) == 2:
        print('hi')
        return (xs, ys)
    # counter +=1
    # 1-4-2-5-3
    while(new_head.ref != None):
        if(counter % 2 == 0):
            counter += 1
            xs.ref = ListNode(new_head.val,None)
            xs = xs.ref
            new_head = new_head.ref
            print(str(counter) + "xs")
            print(xs)

        else:
            counter += 1
            ys.ref = ListNode(new_head.val,None)
            ys = ys.ref
            new_head = new_head.ref
            print(str(counter) + "ys")
            print(ys)
    if(counter % 2 == 0):
        xs.ref = ListNode(new_head.val, None)
        xs = xs.ref
    else:
        ys.ref = ListNode(new_head.val, None)
        ys = ys.ref
    # print(counter)
    return (new_head1,new_head2)



