"""
* A set is an unordered collection of unique elements. 
* It is defined by placing elements inside curly braces {} 
* or by using the set() constructor. Sets are similar 
* to lists or dictionaries, but they do not allow duplicate elements.
"""

# nums = {1, 2, 3, 3 + 6j, "Rahul"}
# print(nums)

# setEx = set((1, 2, "Rahul", 5))
# print(setEx)

# nums2 = {1, 2, 2, 2, 2, 3, 4}
# * One more imp thing is : True is Duplicate of 1 and False is not duplicate of 1
# print(nums2)

# num = {2, 1, True, 3, False, 0}
# num.add("Nikku")
# print(num)

# # * Add elements from another set

# moreNum = {5, 6, 90}
# num.update(moreNum)

# dict = {"Rahul": "XXXXXXXXXXXXXXX"}

# num.update(dict)

# print(num)


#! Merge two sets and create a new set from them
set1 = {23, "Ram", True}
set2 = {False, "Sita", "Ram"}

newSet = set1.union(set2)
print(newSet)


# * keep only the common values from two sets
set1.intersection_update(set2)
print(set1)
