# Name:         Sankalp Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set II
# Term:         Winter 2021

from typing import Optional, Tuple


# do not modify this class
class StackNode:
    """
    A StackNode is like a ListNode except that its ref attribute may only be
    accessed in the push or pop functions, to be defined below.
    """

    def __init__(self, val: int, ref: Optional["StackNode"]) -> None:
        self.val = val
        self.ref = ref
        self.num_items = 0

    def __eq__(self, other: "StackNode") -> bool:
        """
        Return True if the two given stacks have the same number of StackNodes
        and the same StackNode val at each respective position and False
        otherwise.

        >>> xs = StackNode(1, StackNode(2, StackNode(3, None)))
        >>> ys = StackNode(1, StackNode(2, StackNode(4, None)))
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
        Return a string representation of the stack. String representations of
        objects are useful for reading test suite errors.

        >>> xs = StackNode(1, StackNode(2, StackNode(3, None)))
        >>> str(xs)
        "1-2-3"
        """
        stack_str = str(self.val)
        while True:
            self = self.ref
            if self is None:
                return stack_str
            stack_str += "-" + str(self.val)



def push(top: Optional[StackNode], new: StackNode) -> StackNode:
    """
    Add the given new StackNode to the top of the stack and return a reference
    to it. Assume the new StackNode's ref attribute is None.

    >>> top = StackNode(2, StackNode(3, None))
    >>> push(top, StackNode(1, None))
    StackNode(1, StackNode(2, StackNode(3, None)))
    """

    if top == None:
        return new
    elif new == None:
        return top
    elif top == None and new == None:
        return None
    else:
        new_top = new
        new.ref = top
        return new_top



def pop(top: Optional[StackNode]) -> Tuple[StackNode, Optional[StackNode]]:
    """
    Remove the StackNode at the top of the stack and return the popped StackNode
    (with its ref set to None) and the reference to the new top of the stack. If
    the stack is initially empty, raise a ValueError.

    >>> top = StackNode(1, StackNode(2, StackNode(3, None)))
    >>> pop(top)
    (StackNode(1, None), StackNode(2, StackNode(3, None)))
    """

    #print(length(top))

    if top == None:
        raise ValueError
    else:
        new_top = top
        top = top.ref
        new_top.ref = None
    return(new_top, top)


def move(xs: StackNode,
         ys: Optional[StackNode]) -> Tuple[Optional[StackNode], StackNode]:
    """
    Pop the top StackNode from xs and push it to ys. Return references to the
    tops of both stacks.

    >>> xs = StackNode(1, StackNode(2, StackNode(3, None)))
    >>> ys = None
    >>> move(xs, ys)
    (StackNode(2, StackNode(3, None)), StackNode(1, None))
    """
    if xs == None:
        return (None, None)
    else:
        results_from_pop = pop(xs)
        ys = push(ys, results_from_pop[0])
        return (results_from_pop[1], ys)




def flip_stack(top: Optional[StackNode]) -> Optional[StackNode]:
    """
    Return the reversal of the given stack by creating an empty stack and moving
    StackNodes onto it.

    >>> top = StackNode(1, StackNode(2, StackNode(3, None)))
    >>> flip_stack(top)
    StackNode(3, StackNode(2, StackNode(1, None)))
    """

    if top is None or top.val is None:
        return None

    new_stack = None

    while top is not None:
        popped = pop(top)
        top = popped[1]
        new_stack = push(new_stack, popped[0])
    return new_stack


def concat(xs: Optional[StackNode],
           ys: Optional[StackNode]) -> Optional[StackNode]:
    """
    Return the top of a stack that represents the concatenation of the given
    stacks, such that xs comes before ys.

    >>> xs = StackNode(1, StackNode(2, StackNode(3, None)))
    >>> ys = StackNode(4, StackNode(5, None))
    >>> concat(xs, ys)
    StackNode(1, StackNode(2, StackNode(3, StackNode(4, StackNode(5, None)))))
    """

    if xs is None:
        return ys
    if ys is None:
        return xs
    if xs is None and ys is None:
        return None

    new_stack = flip_stack(xs)
    while ys is not None:
        popped = pop(ys)
        ys = popped[1]
        new_stack = push(new_stack, popped[0])
    return flip_stack(new_stack)



