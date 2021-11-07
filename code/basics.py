# dynamic typing is supported so adv. is no need to write data types but drawback is have to be careful with datatypes
my_name = 3
# Variable assignments
print(my_name, type(my_name))
my_name = ["ManiG", "Raj", "Aryan", "Malhotra"]
print(my_name, type(my_name))
my_name = False
print(my_name, type(my_name))

# Strings (syntax of slice [start:stop:step])
# start is the numerical index for the slice start
# stop is the index you will go upto (but not include)
# step is the size of the "jump" you take
my_name = 'maniG'
your_name = "tle"
print(my_name, your_name)
both_names = "  We're maniG and tLe  "
my_string = "abcdefghijk"
print(both_names)  # strip() removes the leading and trailing whitespaces
print('length of bothNames str:', len(both_names))
print('updated len of bothNames str:', len(both_names.strip()))
print('maniG \ntLe')  # escape-character (\t --> tab which gives 4 spaces whereas \n --> is newLine)
print(my_name[0], my_name[1], my_name[2], my_name[3], my_name[4])  # string indexing
print(my_name[0:4])  # string slicing (the end character is exclusive)
print(my_name[0:len(my_name)])  # (or) print(my_name[0:5])
print(my_name[0:])  # this gives the same result as the above line
print(my_name[:4])  # the last letter i.e, stop index is exclusive
print(my_string[3:6], my_string[1:3])  # to get the result of 'def' and 'bc'
print(my_string[::])  # meaning all the way from the beginning to all the way to the end
print(my_string[::2])  # step-size: go in step sizes of 2
print(my_string[1::2])
print(my_string[
      ::-1])  # this step-size would reverse the whole string (this reverses a string instead of using the for-loop and iteration)

# String properties and methods
print("mani" + "" + "kanta" + "G")  # string concatenation
# concatenation: final expected result is ManiAryan
names = "RajAryan"
extract_name = names[3:]
new_name = "Mani" + extract_name  # this '+' is called the string concatenation
print(new_name)
letter = 'G'
print(letter * 10)
upper_case_string = my_string.upper()
print(upper_case_string)
print(upper_case_string.lower())
print(my_string.split())
print(upper_case_string.split())  # organized into a list

# string formatting and printing
to_be_formatted_str = 'My name is {}'
print(to_be_formatted_str.format('ManiG'))
print(to_be_formatted_str.format('RajAryan'))  # here .format() would grab the string
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {1} {1} {1}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown',
                               q='quick'))  # assigning the variables with keywords and using those variable names
# float formatting follows "{value:width.precision f}"
result = 10 / 7
print('The result was: {r}'.format(r=result))
print('The result using float formatting was: {r:1.3f}'.format(
    r=result))  # Note: width describes how long we want the string to be
# f-strings
names = 'Ram Robert Rahim'
print('Hey, their names are {}'.format(names))
print(
    f'Hey, their names are {names}')  # called formatted string literals (f-strings). string-literals means injects the strings into the actual statement itself.
name1 = 'Ram'
name2 = 'Robert'
name3 = 'Rahim'
age1 = 30
age2 = 40
age3 = 35
print(f"{name1} is {age1} years old, {name2}'s age is {age2} years and {name3} is {age3} years old already.")

# Lists
my_list_ints = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_mix = ['str', 100, 23.2, False]
my_list_str = ['86c7863e-ea77-462f-8af1-b9781d53bd8b', '9e982f49-6a39-48c1-9105-7592ff6e0f2e',
               '4f74fac6-c233-48ba-be8b-fe325cff0dcc', '03a50ecf-ce4f-4dcc-af7a-d53041f5ffa9',
               '3fc4b1b2-ddaf-496d-a98a-4fd84d93de7a']
new_line_list_str = ', \n'.join(my_list_str)
print('new line str list: ', new_line_list_str)
print('-------------------------')
print(type(new_line_list_str))
print('-------------------------')
print('first element in the str list: ', my_list_str[0])
print('old int list: ', my_list_ints)
my_list_ints[0] = 'ONE'
my_list_ints[1] = 'TWO'
print('new int list: ', my_list_ints)  # as we can see here list is mutated
my_list_ints.append(9)
my_list_ints.append(10)  # adds something to the ned of the list
print('result of int list: ', my_list_ints)
poppedValue = my_list_ints.pop()  # pop() is used to pop off an element from the end of a list
print('left over int list: ', my_list_ints)
print('popped item: ', poppedValue)
newPoppedValue = my_list_ints.pop(0)
print('new popped value: ', newPoppedValue)
print(my_list_ints)

