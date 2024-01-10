print()

"""
* Python tuples are almost similar to lists. 
* The key difference between the two is that we cannot 
* change the elements of a tuple once it is assigned 
* whereas we can change the elements of a list.

* lists are mutable whereas tuples are immutable
* even we cannot change the order of the elements in a tuple

! In Short, a tuple is an ordered, immutable collection of elements
"""

myTuple = tuple(("1", "2"))
print(myTuple)

anotherTuple = ("1", True, 13, 3 + 5j)
print(anotherTuple)

# myList = list(["1", "2"])
# print(myList)

# * Extended Unpacking in Python is a concept that allows you
# * to unpack elements from an iterable, such as a tuple, into multiple variables.


# * it is similar to object destructuring in javascript

(one, two, *others) = anotherTuple

print(one)
print(two)
print(others)


(one, *two, others) = anotherTuple

print(one)
print(two)
print(others)


print()
