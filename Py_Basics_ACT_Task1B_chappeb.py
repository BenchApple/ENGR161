# Activity Python Basics Practice
# File: Py_Basics_ACT_Task1B_chappeb.py
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
# Accepts an integer n, then computes and outputs the fibonnaci sequence up n values.

def main():
    # Stores the amount of fibbonaci numbers we need to generate to find the one the use requests.
    n = int(input("What is your value of n? "))


    fibbonaci = [0, 1]

    if n == 1:
        print(fibbonaci[0])
    elif n == 2: 
        print (str(i) + ", " for i in fibbonaci)
    else:
        tracker = 2
        while tracker < n:
            fibbonaci.append(fibbonaci[tracker - 1] + fibbonaci[tracker - 2]) 
            tracker += 1

        s = ""
        for i in fibbonaci:
            s = s + str(i) + " "

        print (s)    



# Cautionary if.
if __name__ == "__main__":
    main()