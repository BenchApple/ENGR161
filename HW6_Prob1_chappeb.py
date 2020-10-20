# Activity HW6 Prob 1
# File: HW6_Prob1_chappeb.py
# Date: 19 October 2020
# By: Ben Chappell
# chappeb
# Section: 4
# Team: 54
#
# ELECTRONIC SIGNATURE
# Benjamin Chappell
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
# Accepts from the user a data file containing the experiment data and a two character code. 
# According to the code, sorts with respect to a specific data point, and in ascending or descending
# order. Then outputs the resultant data to a new text file.

def main():
    # Accept input from the user.
    outputID = input("Enter a file name for the reorganized data: ")
    reoorgCode = input("Enter a code for the reorganization: ")

    # Open the input and output files. 
    inputFile = open("plant_treatment_data.txt", "r")
    outputFile = open(outputID, 'w')

    # Read in the data from the input file, line by line.
    inputLines = inputFile.readlines()
    # Remove the first line, since it only has trash identifiers.
    inputLines.pop(0)

    # Iterate through the lines, cleaning the data into actual integers and floats.
    dataset = []
    for line in inputLines:
        line = line.strip("\n")
        separatedLine = line.split()
        
        # Turn the data into ints or floats, depending on what's appropriate.
        for s in range(0, len(separatedLine)):
            try:
                separatedLine[s] = int(separatedLine[s])
            except:
                separatedLine[s] = float(separatedLine[s])

        dataset.append(separatedLine)

    # Replace starting and ending height with the amount of growth.
    for plant in dataset:
        plant[2] = round(plant.pop(3) - plant[2], 2)

    # Determine which method to sort by. An input P means Plant ID, S - Status
    # G - growth data, C - Concentration data.
    # Personal code will be 0 - Plant ID, 1 - Status, 2 - Growth Data, 3 - Concentration. 
    # This way it corresponds directly with the indices where those values should be stored in the dataset.
    sortPara = sortingChoice(reoorgCode[0])

    # Determine which direction to sort in. 0 means increasing, 1 means decreasing on my end. 
    # From the user, A means increasing, D means decreasing.
    sortDir = sortingDirection(reoorgCode[1])

    # Sort dataset according to the parameters we just defined.
    quicksort(dataset, sortPara, sortDir)

    # Create the Header String - hard coded. Then write it to the file.
    newHeader = "PlantID  Status  Growth  Concentration\n"
    outputFile.write(newHeader)

    # The exact locations where each of the data points should be placed in the formatted string.
    startLocations = [0, 9, 17, 25]
    # Turn each of the database lines into the desired strings to print
    for line in dataset:
        # Create a string the same length as the new header, then populate it with spaces and add a newline.
        formatted = [' ' for i in range(0, len(newHeader) - 1)]
        formatted.append('\n')

        # Replace the appropriate spots, character by character, with the characters from the data points
        for i in range(0, len(line)):
            line[i] = str(line[i])

            # Go through character by character
            for j in range(0, len(line[i])):
                formatted[startLocations[i] + j] = line[i][j]
            
        # Finalize the formatted string by joining all elements of the list version of itself.
        formatted = "".join(formatted)
        outputFile.write(formatted)

    # Give the user some sort of closure or something
    print ("")
    print ("File " + outputID + " has been created.")

    # Close our files.
    inputFile.close()
    outputFile.close()
    
# Compares two lists, based on the input parameter and the direction of the sorting.
# Returns true if n2 is greater than n1, false if the inverse when increasing, otherwise the opposite
# p is the sorting parameter, dir is the direction (0 means increasing, 1 means decreasing)
def comparePlants(p, dir, n1, n2):
    if not dir:
        return n1[p] < n2[p]
    return n1[p] > n2[p]

# Returns the personal sorting code depending on what the first letter of the code is.
def sortingChoice(s):
    c = -1

    if s == 'P':
        c = 0
    elif s == 'S':
        c = 1
    elif s == 'G':
        c = 2
    elif s == 'C':
        c = 3

    return c

# Returns the sorting direction given the second letter of the code.
def sortingDirection(s):
    c = -1

    if s == 'A':
        c = 0
    elif s == 'D':
        c = 1

    return c

# Shell method for quicksort. p and dir determine the direction of the sorting.
def quicksort(n, para, dir):
    qsort(n, 0, len(n) - 1, para, dir)
    

# Quicksorts n from lo to hi. p and dir determine the parameter and direction of the sorting
def qsort(n, lo, hi, para, dir):
    if lo < hi:
        p = partition(n, lo, hi, para, dir)
        qsort(n, lo, p - 1, para, dir)
        qsort(n, p + 1, hi, para, dir)

# Finds the partition for the quicksort. The partition is the method by which we effectively sort
# The current section. It is found as the number of items in the list that are less than the 
# value at n[hi]. By finding this value and swapping strategically with n[i] while iterating
# through list n, we can sort the list recursively.
def partition(n, lo, hi, para, dir):
    # If sorting in increasing order, set pivot to n[hi] and i to lo, otherwise the inverse.
    pivot = n[int((hi + lo) / 2)]
    i = lo
    j = hi

    # Infinite loop until we return something. 
    # Finding a place for the pivot where it is exactly in the middle of the two sides.
    # When ascending, want the right side to be wholly less than, and the left side to be wholly greater than the pivot
    # Opposite when descending.
    while True:
        while comparePlants(para, dir, n[i], pivot):
            i += 1

        while comparePlants(para, int(not dir), n[j], pivot):
            j -= 1

        # If the desired status is met, return the location of the pivot
        if i >= j:
            return j

        # Swap the locations of i and j
        temp = n[i]
        n[i] = n[j]
        n[j] = temp
        i += 1
    
# Cautionary if statement
if __name__ == "__main__":
    main()