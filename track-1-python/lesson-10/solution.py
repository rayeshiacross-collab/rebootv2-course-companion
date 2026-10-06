try:
    number = int(input("Number: "))
    print(100 / number)
except ValueError:
    print("Please enter a valid whole number.")
except ZeroDivisionError:
    print("The number cannot be zero.")
