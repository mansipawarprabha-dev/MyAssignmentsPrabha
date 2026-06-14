
#Create a dictionary to store: ● Student name ● Age ● Course ● City Print all dictionary values. 
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "city": "Pune"
}
print(student.values())

#Create a dictionary of employee details and access: ● Employee name ● Salary ● Department using keys 
employee = {
    "name": "Amit",
    "salary": 50000,
    "department": "IT"
}

print("Name:", employee["name"])
print("Salary:", employee["salary"])
print("Department:", employee["department"])

#Add a new key-value pair to an existing dictionary. Example: ● Add "email" to student details.  
student = {
    "name": "Rahul",
    "age": 21
}

student["email"] = "rahul@gmail.com"

print(student)

#Update the value of an existing key in a dictionary. 
student = {
    "name": "Rahul",
    "age": 21
}

student["age"] = 22

print(student)

#Remove a key from a dictionary using: ● pop() ● del 
student = {
    "name": "Rahul",
    "age": 21,
    "city": "Pune"
}

student.pop("city")
print(student)

del student["age"]
print(student)

#Print all: ● Keys ● Values ● Key-value pairs from a dictionary using loops. 
student = {
    "name": "Rahul",
    "age": 21,
    "city": "Pune"
}

print("Keys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

#Count how many subjects are present in a student marks dictionary. 
marks = {
    "Math": 80,
    "Science": 75,
    "English": 90,
    "History": 70
}

print("Total Subjects:", len(marks))

#Create a dictionary containing marks of 5 subjects and calculate the total marks. 
marks = {
    "Math": 80,
    "Science": 75,
    "English": 90,
    "History": 70,
    "Computer": 95
}

total = sum(marks.values())

print("Total Marks:", total)

#Check whether a key exists in a dictionary or not. 
student = {
    "name": "Rahul",
    "age": 21
}

key = "age"

if key in student:
    print("Key exists")
else:
    print("Key does not exist")

#Create a dictionary of products with prices and display only products having price greater than 500.
products = {
    "Mouse": 300,
    "Keyboard": 700,
    "Monitor": 8000,
    "Pen Drive": 450
}

for product, price in products.items():
    if price > 500:
        print(product, ":", price)

#Create a set containing 5 numbers and print all elements. Q12. Add new elements into a set using add(). 
numbers = {10, 20, 30, 40, 50}

for num in numbers:
    print(num)

#Remove an element from a set using: ● remove() ● discard() 
numbers = {10, 20, 30}

numbers.add(40)
numbers.add(50)

print(numbers)

#Create two sets and perform: ● Union ● Intersection ● Difference operations. 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

#Find common elements between two sets. 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Check whether a particular value exists in a set. 
numbers = {10, 20, 30, 40}

if 20 in numbers:
    print("Exists")
else:
    print("Not Exists")

#Take a list containing duplicate values and convert it into a set. 
numbers = [10, 20, 20, 30, 40, 40, 50]

unique_numbers = set(numbers)

print(unique_numbers)

#Create a set of student names and display the total number of unique students. 
students = {"Rahul", "Amit", "Priya", "Rahul", "Neha"}

print("Unique Students:", len(students))

#Create two sets of numbers and check whether both sets are equal or not. 
set1 = {1, 2, 3}
set2 = {3, 2, 1}

if set1 == set2:
    print("Sets are Equal")
else:
    print("Sets are Not Equal")

#Remove all elements from a set using clear().
numbers = {10, 20, 30, 40}

numbers.clear()

print(numbers)

#Create a function that prints: "Welcome to Python Programming" 
def welcome():
    print("Welcome to Python Programming")

welcome()

#Create a function to add two numbers and display the result. 
def add(a, b):
    print("Sum =", a + b)

add(10, 20)

#Create a function that accepts a name as a parameter and prints: "Hello, Rohit" 
def greet(name):
    print("Hello,", name)

greet("Rohit")

#Create a function to find the square of a number. #
def square(num):
    return num ** 2

print(square(5))

#Write a function to check whether a number is even or odd. 
def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(7)

#Create a function to calculate the area of a rectangle. 
def area(length, width):
    return length * width

print("Area =", area(10, 5))

#Write a function that returns the greater number between two numbers. 
def greater(a, b):
    return max(a, b)

print(greater(10, 25))

#Create a function to print numbers from 1 to 10. 
def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()

#Write a function to calculate the sum of all numbers in a list. 
def list_sum(numbers):
    return sum(numbers)

print(list_sum([10, 20, 30, 40]))

#Create a function that checks whether a student is pass or fail based on marks. Condition: ● Pass → marks >= 35 ● Fail → marks < 35 
def result(marks):
    if marks >= 35:
        print("Pass")
    else:
        print("Fail")

result(50)

#Create a function with default arguments. Example: ● Default city should be "Pune" 
def student(name, city="Pune"):
    print("Name:", name)
    print("City:", city)

student("Rahul")

#Create a function using keyword arguments. 
def employee(name, salary):
    print("Name:", name)
    print("Salary:", salary)

employee(salary=50000, name="Amit")

#Write a function that accepts multiple numbers using *args and prints them. 
def numbers(*args):
    for num in args:
        print(num)

numbers(10, 20, 30, 40, 50)

#Create a function that returns: ● Maximum number ● Minimum number from a list. 
def find_max_min(numbers):
    return max(numbers), min(numbers)

maximum, minimum = find_max_min([10, 50, 20, 80, 30])

print("Maximum:", maximum)
print("Minimum:", minimum)

#Write a function to count vowels in a string. Best of Luck Interns  Practice daily to improve your Python programming skills. 
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

print(count_vowels("Python Programming"))