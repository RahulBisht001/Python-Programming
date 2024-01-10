print()

"""
* a dictionary is a built-in data type that allows you to store 
* a collection of key-value pairs. It is a flexible and powerful 
* container that is often used for representing and manipulating 
* data in various applications. 

* Dictionaries are also known as associative arrays or hash maps in other programming languages.
"""
print("Lesson 6 : Python Dictionaries")

subject = {
    "Maths": 99,
    "Physics": 97,
    "Chemistry": 98,
    "Hindi": 96,
    "English": 95,
}

subject2 = dict(Mathematics=99, Physics=97, Chemistry=98, Hindi=96, English=95)

# print(subject)
# print(subject2)

#! Access items in a dictionary
# print(subject["Maths"])
# print(subject.get("Physics"))

#! List all the keys & values in a dictionary

# print(subject.keys())
# print(subject.values())

# * list of key/value pairs as tuples
# print(subject.items())

# * check the existence of a key in a dictionary
# print("Maths" in subject)


# * update the value of a key in a dictionary
# subject["Maths"] = 100

# print(subject.items())

# subject.update({"Python": 100})
# print(subject.items())

# * remove items from a dictionary
# print(subject)
# print(subject.pop("Hindi"))
# print(subject)

# it will return a tuple of the key and value of the last item in the dictionary
# instead of just value in pop() function
# one more thing to notice here is that it will remove the last item  added in the dictionary
# not the last item that lys in the dictionary

# subject.update({"Python": 100})
# print(subject.popitem())

#! del and clear

# del subject["Maths"]
# print(subject)

# subject.clear()
# print(subject)


#! Copy Dictionary

# it is not actually creating a copy of the dictionary but creating an instance
# subject3 = subject

# subject3 = subject.copy()

# subject3.update({"Java": 100})

# print(subject3)
# print(subject)

# * or we can use the dict() function to create a copy of the dictionary

# subject4 = dict(subject)
# print(subject)
# print(subject4)


#! Nested Dictionaries

subject5 = {
    "class_12": subject,
    "class_10": {"Sanskrit": 99, "Science": 100, "maths": 99, "Social Science": 96},
}
print(subject5.items())
print(subject5["class_10"]["Science"])

print()
