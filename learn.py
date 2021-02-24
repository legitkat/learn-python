## test file
'''
    this is also a comment
'''
# for i in range(1, 11, 2):
#     print(i)

# name = "myname"

# for row in range(5):  
#     for column in range(5):
#         print(column, end = '')
#     print()

# for i in range(1, 11):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

# for i in range(1, 13):
#     for j in range(1, i+1):
#         print('{:3}'.format(j), end='')
#     print()

# name = "your_name"

# def greet():
#     print("Hello {} nice to meet you".format(name))

# greet()

# import random

# numbers = [4, 5, 2, 6, 1, 7, 8, 3]

# list_numbers = [[], [], [], []]

# for i in range(2):
#     for j in range(4):
#        list_numbers[j].append(numbers.pop())

# print()
# for list_number in list_numbers:
#     print(list_number)

# numbers = [2, -1, 4, -3, 5, 3, -5]

# positive_int = [number for number in numbers if number > 0]
# negative_int = [number for number in numbers if number < 0]

# print("The postive number list is", positive_int , "and the negative number list is", negative_int)

# import random

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# shuffled_numbers = numbers

# random.shuffle(shuffled_numbers)

# print(shuffled_numbers)

numbers = [[3, 6], [8, 2], [7, 5], [1, 4]]

def my_key(x):
    return x[-1]

numbers = sorted(numbers, key=my_key)
# numbers.sort(key=my_key)

print(numbers)
