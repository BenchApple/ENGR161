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
    columnHeaders = inputLines.pop(0)

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

    # TODO Create some method to sort by a specific parameter. Custom comparison method most likely.

    quicksort(dataset, sortPara, sortDir)
    print(dataset)


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
    if not dir:
        pivot = n[hi]
        i = lo
    else:
        pivot = n[lo]
        i = hi

    # Iterate through all members of the current partition
    for j in range(lo, hi):
        # Swap the pivot with the current item if the pivot is greater than the current item.
        if comparePlants(para, dir, n[j], pivot):
            # Swap n[i] with n[j]
            temp = n[i]
            n[i] = n[j]
            n[j] = temp
        
            # Iterate i
            i += 1

    # Swap n[i] and n[hi]
    if not dir:
        temp = n[i]
        n[i] = n[hi]
        n[hi] = temp
    # swap n[i] and n[lo] if sorting descending
    else:
        temp = n[i]
        n[i] = n[lo]
        n[lo] = temp

    # Return the value of i as the partition.
    return i
    
if __name__ == "__main__":
    main()