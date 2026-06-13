
#Write a program to display your name, college name, and favorite programming language using print()
print("Name: Mansi")
print("College: zeal College")
print("Favorite Programming Language: Python")

#Take user input for name and age, then display: "Hello Sham, you are 22 years old."
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name + ", you are", age, "years old.")

#Create variables for: ● Student name ● Roll number ● Percentage ● Passed status Print all values in a formatted way. 
student_name = "Sham Patil"
roll_number = 101
percentage = 85.5
passed_status = True

print("Student Details")
print("---------------")
print("Name:", student_name)
print("Roll Number:", roll_number)
print("Percentage:", percentage)
print("Passed Status:", passed_status)

#Identify which of the following variable names are invalid and rewrite them correctly: ● 1name ● student-name
#  ● class ● total marks ● user_name 
#In Python, variable names:

#Cannot start with a number.
#Cannot contain spaces or hyphens (-).
#Cannot be reserved keywords.
#Can contain letters, numbers, and underscores (_).

#Variable Name	Valid/Invalid	Correct Form
#student-name	❌ Invalid (contains hyphen)	student_name
#class	        ❌ Invalid (Python keyword)	class_name
#total marks	❌ Invalid (contains space)	total_marks

#Create variables of type: ● int ● float ● str ● bool Print each variable with its data type using type(). 
# Variables of different data types
age = 22               # int
percentage = 85.5      # float
name = "Sham"          # str
passed = True          # bool

# Print values and their data types
print(age, type(age))
print(percentage, type(percentage))
print(name, type(name))
print(passed, type(passed))

#Take two numbers as input from the user and display their sum. 
# Take two numbers as input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and display the sum
sum = num1 + num2

print("Sum =", sum)

#Take a decimal number as input and convert it into: ● integer ● string Display all converted values. 
# Take a decimal number as input
num = float(input("Enter a decimal number: "))

# Convert to integer and string
integer_value = int(num)
string_value = str(num)

# Display converted values
print("Original Value:", num)
print("Integer Value:", integer_value)
print("String Value:", string_value)

#Take user input for age and check whether the input type is string or integer. 
# Take age as input
age = input("Enter your age: ")

# Check input type
print("Value entered:", age)
print("Type before conversion:", type(age))

# Convert to integer
age = int(age)

# Check type after conversion
print("Type after conversion:", type(age))

#Write a program to perform: ● Addition ● Subtraction ● Multiplication ● Division ● Modulus on two user-input numbers. 
# Take two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)

#Take two numbers and display: ● Greater than ● Less than ● Equal to ● Not equal to comparison results. 
# Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Comparisons
print("Greater than:", num1 > num2)
print("Less than:", num1 < num2)
print("Equal to:", num1 == num2)
print("Not equal to:", num1 != num2)

#Create a login system using logical operators: ● Username must be "admin" ● Password must be "1234"
#Display login success or failure. 
# Predefined credentials
username = "admin"
password = "1234"

# Take input from user
user_input = input("Enter username: ")
pass_input = input("Enter password: ")

# Check login using logical operators
if user_input == username and pass_input == password:
    print("Login Successful")
else:
    print("Login Failed")

#Write a program to check whether a number is: ● Positive ● Negative ● Zero 
# Take input from user
num = float(input("Enter a number: "))

# Check condition
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

#Take marks as input and print grade: ● A → 90 and above ● B → 75 to 89 ● C → 50 to 74 ● Fail → below 50 
marks = float(input("Enter your marks: "))

# Determine grade
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

#Write a program to check whether a number is even or odd. 
# Take input from user
num = int(input("Enter a number: "))

# Check even or odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#Take age as input and determine: ● Child ● Teenager ● Adult ● Senior Citizen 
age = int(input("Enter your age: "))

# Determine age group
if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")

#Create a simple calculator using if-elif-else. Operations: ● Addition ● Subtraction ● Multiplication ● Division 
# Simple Calculator using if-elif-else

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    print("Result:", num1 + num2)

elif choice == "2":
    print("Result:", num1 - num2)

elif choice == "3":
    print("Result:", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid choice")

#