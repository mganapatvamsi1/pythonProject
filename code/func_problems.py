"""
warmup problems
"""


## 1 ## LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_numbers(a, b):
    # if both a and b are even then return a as a is the smaller.
    if a % 2 == 0 and b % 2 == 0:
        ## approach-1
        # if a < b:
        #     return a
        # elif b < a:
        #     return b
        # else:
        #     pass
        ## approach-2
        return min(a, b)

    else:  # if one or both of them are odd then return the max value out of them.
        ## approach-1
        # if a > b:
        #     return a
        # elif b > a:
        #     return b
        # else:
        #     pass
        ## approach-2
        return max(a, b)


print("both are even: ", lesser_of_two_numbers(4, 8))  # 4
print("one of them is odd: ", lesser_of_two_numbers(3, 8))  # 8
print("both are odd: ", lesser_of_two_numbers(3, 9))  # 9

## 2 ## ANIMAL CRACKERS: Write a function that takes a two-word string and returns True if both words begin with same letter
"""
  animal_crackers('Levelheaded Llama') --> True
  animal_crackers('Crazy Kangaroo') --> False
"""


def animal_crackers(text):
    ## approach-1
    # word_list = text.lower().split()
    # if word_list[0][0] == word_list[1][0]:
    #     return True
    # else:
    #     return False

    ## approach-2
    # word_list = text.lower().split()
    # first = word_list[0]
    # second = word_list[1]
    # return first[0] == second[0]

    ## approach-3
    word_list = text.lower().split()
    return word_list[0][0] == word_list[1][0]


print('animal crackers1: ', animal_crackers('Levelheaded Llama'))  # True
print('animal crackers2: ', animal_crackers('Crazy Kangaroo'))  # False

## 3 ## MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
"""
    makes_twenty(20,10) --> True
    makes_twenty(12,8) --> True
    makes_twenty(2,3) --> False
"""


def sum_twenty(num1, num2):
    ## approach-1
    # if num1 == 20 or num1 == 20:
    #     return True
    # elif num1 + num2 == 20:
    #     return True
    # else:
    #     return False
    ## approach-2
    return (num1 + num2 == 20) or num1 == 20 or num2 == 20


print(sum_twenty(20, 10))  # True
print(sum_twenty(12, 8))  # False
print(sum_twenty(2, 3))  # False

"""
Level-1 problems
"""

## 1 ## OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
"""
old_macdonald('macdonald') --> MacDonald
Note: `'macdonald'.capitalize()`
returns
`'Macdonald'`
"""


def capitalize_two_letters_func(name):
    # name = name.lower()
    # ## Approach-1
    # # result_name = ''.join(name[0].upper() + name[1] + name[2] + name[3].upper() + name[4:] for name in name.split())
    # # return result_name
    # ## Approach-2
    # return ''.join(name[0].upper() + name[1] + name[2] + name[3].upper() + name[4:])
    ## Approach-3
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()


print(capitalize_two_letters_func("macdonaLD"))
print(capitalize_two_letters_func("manikantaG"))

## 2 ## MASTER YODA: Given a sentence, return a sentence with the words reversed
"""
Ex:     master_yoda('I am home') --> 'home am I'
        master_yoda('We are ready') --> 'ready are We'
"""


def reverse_str(given_str):
    # return given_str[::-1] # this would reverse the complete string
    str_list = given_str.split(' ')
    # return " ".join(str_list[-1::-1]) ## Approach-1:
    ##Approach-2
    reverse_word_list = str_list[::-1]
    return ' '.join(reverse_word_list)


print('rev str1: ', reverse_str('I am home'))
print('rev str2: ', reverse_str('We are ready'))
print('rev str3: ', reverse_str('Hello World'))


## 3 ## ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(number):
    ##Approach-1
    # if (90 <= number <= 110) or (190 <= number <= 210):
    #     return True
    # else:
    #     return False
    ##Approach-2
    return (abs(100 - number) <= 10) or (abs(200 - number) <= 10)


print(almost_there(104))
print(almost_there(90))
print(almost_there(150))
print(almost_there(209))

"""
Level-2 problems
"""


## 1 ##  Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums_list):
    for i in range(0, len(nums_list) - 1):
        # if nums_list[i] == 3 and nums_list[i] == nums_list[i + 1]:
        # if nums_list[i] == 3 and nums_list[i + 1] == 3:
        if nums_list[i: i + 2] == [3, 3]:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print(has_33([3, 3, 9]))

