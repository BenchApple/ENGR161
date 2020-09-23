# Activity Python Basics Practice
# File: Py_Basics_ACT_Task5_chappeb.py
# Date: 9/22/20
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
# Accepts a sequence of positive integers, then computes the factorials of each of those values.


from Factorial import MyFactorial

def main():
    # Take the set of numbers the user inputs.
    userInput = input("Please enter numbers whose factorials should be evaluated:\n")

    # turn the inputs into a lits of inputs using the split function to use the fact that the inputs will be space delimited.
    inputs = userInput.split(" ")

    for i in inputs:
        f = MyFactorial(float(i))
        
        # Do the appropriate action is the input was improper.
        if f < 0:
            print ("Error: Invalid Input.")
            continue
        print("The factorial of " + str(int(i)) + " is " + str(f) + ".")

# Cautionary If statement.
if __name__ == "__main__":
    main()