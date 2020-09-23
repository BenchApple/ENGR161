# Ben Chappell.

# Recursive factorial function
# Still technically a looping method, just not traditional.
# Words because short circuit evaluation immediately returns 1 if not n, so only when n = 0
# Then if n is anything other than zero, it evaluates the second half of the or statements, which executes the recursive bloc.
# Returns -1 if the input is invalid.
def MyFactorial(n):
    return int((not n or n * MyFactorial(n-1)) if (n >= 0 and n % 1 == 0) else -1)