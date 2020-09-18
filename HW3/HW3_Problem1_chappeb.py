# Ben Chappell

import math

def main():
    # List to store all of the variables
    #               0       1           2       3           4       5           6       7           8       9           10
    # Looks like [height, anchorAX, anchorAY, anchorBX, anchorBY, anchorCX, anchorCY, tensileA, tensileB, tensileC, maxOverturnMoment]
    parameters = []

    # While this is the correct solution according to the parameters, I find this to be an incredibly messy way of handling data.
    parameters.append(float(input("Enter the height (in meters): "))) # Stores the height of the tower.    
    parameters.append(float(input("Enter the X coordinates of anchor point A (in meters): "))) # Stores the coordinates of anchor A.
    parameters.append(float(input("Enter the Y coordinates of anchor point A (in meters): "))) # Stores the coordinates of anchor A.
    parameters.append(float(input("Enter the X coordinates of anchor point B (in meters): "))) # Stores the coordinates of anchor B.
    parameters.append(float(input("Enter the Y coordinates of anchor point B (in meters): "))) # Stores the coordinates of anchor B.
    parameters.append(float(input("Enter the X coordinates of anchor point C (in meters): "))) # Stores the coordinates of anchor C.
    parameters.append(float(input("Enter the Y coordinates of anchor point C (in meters): "))) # Stores the coordinates of anchor C.
    parameters.append(float(input("Enter the tensile force in cable DA (in newtons): "))) # Stores the value of the tensile force in cable DA in newtons.
    parameters.append(float(input("Enter the tensile force in cable DB (in newtons): "))) # Stores the value of the tensile force in cable DB in newtons.
    parameters.append(float(input("Enter the tensile force in cable DC (in newtons): "))) # Stores the value of the tensile force in cable DC in newtons.
    parameters.append(float(input("Enter the maximum value for the overturning moment (in N-m): "))) # Stores the value of the maximum overturning moment of the tower.

    # Get the perpendicular force components for each of the anchors.
    perpendicularForceA = getPerpendicularForceComponents(parameters[1], parameters[2], parameters[7], parameters[0]) # For each of these we are inputting (anchorX, anchorY, tensileForce, height)
    perpendicularForceB = getPerpendicularForceComponents(parameters[3], parameters[4], parameters[8], parameters[0])
    perpendicularForceC = getPerpendicularForceComponents(parameters[5], parameters[6], parameters[9], parameters[0])

    # Will store the components of the perpendicular force.
    perpendicularForce = [0, 0]
    perpendicularForce[0] = perpendicularForceA[0] + perpendicularForceB[0] + perpendicularForceC[0]
    perpendicularForce[1] = perpendicularForceA[1] + perpendicularForceB[1] + perpendicularForceC[1]

    # Stores the magnitude of the perpendicular force.
    perpendicularForceMagn = math.sqrt((perpendicularForce[0] ** 2) + (perpendicularForce[1] ** 2))

    # Stores the Overturn Moment that results from the inputted values.
    resultantOverturnMoment = perpendicularForceMagn * parameters[0]

    print ("")
    print ("The overturning moment magnitude is {:.4f} N-m.".format(resultantOverturnMoment))

    # Check if the overturn moment is low enough.
    if resultantOverturnMoment < parameters[10]:
        print ("This retraining system is safe.")
        return
    print ("This restraining system is not safe.")
    return


# Returns the x and y values of the forces perpendicular to the tower from the tensile force of the given anchor in list format [x,y].
def getPerpendicularForceComponents(anchorX, anchorY, tensileForce, height):
    # List three units long that holds the x, y, and z direction of the given force. Initialized to the zero vector
    forceUnitDirection = [0, 0, 0] 

    # Stores the value of the magnitude found from the coordinates of the given anchor. Found by taking the x and y coordinates of the anchor, and using them
    # in conjunction with the height to find the magnitude of their direction. Then is used to calculate the unit vector in the direction of the tensile force.
    directionMagnitude = 0 # Initialized to zero for readability.

    # Stores the value of the perpendicular force. Equivalent to [tensileForce * forceUnitDirection[0], tensileForce * forceUnitDirection[1]]
    perpendicularForceComponents = [0, 0]

    # Calculate the direction magnitude.
    directionMagnitude = math.sqrt((anchorX ** 2) + (anchorY ** 2) + height ** 2)

    # Calculate the components of the tensile force's unit vector.
    forceUnitDirection[0] = anchorX / directionMagnitude
    forceUnitDirection[1] = anchorY / directionMagnitude
    forceUnitDirection[2] = height / directionMagnitude

    # Calculate the component forces perpendicular to the tower using their unit directions and the given tensile force.
    perpendicularForceComponents[0] = forceUnitDirection[0] * tensileForce
    perpendicularForceComponents[1] = forceUnitDirection[1] * tensileForce

    return perpendicularForceComponents


# Cautionary execution to prevent execution of main if this file is being accessed from another file.
if __name__ == "__main__":
    main()