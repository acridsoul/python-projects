num1 = 8


try:
    num2 = int(input("Enter a number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter a number")