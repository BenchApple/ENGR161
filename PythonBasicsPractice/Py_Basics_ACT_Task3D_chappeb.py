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
    minuePosition = input("Is the minute hand at the top of the clock? (y/n) ")

    # Store where the minute hand is for later use.
    minuteAtTop = False
    if minuePosition == 'y':
        minuteAtTop = True

    if (abs(xCoord) not in validInputs) or (abs(yCoord) not in validInputs) or (xCoord ** 2 + yCoord ** 2) != 1.0:
        print ("ERROR: Invalid input.")
        return

    # Check the inputted coords against the possible hand values.
    if xCoord == 0:
        if yCoord == 1:
            print("It is twelve " + ("o'clock" if minuteAtTop else "thirty" ) + "  and the gong sounds " + ("12" if minuteAtTop else "1")  + "times.")
            return
        print ("It is six " + ("o'clock" if minuteAtTop else "thirty" ) + "  and the gong sounds " + ("6" if minuteAtTop else "1")  + " times.")
    elif yCoord == 0:
        if xCoord == 1:
            print("It is three " + ("o'clock" if minuteAtTop else "thirty" ) + "  and the gong sounds " + ("3" if minuteAtTop else "1")  + " times.")
            return
        print("It is nine " + ("o'clock" if minuteAtTop else "thirty" ) + "  and the gong sounds " + ("9" if minuteAtTop else "1")  + " times.")
    elif xCoord == .866:
        if yCoord == .5:
            print("It is two " + ("o'clock" if minuteAtTop else "thirty" ) + "  and the gong sounds " + ("2" if minuteAtTop else "1")  + " times.")
            return
        print ("It is four " + ("o'clock" if minuteAtTop else "thirty" ) + "  and the gong sounds " + ("4" if minuteAtTop else "1")  + " times.")
    elif xCoord == -.866:
        if yCoord == .5:
            print("It is ten " + ("o'clock" if minuteAtTop else "thirty" ) + "  and the gong sounds " + ("10" if minuteAtTop else "1")  + " times.")
            return
        print ("It is eight " + ("o'clock" if minuteAtTop else "thirty" ) + "  and the gong sounds  " + ("8" if minuteAtTop else "1")  + " times.")
    elif xCoord == .5:
        if yCoord == .866:
            print("It is one " + ("o'clock" if minuteAtTop else "thirty" ) + "  and the gong sounds " + ("1" if minuteAtTop else "1")  + "  times.")
            return
        print ("It is five " + ("o'clock" if minuteAtTop else "thirty" ) + "  and the gong sounds " + ("5" if minuteAtTop else "1")  + "  times.")
    elif xCoord == -.5:
        if yCoord == .866:
            print("It is eleven " + ("o'clock" if minuteAtTop else "thirty" ) + "  and the gong sounds " + ("11" if minuteAtTop else "1")  + "  times.")
            return
        print ("It is seven " + ("o'clock" if minuteAtTop else "thirty" ) + "  and the gong sounds " + ("7" if minuteAtTop else "1")  + "  times.")
    else:
        print("The coordinates you provided were invalid in some way. This is likely due to them not being the coordinates for a unit vector.")



# Cautionary if statement.
if __name__ == "__main__":
    main()