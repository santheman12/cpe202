# Name:         Sankalp Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set III
# Term:         Winter 2021

import unittest

import pset3
from pset3 import ListNode  # only allowed use of from ... import


class TestMul(unittest.TestCase):

    def test_mul_1(self):
        self.assertEqual(pset3.mul(-2, -3), 6)

    def test_mul_2(self):
        self.assertEqual(pset3.mul(-2, 5), -10)

    def test_mul_3(self):
        self.assertEqual(pset3.mul(0, -3), 0)

    def test_mul_4(self):
        self.assertEqual(pset3.mul(20, -1), -20)

    def test_mul_5(self):
        self.assertEqual(pset3.mul(0, 0), 0)




class TestExp(unittest.TestCase):

    def test_exp_1(self):
        self.assertEqual(pset3.exp(-2, 3), -8)

    def test_exp_2(self):
        self.assertEqual(pset3.exp(3, 4), 81)

    def test_exp_3(self):
        self.assertEqual(pset3.exp(2, 50), 1048576)

    def test_exp_4(self):
        self.assertEqual(pset3.exp(5, 2), 25)

    def test_exp_5(self):
        self.assertEqual(pset3.exp(0, 0), 1)




class TestFac(unittest.TestCase):

    def test_fac_1(self):
        self.assertEqual(pset3.fac(5), 120)

    def test_fac_2(self):
        self.assertEqual(pset3.fac(1), 1)

    def test_fac_3(self):
        self.assertEqual(pset3.fac(0), 1)

    def test_fac_4(self):
        self.assertEqual(pset3.fac(10), 3628800)

    def test_fac_5(self):
        self.assertEqual(pset3.fac(4), 24)


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_1(self):
        self.assertEqual(pset3.fibonacci(1, 0, 1), 0)

    def test_fibonacci_2(self):
        self.assertEqual(pset3.fibonacci(10, 0, 1), 34)

    def test_fibonacci_3(self):
        self.assertEqual(pset3.fibonacci(4, 0, 1), 2)

    def test_fibonacci_4(self):
        self.assertEqual(pset3.fibonacci(1, 0, 1), 0)

    def test_fibonacci_5(self):
        self.assertEqual(pset3.fibonacci(6, 0, 1), 5)



class TestMakeSubstring(unittest.TestCase):

    def test_make_substring_1(self):
        self.assertEqual(pset3.make_substring("COMPUTER", 0, 10, 3), "CPE")

    def test_make_substring_2(self):
        self.assertEqual(pset3.make_substring("CAT", 0, 5, 2), "CT")

    def test_make_substring_3(self):
        self.assertEqual(pset3.make_substring("CAT", 4, 1, 2), "")

    def test_make_substring_4(self):
        self.assertEqual(pset3.make_substring("DOG", 4, 1, 3), "")

    def test_make_substring_5(self):
        self.assertEqual(pset3.make_substring("", 4, 1, 3), "")




class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome_1(self):
        self.assertEqual(pset3.is_palindrome("tacocat"), True)

    def test_is_palindrome_2(self):
        self.assertEqual(pset3.is_palindrome("palindrome"), False)

    def test_is_palindrome_3(self):
        self.assertEqual(pset3.is_palindrome("tate"), False)

    def test_is_palindrome_4(self):
        self.assertEqual(pset3.is_palindrome('am'), False)

    def test_is_palindrome_5(self):
        self.assertEqual(pset3.is_palindrome("racecar"), True)




class TestSwapChars(unittest.TestCase):

    def test_swap_chars_1(self):
        self.assertEqual(pset3.swap_chars("AaBbCcD"), "aAbBcCD")

    def test_swap_chars_2(self):
        self.assertEqual(pset3.swap_chars("CaDe"), "aCeD")

    def test_swap_chars_3(self):
        self.assertEqual(pset3.swap_chars("C"), "C")

    def test_swap_chars_4(self):
        self.assertEqual(pset3.swap_chars("AcE"), "cAE")

    def test_swap_chars_5(self):
        self.assertEqual(pset3.swap_chars(""), "")




