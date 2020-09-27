# Activity Homework 4
# File: HW4_Prob1_chappeb.py
# Date: 26 September 2020
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
# Utilizes the trapezoid method to calculate the definite integral of exp(cos(x)) given the user
# inputs for the upperbound, lowerbound, and the convergence criterion.

from math import exp, cos

def main():
    #---------------------------------------------------
    #  Inputs
    #---------------------------------------------------
    lowerbound = float(input("Enter the lower bound: "))
    upperbound = float(input("Enter the upper bound: "))
    convCrit = float(input("Enter the convergence criterion value: "))

    #---------------------------------------------------
    #  Computations
    #---------------------------------------------------

    # Check is the lower and upper bound are valid, check if the convergence criterion is greater than 0.
    if lowerbound > upperbound:
        print("Error: upper bound must be greater than lower bound")
        return
    if convCrit <= 0:
        print("Error: convergence criterion must be strictly greater than zero")
        return

    # This value correlates to the amount of trapezoids formed.
    n = 2
    
    # Store the current and previous calculated integrals.
    currCalcedIntegral = 0 # initialized to zero so that something that doesn't enter the while loop computes properly.
    prevCalcedIntegral = -convCrit - 1
    
    # Define f(x) as exp(cos(x)) as a lambda function.
    f = lambda x : exp(cos(x))

    # While loop continually computes the integral using the trapezoid rule until the computed integral
    while abs(currCalcedIntegral - prevCalcedIntegral) >= convCrit:
        deltaX = (upperbound - lowerbound) / n

        # lambda function to be used to determine the value of x_k
        x = lambda k : (lowerbound + (k * deltaX))

        # Move the currently calculated integral to the previously calculated integral.
        prevCalcedIntegral = currCalcedIntegral

        # Calculate the integral using the formula described in the problem prompt.
        currCalcedIntegral = (deltaX / 2) * (f(lowerbound) + (2 * sum(f(x(k)) for k in range(1, n))) + f(upperbound))

        # Iterate n by one.
        n += 1

    #---------------------------------------------------
    #  Outputs
    #---------------------------------------------------
    print("")
    print("The value of the integral is " + str(currCalcedIntegral))


if __name__ == "__main__":
    main()
