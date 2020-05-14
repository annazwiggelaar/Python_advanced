import time

def readposint():
    try:
        i = int(input("Please provide a number: "))
        assert i >= 0
    except ValueError:
        print("You did not enter a number.")
    except AssertionError:
        print("The number you provided is negative.")
    else:
        print("The positive integer you provided is:", i)
    finally:
        print("Thank you.")


print(readposint())
