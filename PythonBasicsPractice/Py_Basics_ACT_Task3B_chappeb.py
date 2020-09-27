# Ben Chappell


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
            print("It is twelve o'clock and the gong sounds 12 times.")
            return
        print ("It is six o'clock and the gong sounds 6 times.")
    elif yCoord == 0:
        if xCoord == 1:
            print("It is three o'clock and the gong sounds 3 times.")
            return
        print("It is nine o'clock and the gong sounds 9 times.")
    elif xCoord == .866:
        if yCoord == .5:
            print("It is two o'clock and the gong sounds 2 times.")
            return
        print ("It is four o'clock and the gong sounds 4 times.")
    elif xCoord == -.866:
        if yCoord == .5:
            print("It is ten o'clock and the gong sounds 10 times.")
            return
        print ("It is eight o'clock and the gong sounds 8 times.")
    elif xCoord == .5:
        if yCoord == .866:
            print("It is one o'clock and the gong sounds 1 times.")
            return
        print ("It is five o'clock and the gong sounds 5 times.")
    elif xCoord == -.5:
        if yCoord == .866:
            print("It is eleven o'clock and the gong sounds 11 times.")
            return
        print ("It is seven o'clock and the gong sounds 7 times.")
    else:
        print("The coordinates you provided were invalid in some way. This is likely due to them not being the coordinates for a unit vector.")



# Cautionary if statement.
if __name__ == "__main__":
    main()