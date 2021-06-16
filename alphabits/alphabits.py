# Name:         Sankalp Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   AlphaBits
# Term:         Winter 2021

from typing import Optional, List


class HuffmanNode:
    
    def __init__(self, char: str, count: int, l_ref: Optional["HuffmanNode"],
                 r_ref: Optional["HuffmanNode"]) -> None:
        self.char = char
        self.count = count
        self.l_ref = l_ref
        self.r_ref = r_ref

    def __eq__(self, other: Optional["HuffmanNode"]) -> bool:
        if other is None:
            return False
        return (self.char == other.char and self.count == other.count
                and self.l_ref == other.l_ref and self.r_ref == other.r_ref)

    def __repr__(self) -> str:
        s = f"{self.char}:{self.count}"
        if self.l_ref is not None:
            s += " " + str(self.l_ref)
        if self.r_ref is not None:
            s += " " + str(self.r_ref)
        return s


def create_tree(chars: str) -> HuffmanNode:
    """
    Build a Huffman tree by analyzing the frequency of each character in the
    given string and return the root node of the tree.
    """

    if len(chars) == 0:
        return None

    node_list: List[HuffmanNode] = []

    if len(node_list) == 1:
        return node_list[0]

    while len(chars) != 0:
        x = 0
        for char in chars:
            if chars[0] == char:
                x += 1
        node_list.append(HuffmanNode(chars[0], x, None, None))

        chars = chars.replace(chars[0], "")
        #print(node_list)
        #print(str(chars))

    while len(node_list) != 2:
        temp_p1 = lowest_val(node_list)
        temp_p2 = lowest_val(node_list)

        #print(str(temp_p1) + ' temp 1')
        #print(str(temp_p2) + ' temp 2')
        if ord(temp_p1.char) > ord(temp_p2.char):
            parent_rn = HuffmanNode(temp_p2.char,
            temp_p1.count + temp_p2.count, temp_p1, temp_p2)
        elif ord(temp_p1.char) < ord(temp_p2.char):
            parent_rn = HuffmanNode(temp_p1.char,
            temp_p1.count + temp_p2.count, temp_p1, temp_p2)
        node_list.append(parent_rn)

        #print(str(parent_rn) + ' parent rn')

    # if it is only two vals
    temp_p1 = lowest_val(node_list)
    temp_p2 = lowest_val(node_list)

    if ord(temp_p1.char) > ord(temp_p2.char):
        parent_rn = HuffmanNode(temp_p2.char,
        temp_p1.count + temp_p2.count, temp_p1, temp_p2)
    elif ord(temp_p1.char) < ord(temp_p2.char):
        parent_rn = HuffmanNode(temp_p1.char,
        temp_p1.count + temp_p2.count, temp_p1, temp_p2)

    return parent_rn


def lowest_val(vals: List[HuffmanNode]) -> HuffmanNode:
    print(str(vals) + ' + vals')
    print(type(vals[0]))
    min_val = vals[0]
    for val in vals:
        #print(str(min_val) + ' the min val')
        #print(str(vals) + ' vals')
        if val.count < min_val.count:
            min_val = val
        elif val.count == min_val.count:
            #print(str(val.count) + ' the val count')
            if ord(val.char) < ord(min_val.char):
                min_val = val
    vals.remove(min_val)
    print(str(min_val) + ' min val')
    return min_val


def encode(chars: str, root: Optional[HuffmanNode]) -> str:
    """
    Return the Huffman code (bit string) of the given characters, using the
    provided Huffman tree.
    """

    print(type(root))
    print(type(root.char))
    if chars is None:
        return ''
    res = ''
    for char in chars:
        print('i')
        res = res + char_leaf(root, char, '')

    return res


def char_leaf(root: Optional[HuffmanNode],
              char: str, res: str) -> str:
    """
    Accepts the huffman tree, the char we need to find, and
    the ending string. This function finds the char in the leaves
    and returns the bit string for that char
    """
    if root.char != char and root.l_ref is None and \
       root.r_ref is None:
        return ''

    if root.char == char and root.l_ref is None and \
       root.r_ref is None:
        return res

    print(char_leaf(root.r_ref, char, res + '1') + \
           char_leaf(root.l_ref, char, res + '0'))

    return char_leaf(root.r_ref, char, res + '1') + \
           char_leaf(root.l_ref, char, res + '0')


def decode(bits: str, root: Optional[HuffmanNode]) -> str:
    """
    Return the original encoded string from the given string of bits, using the
    provided Huffman tree.
    """
    if root is None:
        return ''

    if bits is None:
        return ''

    res = ''
    temp_node = root

    for bit in bits:
        if temp_node.r_ref is None and temp_node.l_ref is None:
            print(res)
            res = res + temp_node.char
            temp_node = root
            if bit == '0':
                print('in 0')
                temp_node = temp_node.l_ref
            elif bit == '1':
                temp_node = temp_node.r_ref
        elif bit == '0':
            print('in 0')
            temp_node = temp_node.l_ref
        elif bit == '1':
            temp_node = temp_node.r_ref
        print(res)
    res = res + temp_node.char
    print(res)
    return res


# do not modify code below this line
def main() -> None:
    chars = input("Treeify: ")  # initial chars used to create Huffman tree
    root = create_tree(chars)
    while True:
        try:
            chars = input(">>> ")  # chars to encode
            code = encode(chars, root)
            assert decode(code, root) == chars
            print(code)
        except AssertionError:
            print("Encode/Decode Failure")
        except EOFError:  # loop breaks with CTRL+d
            break
    print()


if __name__ == "__main__":
    main()
