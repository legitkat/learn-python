'''
    notes made properly below
'''
###
#fcc lec 1

'''
    dir(var)
    type(var) 
    help(on diff functions and stuff)
'''

# function

def new_line():
    print()

# .upper() and .format

name = "myname"
print("my name is {}".format(name))
print("my name is {}".format(name.upper()))
new_line()

# range, for loop and f string

for i in range(3):
    print(f"{i}st ")

new_line()

# lists and range (last term doesnt get included in range)

my_list = list(range(1, 6, 2))
for elements in my_list:
    print(elements)

new_line()

# using list like an array (i guess thats what u call it) (last term doesnt get included just like range)

name = "myname"
print(name[0])
print(name[1:4])
print(name[2:])

new_line()

# even further (3rd arguement just like range)

name = "myname"
print(name[::-1])
print(name[::2])

new_line()

# if elif else

name = "myname"

if name == "myname":
    print(f"Welcome {name}")
elif name == "":
    print("Please enter a name")

# escape seq

print("He said,\"Use this to solve ur problem\"")
new_line()

# print with no newline (\n)

my_list = [1, 2, 3, 4, 5]

for elements in my_list:
    print(elements)

new_line()

for elements in my_list:
    print(elements, end='')

new_line()

#