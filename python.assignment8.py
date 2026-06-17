
#Question 1: Handle Division by Zero
#Write a program that:
#Takes two numbers as input.
#Divides the first number by the second number.
#Handles the ZeroDivisionError exception.
#Example:
#Enter first number: 10
#Enter second number: 0
#Cannot divide by zero.
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

#Question 2: Handle Invalid Number Input
#Write a program that:
#Takes a number from the user.
#Handles the ValueError exception if the user enters text instead of a number.
#Example:
#Enter a number: abc
#Invalid input. Please enter a number.
try:
    num = float(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input. Please enter a number.")

#Question 3: Using try and except
#Write a program that:
#Creates a list containing 5 numbers.
#Takes an index from the user.
#Prints the element at that index.
#Handles the IndexError exception.
#Example:
#Enter index: 10
#Index out of range.
numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Element:", numbers[index])

except IndexError:
    print("Index out of range.")

#Question 4: Using else Block
#Write a program that:
#Uses else to display the result when no exception occurs.
#Example:
#Result: 5.0
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

#Question 5: Using finally Block
#Write a program that:
#Opens a file using open().
#Uses try-except-finally.
#Prints a message in the finally block.
#Expected Output:
#File operation completed.
try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found.")

finally:
    print("File operation completed.")

#Question 6: Multiple Exceptions
#Write a program that:
#Takes a number and an index from the user.
#Handles both:
#ValueError
#IndexError
#Example:
#Invalid input.
#or
#Index out of range.
numbers = [10, 20, 30, 40, 50]

try:
    num = int(input("Enter a number: "))
    index = int(input("Enter an index: "))

    print("Number:", num)
    print("Element:", numbers[index])

except ValueError:
    print("Invalid input.")

except IndexError:
    print("Index out of range.")

#Question 7: Custom Exception
#Create a custom exception named NegativeNumberError.
#Take a number from the user.
#Raise the exception if the number is negative.
#Display an appropriate error message.
#Example:
#Enter a number: -5
#Negative numbers are not allowed.
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise NegativeNumberError

    print("You entered:", num)

except NegativeNumberError:
    print("Negative numbers are not allowed.")
