# Name:         Sankalp Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Postfix-It
# Term:         Winter 2021

import unittest

#from postfixit import postfix_eval
#from postfixit import infix_to_postfix

import postfixit


class TestPostfixEval(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertEqual(postfixit.postfix_eval('2 3 1 * + 9 -'),
                               '-4.000')

    def test_postfix_eval_02(self):
        self.assertEqual('757.000',
                               postfixit.postfix_eval("100 200 + 2 / 5 * 7 +"))

    def test_postfix_eval_03(self):
        self.assertEqual('18.000',
                               postfixit.postfix_eval("5 2 4 * + 7 2 - "
                                                      "4 6 2 / 2 - * + 4 - +"))

    def test_postfix_eval_04(self):
        self.assertEqual('12.000', postfixit.postfix_eval("12"))

    def test_postfix_eval_05(self):
        self.assertEqual(postfixit.postfix_eval("10 5 + 5 / 3 * 10 *"),
                               '90.000')

class TestInfixToPostfix(unittest.TestCase):
    def test_infix_to_postfix_01(self):
        self.assertEqual(postfixit.infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(postfixit.infix_to_postfix("6"), "6")

    def test_infix_to_postfix_02(self):
        self.assertEqual(postfixit.infix_to_postfix("( 5 + 20 ) + ( 5 * 3 )")
                         , "5 20 + 5 3 * +")
        self.assertEqual(postfixit.infix_to_postfix("2 - 1"), "2 1 -")
    def test_infix_to_postfix_03(self):
        self.assertEqual(postfixit.infix_to_postfix("5 + 5"),
                         "5 5 +")

    def test_infix_to_postfix_04(self):
        self.assertEqual(postfixit.infix_to_postfix(None), None)

    def test_infix_to_postfix_05(self):
        self.assertEqual(postfixit.infix_to_postfix("3 + 4 * ( 6 ^ 9 )"),
                         "3 4 6 9 ^ * +")
        #self.assertEqual(postfixit.infix_to_postfix("4 - 1"), "4 1 -")
class TestOperationsPriority(unittest.TestCase):
    def test_operator_priority_01(self):
        self.assertEqual(postfixit.operator_priority("+"), 1)

    def test_operator_priority_02(self):
        self.assertEqual(postfixit.operator_priority("-"), 1)

    def test_operator_priority_03(self):
        self.assertEqual(postfixit.operator_priority("*"), 2)

    def test_operator_priority_04(self):
        self.assertEqual(postfixit.operator_priority("^"), 3)

    def test_operator_priority_05(self):
        self.assertEqual(postfixit.operator_priority("/"), 2)


if __name__ == "__main__":
    unittest.main()
