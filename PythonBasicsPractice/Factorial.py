# Activity Python Basics Practice
# File: Factorial.py
# Date: 9/22/2-
# By: Ben Chappell
# chappeb
# Section: 4
# Team: 54
#
# ELECTRONIC SIGNATURE
# Ben Chappell
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
# Calculates the factorial of any given positive integer.


# Recursive factorial function
# Still technically a looping method, just not traditional.
# Words because short circuit evaluation immediately returns 1 if not n, so only when n = 0
# Then if n is anything other than zero, it evaluates the second half of the or statements, which executes the recursive bloc.
# Returns -1 if the input is invalid.
def MyFactorial(n):
    return int((not n or n * MyFactorial(n-1)) if (n >= 0 and n % 1 == 0) else -1)