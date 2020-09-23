# Ben Chappell

def main():
    # Stores the amount of fibbonaci numbers we need to generate to find the one the use requests.
    n = int(input("What is your maximum value? "))


    fibbonaci = [0, 1]

    if n == 0:
        print(fibbonaci[0])
    else:
        tracker = 2
        while fibbonaci[tracker - 1] <= n:
            fibbonaci.append(fibbonaci[tracker - 1] + fibbonaci[tracker - 2]) 
            tracker += 1

        s = ""
        for i in fibbonaci:
            s = s + str(i) + " "

        print (s)    


if __name__ == "__main__":
    main()