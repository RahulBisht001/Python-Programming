print()

#! Lesson 5 : Python List
print("Lesson 5 : Python List")


"""
* In Python, a list is a versatile and mutable data type that allows 
* you to store and manipulate a collection of items. 

* Lists are defined by enclosing elements within square 
* brackets ([]) and separating them with commas. 

"""

users = ["admin", "Rahul", "user2", "user3"]

data = ["Rahul", "Nikku", 69, 3 + 4j, True, "God"]

emptyList = []

# * The keyword `in` is used as a membership test operator.

# print("Rahul" in data)
# print("rahul" in data)

# print("Rahul" in data and "Rahul" in users)

# print(data[0])
# print(data[3])
# print(data[-3])
# print(data[-5])


# print(data.index("Rahul"))
# print(data.index(69))


# data = ["Rahul", "Rahul", 69, 3 + 4j]

# print(data[0:4])
# print(data[0:-1])

# * Here the last value is showing the step size
# * Something like take this num and leave step size
# * it's kind of gap between two alternate values.

# print(data[-6:-1:3])
# print(data[-1:-3])

# data.append("Elisha")
# print(data)

# data += ["Lord Krishna"]
# print(data)

# data.extend("Mahadev")

# * The extend method takes a list as an argument and appends
# * the Append method takes a single value as an argument an

# * See the Output of the below code. you will see the difference between
# * Extend and Append method.

# * Extend treat the list as collection and all values separately while
# * Append take the list as single element and append it.

# data.extend(["Mahadev"])
# data.append(["Jimmy", "Lora"])
# print(data)

# data.insert(3, "Elisha")
# print(data)

# data.remove("Rahul")
# print(data)

# print(data.pop())

# * `del` Keyword for deleting a Specific item

del data[0]
# print(data)

# del data
# print(data)

# data.clear()
# print(data)

# users.sort()
# print(users)


nums = [2, 34, 67, 2325, 12]

# nums.reverse()
# print(nums)

# nums.sort()
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# print(nums)
# print(sorted(nums, reverse=True))
# print(nums)

#! Copy the List
# * 3 Ways of Copying the List

numsCopy = nums.copy()
myNums = list(nums)
myCopy = nums[:]

# print(numsCopy)
# print(myNums)
# print(myCopy)

print(type(myCopy))

print()
