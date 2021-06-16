# Name:         Sankalp Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Postfix-It
# Term:         Winter 2021

from typing import List

def main() -> None:
    """
    Iteratively prompt the user for an infix expression and display both the
    postfix equivalent and, on the next line, the result as a float (even if it
    is a whole number) rounded to 3 decimal places. Assume the infix expression
    is properly formatted.
    """
    while True:
        try:
            infix = input(">>> ")

            postfix = infix_to_postfix(infix)
            print(postfix)

            postfix_result = postfix_eval(postfix)
            print(postfix_result)


        except EOFError:  # loop breaks with CTRL+d
            break
    print()  # empty line prints before program ends
    # end of main (no return statement is equivalent to |return None|)


# insert additional function definitions below this line
def infix_to_postfix(infix: str) -> str:
    """
       Converts infix to postfix. If infix is None, it returns none.

       >>> 3 + 4
       >>> infix_to_postfix(infix)
       3 4 +
    """

    if infix is None:
        return None

    infix_list = list(infix.split(" "))

    if len(infix_list) == 1:
        return infix

    # create a empty list to take operators in and out of
    temp_list: List[str] = []
    # keep adding to this string
    postfix = ''

    for char in range(len(infix_list)):
        if ('-' in infix_list[char] and len(infix_list[char]) > 1) \
                or '.' in infix_list[char]:
            postfix += ' ' + infix_list[char]

        elif infix_list[char].isalnum():
            postfix += ' ' + infix_list[char]

        #if infix_list[char].isalnum():
            #postfix += ' ' + infix_list[char]

        elif infix_list[char] == '(':
            temp_list.append(infix_list[char])
        elif infix_list[char] == ')':
            while len(temp_list) != 0 and temp_list[-1] != '(':
                postfix += ' ' + temp_list.pop()

            temp_list.pop()  # for the '('
        else:

            if operator_priority(infix_list[char]) == 0:
                return str(ValueError('Invalid Operator'))
            while len(temp_list) != 0 and \
                operator_priority(infix_list[char]) <= \
                    operator_priority(temp_list[-1]):
                postfix += ' ' + temp_list.pop()
            temp_list.append(infix_list[char])

    while len(temp_list) != 0:
        postfix += ' ' + temp_list.pop()


    return postfix.strip()



def postfix_eval(postfix: str) -> str:

    if postfix is None or postfix == 'Invalid Operator':
        return None

    postfix_list = list(postfix.split(" "))
    #print(postfix_list)

    if len(postfix_list) == 1 and postfix_list[0].isnumeric():
        return f'{float(postfix_list[0]):.3f}'

    if len(postfix_list) == 1 and not postfix_list[0].isnumeric():
        return None

    temp_list: List[float] = []
    for char in range(len(postfix_list)):
        if postfix_list[char] in '+ - * / ^':
            first_op = temp_list[-1]
            temp_list.pop()
            second_op = temp_list[-1]
            temp_list.pop()
            if postfix_list[char] == '+':
                result = first_op + second_op
            elif postfix_list[char] == '-':
                result = second_op - first_op
            elif postfix_list[char] == '*':
                result = second_op * first_op
            elif postfix_list[char] == '/':
                result = second_op / first_op
            elif postfix_list[char] == '^':
                result = second_op ** first_op
            temp_list.append(float(result))
        else:
            temp_list.append(float(postfix_list[char]))

# temp_list[0] = float(temp_list[0])
# print('final answer: ' + f'{temp_list[0]:.3f}' + str(type(temp_list[0])))
    return f'{temp_list[0]:.3f}'


# this method is to check for which operator is more powerful
def operator_priority(operator: str) -> int:

    """
       Find out which operator has higher
       precendent and return a number accordingly.

       >>> '*'
       >>> operator_priority(operator)
       2
    """
    if operator == '^':
        return 3  # exponents have the highest precedence
    elif operator == '*' or operator == '/':
        return 2  # mul and div are second in line
    elif operator == '+' or operator == "-":
        return 1  # add and sub are always done last
    else:
        return 0



# do not add code below this line
if __name__ == "__main__":  # runs main with command |python3 postfixit.py|
    main()
