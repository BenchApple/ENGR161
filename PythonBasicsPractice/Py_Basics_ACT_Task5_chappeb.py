# Ben Chappell

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