class TestLength(unittest.TestCase):

    def test_length_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset3.length(head), 3)

    def test_length_2(self):
        head = ListNode(1, None)
        self.assertEqual(pset3.length(head), 1)

    def test_length_3(self):
        head = None
        self.assertEqual(pset3.length(head), 0)

    def test_length_4(self):
        head = ListNode(5, ListNode(23, ListNode(3,
            ListNode(2, ListNode(9, None)))))
        self.assertEqual(pset3.length(head), 5)

    def test_length_5(self):
        head = ListNode(2, ListNode(9, None))
        self.assertEqual(pset3.length(head), 2)


class TestFindMax(unittest.TestCase):

    def test_find_max_1(self):
        head = ListNode(2, ListNode(3, ListNode(4, ListNode(1, None))))
        self.assertEqual(pset3.find_max(head), 4)

    def test_find_max_2(self):
        head = ListNode(8, ListNode(9, None))
        self.assertEqual(pset3.find_max(head), 9)

    def test_find_max_3(self):
        head = ListNode(4, ListNode(4, None))
        self.assertEqual(pset3.find_max(head), 4)

    def test_find_max_4(self):
        head = ListNode(4, ListNode(4, ListNode(1, None)))
        self.assertEqual(pset3.find_max(head), 4)

    def test_find_max_5(self):
        head = ListNode(0, None)
        self.assertEqual(pset3.find_max(head), 0)




class TestReverse(unittest.TestCase):

    def test_reverse_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, None)))
        self.assertEqual(pset3.reverse(head, None),
                         ListNode(3, ListNode(2, ListNode(1, None))))

    def test_reverse_2(self):
        head = ListNode(1, ListNode(2, None))
        self.assertEqual(pset3.reverse(head, None),
                         ListNode(2, ListNode(1, None)))

    def test_reverse_3(self):
        head = ListNode(1, None)
        self.assertEqual(pset3.reverse(head, None),
                         ListNode(1, None))

    def test_reverse_4(self):
        head = None
        self.assertEqual(pset3.reverse(head, None),
                         None)

    def test_reverse_5(self):
        head = ListNode(5, ListNode(6, ListNode(3, None)))
        self.assertEqual(pset3.reverse(head, None),
                         ListNode(3, ListNode(6, ListNode(5, None))))


class TestNestingDollConstructor(unittest.TestCase):

    def test_nesting_doll_constructor_1(self):
        doll = pset3.NestingDoll(3)
        self.assertEqual(doll.inner.inner.inner, None)

    def test_nesting_doll_constructor_2(self):
        doll = pset3.NestingDoll(1)
        self.assertEqual(doll.inner, None)

    def test_nesting_doll_constructor_3(self):
        doll = pset3.NestingDoll(4)
        self.assertEqual(doll.inner.inner.inner.inner, None)

    def test_nesting_doll_constructor_4(self):
        doll = pset3.NestingDoll(2)
        self.assertEqual(doll.inner.inner, None)

    def test_nesting_doll_constructor_5(self):
        doll = pset3.NestingDoll(6)
        self.assertEqual(doll.inner.inner.inner.inner.inner.inner, None)




class TestNestingDollEquals(unittest.TestCase):

    def test_nesting_doll_equals_1(self):
        self.assertEqual(pset3.NestingDoll(1), pset3.NestingDoll(1))

    def test_nesting_doll_equals_2(self):
        self.assertNotEqual(pset3.NestingDoll(1), pset3.NestingDoll(2))

    def test_nesting_doll_equals_3(self):
        self.assertEqual(pset3.NestingDoll(2), pset3.NestingDoll(2))

    def test_nesting_doll_equals_4(self):
        self.assertNotEqual(pset3.NestingDoll(2), pset3.NestingDoll(5))

    def test_nesting_doll_equals_5(self):
        self.assertEqual(pset3.NestingDoll(5), pset3.NestingDoll(5))




class TestNestingDollString(unittest.TestCase):

    def test_nesting_doll_string_1(self):
        self.assertEqual(str(pset3.NestingDoll(3)), "((8))")

    def test_nesting_doll_string_2(self):
        self.assertEqual(str(pset3.NestingDoll(1)), "8")

    def test_nesting_doll_string_3(self):
        self.assertEqual(str(pset3.NestingDoll(4)), "(((8)))")

    def test_nesting_doll_string_4(self):
        self.assertEqual(str(pset3.NestingDoll(2)), "(8)")

    def test_nesting_doll_string5(self):
        self.assertEqual(str(pset3.NestingDoll(5)), "((((8))))")


if __name__ == "__main__":
    unittest.main()
