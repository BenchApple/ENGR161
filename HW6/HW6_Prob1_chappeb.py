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

    print (dataset)

    # TODO Create some system to determine which parameter to sort by
    # Determine which method to sort by. An input P means Plant ID, S - Status
    # G - growth data

    # TODO Create some method to sort by a specific parameter.




    # Close our files.
    inputFile.close()
    outputFile.close()
    

# Shell method for quicksort
def quicksort(n):
    qsort(n, 0, len(n) - 1)

# Quicksorts n from lo to hi. 
def qsort(n, lo, hi):
    if lo < hi:
        p = partition(n, lo, hi)
        qsort(n, lo, p - 1)
        qsort(n, p + 1, hi)

# Finds the partition for the quicksort. The partition is the method by which we effectively sort
# The current section. It is found as the number of items in the list that are less than the 
# value at n[hi]. By finding this value and swapping strategically with n[i] while iterating
# through list n, we can sort the list recursively.
def partition(n, lo, hi):
    pivot = n[hi]
    i = lo

    # Iterate through all members of the current partition
    for j in range(lo, hi):
        # Swap the pivot with the current item if the pivot is greater than the current item.
        if n[j] < pivot:
            # Swap n[i] with n[j]
            temp = n[i]
            n[i] = n[j]
            n[j] = temp
        
            # Iterate i
            i += 1

    # Swap n[i] and n[hi]
    temp = n[i]
    n[i] = n[hi]
    n[hi] = temp

    # Return the value of i as the partition.
    return i
    
if __name__ == "__main__":
    main()