two_dim_list = [3, 5, 7, [9, 11, 13]]
print(two_dim_list[3][1])  # to get the value of 11

# Dictionaries (storing operations using key-value pairs)
# Note: In dictionaries objects are retrieved by key name whereas in lists objects are retrieved by location.
my_dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(my_dictionary['key2'])  # value2
price_lookup = {'apple': 2.99, 'oranges': 1.99, 'grapes': 2.49, 'mangoes': 3.49, 'milk': 4.99}
print(price_lookup['grapes'])
new_dict = {'k1': 100, 'k2': 200}
new_dict['k3'] = 300
new_dict['k4'] = 400
print('actual newDict: ', new_dict)
new_dict['k1'] = 99
new_dict['k2'] = 222
print('updated newDict: ', new_dict)
print(new_dict.keys())  # to get all the keys within a dictionary
print(new_dict.values())  # to get all the values within a dictionary
print(new_dict.items())  # to get all the pairs within a dictionary

# Tuples
# Note: Tuples are very similar to lists but the only difference is they're immutable.
# Note: Once an element is added to a tuple, it cannot be re-assigned and tuples use parenthesis ex: (1, 2, 3)
my_tuple = (1, 2, 3, 3, 3)
print(type(my_tuple))
my_list = [1, 2, 3, 3, 3]
print(type(my_list))
print('num of times 3 appears in the tuple: ', my_tuple.count(3))
print('index of first 3 in the tuple: ', my_tuple.index(3))
print('index of first 1 in the tuple: ', my_tuple.index(1))

my_list[0] = 'ONE'
print(my_list)
# my_tuple[0] = 'ONEE' # tuple doesn't support item assignment
# Note: In situations where we don't have to get into any re-assignments, tuple would be the choice


# Sets
my_set = {1, 2, 2}
print(my_set)
duplicate_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]
print(duplicate_list)
print(set(duplicate_list))
# Note: here set() would help in removing the duplicates but its good to keep in mind that set won't have ordering.


# boolean
print(1 > 2)
print(3 == 3)
# Note: 'None' is used as a placeholder, we also use this for in-place result assignments


# I/O with basic files in python
my_file1 = open('myfile.txt', 'w')
add_str = "This is Philadelphia \n"
add_list = ["This is Seattle \n", "This is Chicago \n", "This is SaintLouis \n", "This is NewYork \n",
            "This is California \n", "This is Austin \n"]
my_file1.write(add_str)
my_file1.writelines(add_list)
my_file1.close()

my_file1 = open('myfile.txt', 'r')
print(my_file1.read())
my_file1.close()

# python statements
# if, elif and else
is_dog_hungry = False
is_dog_little_hungry = True
is_dog_full = False
if is_dog_hungry:
    print("I'll feed the dog and make sure its full.@!")
elif is_dog_little_hungry:
    print("I'll leave it to the dog to decide whether it wants to eat or not.")
else:
    print("I'll let the dog do some activity or take some rest to digest the food it ate.")

location = 'Bank'
if location == 'Auto Shop':
    print("Cars are pretty cool.!")
elif location == 'Restaurant':
    print("Food is awesome as we can try and enjoy different cuisines.!")
elif location == 'Bank':
    print("Having money is cool.!")
elif location == 'Store':
    print("Welcome to the store")
else:
    print("I don't know much.!")
# for loops (we can use for loops to execute a block of code for every iteration)
my_for_iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for element in my_for_iterable:
    # using string formatting (f-strings)
    if element % 2 == 0:
        print(f"Even Number: {element}")
    else:
        print(f"Odd Number: {element}")

iterable_list_sum = 0
for number in my_for_iterable:
    iterable_list_sum += number
print(f"Sum of first {len(my_for_iterable)} numbers is: {iterable_list_sum}")

for _ in 'Hello Python':
    print('Cool.!')

my_new_tuple = (1, 2, 3)
for item in my_new_tuple:
    print(item)
my_tuples_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
print(f"Length of tuple: {len(my_tuples_list)}")
for item in my_tuples_list:
    print(item)
# can also call the below line like this: for a, b in my_tuples_list:
for (a, b) in my_tuples_list:  # this is called tuple unpackaging, which helps in getting access to the individual items
    print('first: ', a)
    print('second: ', b)
three_param_tuple_list = [(1, 2, 3), (4, 6, 6), (7, 8, 9), (10, 11, 12)]
for (a, b, c) in three_param_tuple_list:
    print(b)
dict_new = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5}
for item in dict_new:
    print(item)  # by default, when we iterate through a dict, we only iterate through the keys
