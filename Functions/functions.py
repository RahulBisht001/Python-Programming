print()
print("Python Functions\n\n")

"""
* functions are reusable pieces of code that perform a specific task. 
* in python we define functions using the def keyword.

"""


def hello_world():
    print("Hello from RahulB!")


# hello_world()
# print("------------")


def get_sum(num1, num2):
    print(num1 + num2)


# get_sum(6, 9)
# print("------------")

# get_sum(3, 1)
# print("------------")

# get_sum(2, 4)
# print("------------")


#! return a value from a function


def total_sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        print("Type mismatch --> Hence early return without summation")
        return

    return num1 + num2


# total = total_sum()
# total = total_sum(2)
# total = total_sum(2, 1)
# total = total_sum(2, "Rahul")

# print(total)
# print(type(total))
# print(type(total_sum))
# print("-----------")


#! Multiple items in a function we don't know how many arguments will be there


def multiple_arguments(*args):
    print("Multiple arguments")
    print(args)
    print(type(args))

    for arg in args:
        for char in arg:
            print(char, end=" ")
        ## print(arg)
        print()


# multiple_arguments("Raju", "BabuRau", "Shyam", "Tiwari", "NanjiBhai")
# multiple_arguments("Raju", "BabuRau", "Shyam", 20, "NanjiBhai")


def multi_named_arguments(**kwargs):
    print("Multiple named arguments")
    print(kwargs)
    print(type(kwargs))
    print()

    for key, value in kwargs.items():
        print(key, " ----> ", value)


multi_named_arguments(name="Rahul", age=20, city="Delhi")

print()
