print()
print()

print("Lesson 4 : Python DataTypes")


#! ___________ String DataType  _________

#! Literal Assignment

first = "Rahul"
last = "B"

"""
* All these statements below are doing the same
* thing. they all are checking for the class of 
* variable.

* isinstance is an inbuilt function in python
* type is also another builtin function in python for type checking

"""
print(type(first))
print(type(first) == str)
print(isinstance(first, str))


#! constructor function

pizza = str("Margarita")


print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))


#! Concatenation

fullName = first + " " + last
print(fullName)

#! Casting a Number to a String

year = 2002
year = str(year)

print(year)
statement = "I was born in Year " + year + " December"
print(statement)
print(type(year))


#! Multiline

multiline = """

-----------------------------------------------
Hi I am Rahul !
I am a Full Stack Developer.

Concreted my Problem Solving Skills with 
DSA in Java on certain platforms like 
leetcode, geeksforgeeks and codechef. 

I have Good CS Fundamental knowledge as well.
-----------------------------------------------

"""
print(multiline)

#! Escaping  Specially Characters

sentence = "I'm back in form! I Know my CLASS\t  "
print(sentence)


#! String Methods
# * Methods are special functions that belong to objects.
# * Methods are called with a period followed by the method name.

print(first)
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("Java", "Ultimate Java"))
print(multiline.upper())
print(multiline.capitalize())

print(len(multiline))
print(len(multiline.strip()))

print(len(multiline.lstrip()))
print(len(multiline.rstrip()))


#! Build a Menu

title = "  menu  ".upper()
print(title.center(20, "="))

print("Coffee ".ljust(20, ".") + "$1".rjust(5, " "))
print("Muffin ".ljust(20, ".") + "$2".rjust(5, " "))
print("Cupcake ".ljust(20, ".") + "$3".rjust(5, " "))
print("Burger ".ljust(20, ".") + "$5".rjust(5, " "))


#! String Index values

# Rahul

print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#! Some Method return Boolean data

print(first.startswith("R"))
print(first.endswith("l"))


# ^ _________ Boolean Data Type __________

value = True
print(value)

value = bool(False)
print(value)
print(type(value))
print(type(value) == bool)


# * ___________ Numeric data type __________

#! Integer
#! float


# ~ ______________ Complex data type _______________
# * it is a kind of Numeric data type but mostly used in electrical
# * engineering. it uses a 'j' notation


complex_data = 3 + 4j

print(complex_data)
print(type(complex_data))

print(complex_data.real)
print(complex_data.imag)


#! Built in Functions for Numbers
gpa = 8.392

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))


#! The 'Math Module'

import math

print(math.pi)
print(math.ceil(gpa))
print(math.floor(gpa))
print(math.sqrt(121))
print(int(math.pow(11, 2)))

#! Casting a String to a Number

zip_code = "248001"
zip_value = int(zip_code)
print(zip_value)
print(type(zip_value))

# * Error
print(int("Rahul"))

print()