# but if we want to have the values then we should iterate through the dict_new.values() i.e,
for item in dict_new.items():
    print(item)  # this gives both key and value as a tuple i.e, tuple unpacking
for (key, value) in dict_new.items():
    print('key: ', key)
    print('value: ', value)

# while loop
x = 0
while x < 5:
    print(f"The current value of x: {x}")
    x += 1
else:
    print(f"{x} IS NOT LESS THAN 5")

# Note: We can use break, continue, and pass statements in our loops to add additional functionality
# for various cases. The three statements are defined by:-
# break: Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the closest enclosing loop.
# pass: Does nothing at all.
x = [1, 2, 3]
for item in x:
    pass  # will get back later (here pass is helping to not get any syntax error)
print('end of the script.')

my_str = "Manikanta"
for c in my_str:
    if c == 'k':
        break
    print(c)
for char in my_str:
    if char == 'a':
        continue
    print(char)

# Useful Operators (range, enumerate, )
my_list_new = [1, 2, 3, 4, 5]
for num in range(6):
    print(num)

for num in range(0, 11, 2):
    print(num)

print(list(range(0, 11, 2)))
# Note: A generator is a special type of function that would generate information instead of saving it all to memory.

index_count = 0
for letter in 'abcde':
    # print('At index {} the letter is {}'.format(index_count, letter)) # this does the same thing as the below line with f-strings
    print(f"At index {index_count} the letter is {letter}")
    index_count += 1

first_five_alphabets = 'abcde'
for item in enumerate(first_five_alphabets):
    print(item)  # here its doing index count automatically using tuples
# Note: enumerate() can take in any iterable object, it returns the index count and the object or element itself too
for (index, letter) in enumerate(first_five_alphabets):
    print(index)
    print(letter + '\n')

# zip
list_one = [1, 2,
            3]  # [1, 2, 3, 4, 5, 6] => even in this case the output would be the same because the smallest length is still 3.
list_two = ['a', 'b', 'c']
list_three = ['Mani', 'Raj', 'Aryan']
print(zip(list_one, list_two, list_three))  # <zip object at 0x1167b7f80>
for item in zip(list_one, list_two, list_three):
    print(item)  # this gives the list of tuples
# Note: lot of python built in functions return list of tuples
# Note: zip would only zip upto the shortest of the length of the all things we are trying to zip

print(list(zip(list_one, list_two, list_three)))

# 'in' operator (to check if something is in the list or not and returns boolean)
numbers_four = [1, 2, 3, 4]
print('X' in numbers_four)
print('X' in ['X', 'Y', 'Z', 'A'])
# this also works with dictionaries (both with keys and values)
dict_test = {'k1': 1, 'k2': 2, 'k3': 3}
print('k1' in dict_test)
print(3 in dict_test.values())

# 'min' and 'max' mathematical operators
print(min(numbers_four))
print(max(numbers_four))

# random library, shuffle and randint (random integer)
from random import shuffle

shuffle(numbers_four)  # this is an in-place operation i.e, if we try to print this it gives 'None' as its of NoneType
print(numbers_four)

from random import randint

print(randint(0, 1000))  # this keeps on giving a random number, everytime we run this

# accepting user input by using input()
# result = input('What is your name? ')
# print(result)

# List Comprehensions (Practice this more)
my_string_one = 'hello'
my_list_new = []
for char in my_string_one:
    my_list_new.append(char)
print(my_list_new)

my_list_new_two = [letter for letter in my_string_one]  # this is list comprehension
print(my_list_new_two)

list_of_first_ten_nos = [num for num in range(0, 11)]
print(list_of_first_ten_nos)
# if i want to get square of nums then:
list_of_squares_first_ten_nos = [num ** 2 for num in range(0, 11)]
print(list_of_squares_first_ten_nos)

# If I only want even nos
list_even_nos = [num for num in range(0, 11) if num % 2 == 0]
print(list_even_nos)
# Note: if we want to do if and else together and also can do nested loops in list comprehension then the order changes and looks more complex

list_nos_div_three = [num for num in range(1, 51) if num % 3 == 0]
print(f'numbers div by 3 between 1 to 50: {list_nos_div_three}')

str_test = 'Create a list of the first letters of every word in this string'
# expected out = ['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']
[word for word in str_test.split(' ')] # ['Create', 'a', 'list', 'of', 'the', 'first', 'letters', 'of', 'every', 'word', 'in', 'this', 'string']
list_for_test = [word[0] for word in str_test.split(' ')]
print(list_for_test)









