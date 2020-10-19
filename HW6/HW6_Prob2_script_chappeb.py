# Activity HW6 Part B
# File: HW6_Prob2_script_chappeb.py
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
# Given the user inputs for the amplitude, period, and upper time limit for the sawtooth function,
# as well as the number of terms in the fourier series one will use to approximate the sawtooth 
# function, creates a single figure with two plots in the same graph. One of these plots is the
# actual sawtooth function plotted from time 0 to the inputted maximum. The other plot will be 
# the approximation summing the first K terms in the given Fourier series plotted over the same time period.

# Imports
from HW6_Prob2_sawtooth_chappeb import HW6_Prob2_sawtooth_chappeb as st
from matplotlib import pyplot as plt
from math import sin, pi

def main():
    # User inputs
    ampl = float(input("Enter amplitude -> "))
    period = float(input("Enter period -> "))
    tMax = float(input("Enter maximum time -> "))
    capK = int(input("Enter maximum terms for the Fourier Series -> "))

    # Calculate the tStep according to it equalling period / 50
    tStep = period / 50

    # Get the sawtooth function from our sawtooth script. Set tStep using the maximum T divided by 50.
    sawtooth = st(ampl, period, tMax, tStep)

    # Fourier stores the fourier values, tVals stores the values of t we are evaluating.
    fourier = []
    tVals = []

    # Set the starting values for our tracker variables.
    t = 0

    # Generate the fourier series list.
    while t < tMax:
        # Stores the result of the summation.
        s = 0

        # Iterate through the k values to complete the summation in the fourier series.
        for k in range(1, int(capK)):
            s += b_k(ampl, k) * sin((2 * k * pi * t) / period)

        # add the value of summation to the fourier series list.
        fourier.append(s)
        tVals.append(t)

        # Iterate the iteratable values.
        t += tStep

    # Begin the plotting mechanism.
    # We will use both sawtooth and fourier as y values, and use tVals as our independent variable.
    plt.figure(num=1, figsize=(13,8), dpi=80)
    plt.title("Sawtooth Function: Actual vs Approximate", fontsize=15)
    plt.xlabel("Time t (seconds)", fontsize=13)
    plt.ylabel("S(t)", fontsize=13)
    # plt.axis(xlim=(0, tMax), option=True)
    plt.plot(tVals, sawtooth, label = 'Sawtooth', linewidth="1")
    plt.plot(tVals, fourier, label = 'Approximate', linestyle="--")
    plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0)
    plt.show()

# Finds the value of b sub k in the summation for the fourier series.
def b_k(A, k):
    return -((2 * A) / (pi * k)) * pow(-1, k)

# Cautionary if statement.
if __name__ == "__main__":
    main()