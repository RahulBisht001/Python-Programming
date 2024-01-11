print()


print("Python Loops\n")

# value = 1


# while value < 10:
#     print(value, end=" ")

#     # if value == 5:
#     #     break
#     value += 1
# else:
#     print("\n\nWhile Loop Done Properly, Hence we are able to use `else`")


# -------------------------------------------------

# Hera Pheri 2 Cast

names = ["Raju", "Shyam", "BabuRav", "Tiwari", "Munna", "Kachra Seith", "Nanji Bhai"]

# for name in names:
#     print(name, end="  ")

# print("\n")

# for x in "Hera Pheri 2":
#     print(x)


for name in names:
    for ch in name:
        print(ch, end=" ")

    print("\n")

# for i in range(5):
#     print(i, end=" ")


# for i in range(1, 10):
#     print(i, end=" ")

# print("Table of 9\n")

# version 1 :

# for i in range(1, 11):
#     print("9 X " + str(i) + " = " + str(9 * i))


# version 2 :

# for i in range(1, 11):
#     print(f"9 X {i} = {9 * i}")

"""
* 👆🏻👆🏻 In this version, the f-string allows you to embed expressions 
* inside string literals, making it easier to include variables 
* and expressions directly in the string. It enhances the readability 
* of the code and reduces the need for explicit conversions using str().
"""
# wrong

# for i in range(0, 101, i += 10):
#     print(i, end=" ")


print()
print()