def pop_all(top: Optional[StackNode], val: int) -> Optional[StackNode]:
    """
    Return a stack with all StackNodes containing the given integer value
    removed from the given stack.

    >>> top = StackNode(1, StackNode(2, StackNode(1, StackNode(3, None))))
    >>> pop_all(top, 1)
    StackNode(2, StackNode(3, None))
    """

    if top is None:
        return None

    new_stack = None
    while top is not None:
        if top.val == val:
            popped = pop(top)
            top = popped[1]
        else:
            popped_if_not_eq = pop(top)
            top = popped_if_not_eq[1]
            new_stack = push(new_stack, popped_if_not_eq[0])

    return flip_stack(new_stack)


def zip_stacks(xs: Optional[StackNode],
               ys: Optional[StackNode]) -> Optional[StackNode]:
    """
    Return the top of a stack that represents the pair-wise combination of the
    given stacks. If one stack runs out of StackNodes, append the remainder of
    the other stack.

    >>> xs = StackNode(1, StackNode(2, StackNode(3, None)))
    >>> ys = StackNode(4, None)
    >>> zip_stacks(xs, ys)
    StackNode(1, StackNode(4, StackNode(2, StackNode(3, None))))
    """

    if xs is None:
        return ys
    if ys is None:
        return xs
    if xs is None and ys is None:
        return None

    new_stack = None
    counter = 0
    while xs is not None or ys is not None:
        print(counter)
        if counter % 2 == 0:
            if xs is not None:
                popper = pop(xs)
                new_stack = push(new_stack, popper[0])
                xs = popper[1]
        else:
            if ys is not None:
                popper = pop(ys)
                new_stack = push(new_stack, popper[0])
                ys = popper[1]
        counter += 1
    return flip_stack(new_stack)


def unzip_stack(top: Optional[StackNode]
) -> Tuple[Optional[StackNode], Optional[StackNode]]:
    """
    Return a 2-tuple of tops of stacks that represents the pair-wise separation
    of the given stacks. This operation is the inverse of zip_stacks.

    >>> top = StackNode(1, StackNode(4, StackNode(2, \
                                        StackNode(5, StackNode(3, None)))))
    >>> unzip_stack(top)
    (StackNode(1, StackNode(2, StackNode(3, None))), \
     StackNode(4, StackNode(5, None)))
    """

    if top is None:
        return (None, None)


    xs = None
    ys = None
    counter = 0
    while top is not None:
        if counter % 2 == 0:
            if top is not None:
                popper = pop(top)
                xs = push(xs, popper[0])
                top = popper[1]
        else:
            if top is not None:
                popper = pop(top)
                ys = push(ys, popper[0])
                top = popper[1]
        counter += 1

    return(flip_stack(xs), flip_stack(ys))



def sort_stack(top: Optional[StackNode]) -> Optional[StackNode]:
    """
    Return a stack in with the StackNodes from the given stack are sorted in
    ascending order by their integer values.

    It is recommended to create two empty stacks: one to which StackNodes are
    temporarily moved, and another to store the sorted StackNodes.

    >>> top = StackNode(5, StackNode(2, StackNode(8, None)))
    >>> sort_stack(top)
    StackNode(2, StackNode(5, StackNode(8, None)))
    """

    if top is None:
        return None

    temp_stack = None
    while top is not None:
        popper = pop(top)
        temp = popper[0]
        top = popper[1]

        # print('this is the temp top')
        print('temp'+str(temp))
        # print('this it the remaining top')
        print("top" + str(top))

        print('temp_stack before if: ' + str(temp_stack))

        while temp_stack is not None and temp_stack.val > temp.val:
            print('top of stack is greater than temp')
            temp_popper = pop(temp_stack)
            temp_stack = temp_popper[1]
            temp_stack_top = temp_popper[0]
            # print('we took it out of temp stack, temp stack now equals')
            # print(temp_stack)

            top = push(top, temp_stack_top)
            # print('top now equals')
            # print(top)

        # print('the temp value is greater then temp stacks val')
        print(temp_stack)
        temp_stack = push(temp_stack, temp)
        # print('this is the temp_stack')
        print('temp_stack' + str(temp_stack))

    return flip_stack(temp_stack)
