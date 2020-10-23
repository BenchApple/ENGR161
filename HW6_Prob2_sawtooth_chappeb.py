# Activity HW6 Part A
# File: HW6_Prob2_sawtooth_chappeb.py
# Date: 19 October 2020
# By: Ben Chappell
# chappeb
# Section: 4
# Team: 54
#
# ELECTRONIC SIGNATURE
# Benjamin Chappell
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
# Given the input arguments for the amplitude, period, maximum time, and time step, creates a list 
# of the values of the sawtooth function according to the specifications found within the problem prompt.

from math import floor

def HW6_Prob2_sawtooth_chappeb(ampl, period, tMax, tStep):
    # The list where we put each value from the function, will be returned.
    output = []

    # Iterate through the given values
    i = 0
    while i < tMax:
        # Extend the function to evaluate outside of it's given period.
        t = i - (floor(i / period) * period)

        # Append the result of the function at the given time according to the 
        output.append(sawtooth(ampl, period, t))

        # iterate the values that we need to iterate.
        i += tStep
    
    # Return the resultant.
    return output

# Returns the result of the sawtooth function according to the time, amplitude, and period
def sawtooth(A, T, t):
    return ((2 * A * t) / T) if (0 <= t and t < (T / 2)) else (((2 * A * t) / T) - (2 * A))
