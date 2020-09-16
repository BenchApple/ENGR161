# Ben Chappell


def main():
    # Stores the inputted fundemental frequency.
    fundementalFreq = int(input("Enter the fundemental frequency for the string (in Hertz): "))
    # Stores the lowest frequency of the band pass filter.
    lowFreqFilter = int(input("Enter the lowest frequency of the band pass filter (in Hertz): "))
    # Stores the highest frequency of the band pass filter.
    highFreqFilter = int(input("Enter the highest frequency of the band pass filter (in Hertz): "))
    # Stores the number of harmonics to investigate.
    numHarmonics = int(input("How many harmonics do you want to investigate? "))

    for harmonic in range(fundementalFreq, fundementalFreq * numHarmonics + 1, fundementalFreq):
        curHarmonic = str(int(harmonic / fundementalFreq))
        if harmonic > highFreqFilter or harmonic < lowFreqFilter:
            print ("Harmonic " + curHarmonic + " is completely filtered")
        elif harmonic < (1.1 * lowFreqFilter) or harmonic > (.9 * highFreqFilter):
            print ("Harmonic " + curHarmonic + " is partially filtered")
        else:
            print ("Harmonic " + curHarmonic + " is not filtered")



# Cautionary if, so that this file only executes main if it is meant to run main when executed or referenced.
if __name__ == "__main__":
    main()