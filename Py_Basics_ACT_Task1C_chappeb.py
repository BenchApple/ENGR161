# Activity Python Basics Practice
# File: Py_Basics_ACT_Task1C_chappeb.py
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
# Accepts an integer n, then computes the fibonnaci sequence up to and including that value. Outputs this sequence.

def main():
    # Stores the amount of fibbonaci numbers we need to generate to find the one the use requests.
    n = int(input("What is your maximum value? "))


    fibbonaci = [0, 1]

    if n == 0:
        print(fibbonaci[0])
    else:
        tracker = 2
        while fibbonaci[tracker - 1] <= n:
            fibbonaci.append(fibbonaci[tracker - 1] + fibbonaci[tracker - 2]) 
            tracker += 1

        s = ""
        for i in fibbonaci:
            s = s + str(i) + " "

        print (s)    


if __name__ == "__main__":
    main()