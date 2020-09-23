# Activity Python Basics Practice
# File: Py_Basics_ACT_Task2_chappeb.py
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
# Accepts the hard coded tempurature and pressure of a system and outputs the neccesary output: Danger, normal, or warning.

def main():
    temperature = 850 # hard coded value to store the tempurature of the system.
    pressure = 17 # hard coded value to store the pressure of the system.

    if temperature > 1000 or pressure > 20:
        print("System is in Danger!")
    elif temperature > 750 and pressure > 10:
        print("System is normal.")
    else:
        print("System is in warning.")

# Cationary if statement.
if __name__ == "__main__":
    main()
