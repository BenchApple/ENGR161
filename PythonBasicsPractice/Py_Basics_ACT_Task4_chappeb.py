# Ben Chappell

def main():
    # Accept the user input.
    n = float(input("What is your desired value of n? "))

    if n % 1 != 0:
        print("Error: Negative input")
        return

    n = int(n)

    output = myFactorial(n)

    print(("The factorial of " + str(n) + " is " + str(output) + ".") if output > 0 else ("Error: Negative input."))
        

# Recursive factorial function
# Still technically a looping method, just not traditional.
# Words because short circuit evaluation immediately returns 1 if not n, so only when n = 0
# Then if n is anything other than zero, it evaluates the second half of the or statements, which executes the recursive bloc.
# Returns -1 if the input is invalid.
def factorialR(n):
    return (not n or n * factorialR(n-1)) if (n >= 0 and n % 1 == 0) else -1

# The actual what I assume is desired method for finding the factorial
# Uses a legitimate loop function we learned in class.
# Returns -1 if the input is invalid.
def myFactorial(n):
    final = 1 # Stores the final value to return of the function.

    # Executes the factorial method via a for loop.
    for i in range(n, 0, -1):
        final *= i

    if n >= 0 and n % 1 == 0:
        return final
    return -1

# Cautionary If statement.
if __name__ == "__main__":
    main()