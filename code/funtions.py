# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)
# my_list.pop()
# print(my_list)
# my_list.insert(3, 4)  # insert no. 4 at index 3
# my_list.insert(4, 5)
# my_list.insert(0, 0)
# print(my_list)
# help(my_list.insert)

def say_hello():
    print('Hello Python Devs.!')


def say_hi(name='Default'):
    say_hello()
    return f'Hello {name}'


print(say_hi("ManiG"))
print(say_hi())


def print_result(a, b):
    print(a + b)


def return_result(x, y):
    return x + y


print_result(10, 20)
result = return_result(10, 20)
print(result)
print_result('10', '20')  # this gives 1020 as the output as have to be careful with the types


def even_no_check(number):
    return number % 2 == 0


print('Is 20 even: ', even_no_check(20))
print('Is 33 even: ', even_no_check(33))


# return true if any no. is even inside a list
def list_even_no_check(input_list):
    for no in input_list:
        if no % 2 == 0:
            return True
        else:
            pass
            # return False
    return False


def list_even_no_check_list_comprehension(number_list):
    if [num for num in number_list if num % 2 == 0]:
        return True
    else:
        pass
        # return False
    return False


print('even no check: ', list_even_no_check([1, 3, 5, 7]))
print('even no check using list comprehension: ', list_even_no_check_list_comprehension([1, 3, 5, 7]))
print('even no check: ', list_even_no_check([1, 3, 5, 8]))
print('even no check using list comprehension: ', list_even_no_check_list_comprehension([1, 3, 5, 8]))


#  return all even no's in the list
def all_even_nos_list(input_list):
    even_nos_list = []
    for number in input_list:
        if number % 2 == 0:
            even_nos_list.append(number)
        else:
            pass
    return even_nos_list


print("print all even no's in the list: ", all_even_nos_list([1, 3, 2, 5, 8, 11, 10]))

## tuple unpacking

stock_prices = [('APPL', 300), ('GOOG', 3000), ('AMAZ', 4000), ('MSFT', 250), ('EXPE', 200)]

for item in stock_prices:
    print(f'Stock pairs: {item}')

for ticker, price in stock_prices:
    print(f'Stock name: {ticker}')
    print(f'Stock price: {price}')

## need to find employee of the year i.e, the employee working max. hours
weekly_work_hours = [('MANI', 50), ('MAO', 80), ('AMAN', 60), ('KISH', 40), ('RAJ', 70)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for (key, value) in work_hours:
        if value > current_max:
            current_max = value
            employee_of_month = key
        else:
            pass
    return (employee_of_month, current_max)
    # print(f'Winner pair approach 1: ({employee_of_month}, {current_max}) ')


# # approach-2
#     output = [item for item in work_hours if item[0] == current_max or item[1] == current_max]
#     print(f'Winner pair approach 2: {output}')


print(employee_check(weekly_work_hours))
name, hours = employee_check(weekly_work_hours) # tuple unpacking
print((name, hours))


# Interaction between functions
my_example = [1, 2, 3, 4, 5, 6, 7, 8, 9]
from random import shuffle
shuffle(my_example)
# print(my_example)


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


# print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(shuffle_list([' ', 'O', ' '])) # game list


# def player_guess():
#     guess = ''
#     while guess not in ['0', '1', '2']:
#         guess = input('Pick a number: 0, 1 or 2')
#
#     return int(guess)


# my_index = player_guess()
# print(my_index)


def check_guess(my_list, my_guess):
    if my_list[my_guess] == 'O':
        print("That's Correct.!")
    else:
        print('Wrong guess, sorry try again later')
        print(my_list)


## INITIAL LIST
my_list = [' ', 'O', ' ']

## SHUFFLE LIST
mixedup_list = shuffle_list(my_list)

## USER GUESS
# guess = player_guess()

## CHECK GUESS
# check_guess(mixedup_list, guess)


## arguments (*args) and keyword arguments (**kargs)

# function should return 5% of the sum of the 2 parameters being passed to the function.
def myfunc(a, b):
    return sum((a, b)) * 0.05


print(myfunc(60, 140)) # 10.0

#Note: *args will allow us to take an arbitrary no. of parameters which makes it easy to handle by passing
#Note: by passing *args we don't need to know on how many arguments are passed to the function
#Note: *args --> this is considered as a tuple of arguments coming in
#Note: i.e, the user can pass in as many parameters as they want but inside the *args they are treated as tuple
#Note: args can be anything else as its an arbitrary choice but its a good practice but what's mandatory is * before that argument
#Note: similarly to handle a bunch of keyworded arguments we have **kwargs


def myfunc(*args):
    return sum(args) * 0.05


print(myfunc(40, 60))
print(myfunc(40, 60, 100))
print(myfunc(40, 60, 100, 150, 50))
print(myfunc(40, 60, 100, 200, 300, 400, 500))


def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I donot have the fruit of my choice')

myfunc(fruit='apple', veggie='spinach', movie='3 Idiots', brand='Apple')
#Note: *args --> would return a tuple whereas **kwargs would return a dictionary


def my_new_func(**milkchocolate):
    print(milkchocolate)

my_new_func(fruit='apple', veggie='spinach', movie='3 Idiots', brand='Apple') #output: {'fruit': 'apple', 'veggie': 'spinach', 'movie': '3 Idiots', 'brand': 'Apple'}


def my_unique_func(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))

my_unique_func(10, 20, 30, 40, 50, fruit='apple', veggie='spinach', movie='3 Idiots', brand='Apple', food='dim sum')
#Note: positional argument (*args) cannot be passed into the function after keyword argument (**kwargs)


## Pick Evens: Define a func. called myfunc that takes in an arbitrary number of arguments, and returns
## a list containing only those arguments that are even.
def myfunc_even(*args):
    return [element for element in args if element % 2 == 0]

print(myfunc_even(10, 20, 21, 23, 25, 28))


## skyline: define a func that takes in  a string, and returns a matching string where every even letter
## is uppercase, and every odd letter is lowercase. Assume that string only contains letters.

def myfunc_skyline(str):
    final_str = ""
    index = 0
    for every_char in str:
        if index % 2 == 0:
            final_str += every_char.upper()
        else:
            final_str += every_char.lower()
        index += 1
    return final_str

print(myfunc_skyline("Anthropomorphism")) #output: AnThRoPoMoRpHiSm