## 2 ## PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
""" Ex's:
    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""


def paper_doll(str):
    new_list = []
    for character in str:
        character = character * 3
        new_list.append(character)
    result_str = ''.join(new_list)
    # print(f'test result_str: {result_str}')
    return result_str


print('result: ', paper_doll('Hello'))


## 3 ## BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
#                  If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally,
#                  if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a, b, c):
    if a == 11 or b == 11 or c == 11:
        return (a + b + c - 10)
    else:
        if a + b + c > 21:
            return 'BUST'
        else:
            return (a + b + c)


print(blackjack(5, 6, 7))  # 18
print(blackjack(9, 9, 9))  # 'BUST'
print(blackjack(9, 9, 11))  # 19

## 4## SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
#                     and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
"""
    summer_69([1, 3, 5]) --> 9
    summer_69([4, 5, 6, 7, 8, 9]) --> 9
    summer_69([2, 1, 6, 9, 11]) --> 14
"""


def sum_numbers_ignore_six_nine(given_arr):
    total_sum = 0
    bool_flag = True
    for num in given_arr:
        while bool_flag:
            if num != 6:
                total_sum += num
                break
            else:
                bool_flag = False
                break
        while not bool_flag:
            if num != 9:
                break
            else:
                bool_flag = True
                break
    return total_sum


print(sum_numbers_ignore_six_nine([1, 3, 5]))  # 9
print(sum_numbers_ignore_six_nine([4, 5, 6, 7, 8, 9]))  # 9
print(sum_numbers_ignore_six_nine([2, 1, 6, 9, 11]))  # 14

"""
CHALLENGING PROBLEMS
"""

## 1 ## SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
"""
     spy_game([1,2,4,0,0,7,5]) --> True
     spy_game([1,0,2,4,0,5,7]) --> True
     spy_game([1,7,2,0,4,5,0]) --> False
"""


def james_bond(nums_list):
    code = [0, 0, 7, 'x']
    for num in nums_list:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works
    return len(code) == 1


print(james_bond([1, 2, 4, 0, 0, 7, 5]))
print(james_bond([1, 0, 2, 4, 0, 5, 7]))
print(james_bond([1, 7, 2, 0, 4, 5, 0]))
print('------------------------------------------------')


# name = 'RajAryan'
# print(name.split())
#
# arr = [1, 2, 3, 4]
# arr_new = []
# print('TEST: ', sum(arr))
# arr_new.append(1)
# arr_new.append(3)
# print('TEST2: ', sum(arr_new))

def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4]

for item in map(square, my_nums):
    print(item)

print('printing the square values in a list: ', list(map(square, my_nums)))
print('printing the square values in a list using lambda: ', list(map(lambda num: num ** 2, my_nums)))


def splicer(my_string):
    if len(my_string) % 2 == 0:
        return "EVEN"
    else:
        return my_string[0]


names = ['mani', 'raj', 'aryan', 'malhotra']

print('list of string names as a list based on a pattern: ', list(map(splicer, names)))

# checking whether a number is even or not
def check_even(num):
    return num % 2 == 0


def check_odd(num):
    return num % 2 != 0


new_nums = [1, 2, 3, 4, 5, 6]

print('check even no. using filter function: ', list(filter(check_even, new_nums)))  # [2, 4, 6]
print('check even no. using filter function using lambda: ', list(filter(lambda num: num % 2 == 0, new_nums)))  # [2, 4, 6]
print('check odd no. using filter function: ', list(filter(check_odd, new_nums)))  # [1, 3, 5]
print('check odd no. using filter function using lambda: ', list(filter(lambda num: num % 2 != 0, new_nums)))  # [1, 3, 5]


# Lambda function
def new_square(num): return num ** 2
print(new_square(5))

new_square_two = lambda num: num ** 2
print(new_square_two(5))


fav_names = ['mani', 'raj', 'aryan', 'malhotra', 'rahul']
print('test: ', list(map(lambda firstletter: firstletter[0], fav_names)))


## nested statements and scopes
# LEGB Rule i.e, Local, Enclosing Function Local, Global and Built-in

# example of local lambda function
local_lambda = lambda num: num**2

# example of enclosing lambda function local
# global
name = 'this is a global string'
def greet():
    # enclosing
    name = 'ManiG'
    def hello():
        # local
        name = 'I am local'
        print('Hello '+name)
    hello()

greet()


x = 25
def printer():
    x = 50
    return x

print(x)
## Note:If we declare variables inside of a function define those variables only have a scope local to that function.
## Note: If we want our local function specific assignments to be impacted globally then we need to define 'global' keyword inside the function.
## The other way to do the same as 'global' keyword is to return that x and and re-assign it again.








