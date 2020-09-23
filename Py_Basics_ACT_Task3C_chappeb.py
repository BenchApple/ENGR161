# Activity Python Basics Practice
# File: Py_Basics_ACT_Task3C_chappeb.py
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
# Accepts the components of a unit vector pointing in the direction of the hour hand of a clock assuming
# that the minute hand is in the bottom position, and calculates the time and the number of times the gong will ring.


def main():
    # Variable Declaration
    rootThreeOverTwo = .866 # Stores the value of root three over two for later checking
    oneHalf = .5 # Stores the value of one half for later checking.

    # Stores the group of valid inputs.
    validInputs = (rootThreeOverTwo, oneHalf, 1, 0)
    
    # User inputs. For each, will only accept the values of +-.866, +-.5, +-1, or 0
    xCoord = float(input("Input the x unit direction. Must have the absolute value of .866, .5, 1, or 0 -> "))
    yCoord = float(input("Input the y unit direction. Must have the absolute value of .866, .5, 1, or 0 -> "))

    if (abs(xCoord) not in validInputs) or (abs(yCoord) not in validInputs):
        print ("ERROR: Invalid input.")
        return

    # Check the inputted coords against the possible hand values.
    if xCoord == 0:
        if yCoord == 1:
            print("It is twelve thirty and the gong sounds 1 time.")
            return
        print ("It is six thirty and the gong sounds 1 time.")
    elif yCoord == 0:
        if xCoord == 1:
            print("It is three thirty and the gong sounds 1 time.")
            return
        print("It is nine thirty and the gong sounds 1 time.")
    elif xCoord == .866:
        if yCoord == .5:
            print("It is two thirty and the gong sounds 1 time.")
            return
        print ("It is four thirty and the gong sounds 1 time.")
    elif xCoord == -.866:
        if yCoord == .5:
            print("It is ten thirty and the gong sounds 1 time.")
            return
        print ("It is eight thirty and the gong sounds 1 time.")
    elif xCoord == .5:
        if yCoord == .866:
            print("It is one thirty and the gong sounds 1 time.")
            return
        print ("It is five thirty and the gong sounds 1 time.")
    elif xCoord == -.5:
        if yCoord == .866:
            print("It is eleven thirty and the gong sounds 1 time.")
            return
        print ("It is seven thirty and the gong sounds 1 time.")
    else:
        print("The coordinates you provided were invalid in some way. This is likely due to them not being the coordinates for a unit vector.")



# Cautionary if statement.
if __name__ == "__main__":
    main()