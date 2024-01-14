print()

"""
* Recursion is a programming concept where a function calls
* itself in its own definition. In Python,recursion is used 
* to solve problems that can be broken down into smaller,
* simpler instances of the same problem.

* Recursion is a powerful tool for solving problems.
"""


#! Calculating Factorial using recursion
def factorial(num):
    if num <= 1:
        return 1

    return num * factorial(num - 1)


ans = factorial(5)
print(ans)
