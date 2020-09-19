# Ben Chappell

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
