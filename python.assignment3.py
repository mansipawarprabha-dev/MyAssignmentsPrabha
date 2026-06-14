
#Challenge 1: Create a module named calculator.py containing functions add(), subtract(), multiply(), divide(). Import the module in another file and perform all operations. #
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))

#Challenge 2: Create a module named employee.py. Store employee name and salary. Create a function to display employee details. Import and use the function in another file. #
employee_name = "John"
salary = 50000

def display_employee():
    print("Employee Name:", employee_name)
    print("Salary:", salary)

import employee

employee.display_employee()

#Challenge 3: Import the math module and write a program to find square root of 144, value of pi, and factorial of 6. 
import math

print("Square Root of 144:", math.sqrt(144))
print("Value of Pi:", math.pi)
print("Factorial of 6:", math.factorial(6))

#Challenge 4: Import the random module and generate a random number between 1 and 100 and a random choice from ['Python', 'Java', 'React', 'Django'].
import random

print("Random Number:", random.randint(1, 100))

languages = ['Python', 'Java', 'React', 'Django']
print("Random Choice:", random.choice(languages))

#Challenge 5: Create a custom module area.py with functions area_circle() and area_rectangle(). Import the module and calculate areas. 
import math

def area_circle(radius):
    return math.pi * radius * radius

def area_rectangle(length, width):
    return length * width

import area

print("Circle Area:", area.area_circle(5))
print("Rectangle Area:", area.area_rectangle(10, 4))

#Challenge 6: Create a class Student with attributes name and age. Create an object and display the values. 
class Student:
    name = "Rahul"
    age = 20

s1 = Student()

print("Name:", s1.name)
print("Age:", s1.age)

#Challenge 7: Create a class Car with attributes brand and model. Create two objects and display details. 
class Car:
    pass

car1 = Car()
car1.brand = "Toyota"
car1.model = "Camry"

car2 = Car()
car2.brand = "Honda"
car2.model = "City"

print(car1.brand, car1.model)
print(car2.brand, car2.model)

#Challenge 8: Create a class Book with attributes title, author, and price. Create three objects and display details. 
class Book:
    pass

b1 = Book()
b1.title = "Python Basics"
b1.author = "John"
b1.price = 500

b2 = Book()
b2.title = "Java Guide"
b2.author = "Mike"
b2.price = 600

b3 = Book()
b3.title = "React Mastery"
b3.author = "David"
b3.price = 700

for book in [b1, b2, b3]:
    print(book.title, book.author, book.price)

#Challenge 9: Create a class Laptop with attributes brand, RAM, and price. Create two objects and print information. 
class Laptop:
    pass

l1 = Laptop()
l1.brand = "Dell"
l1.ram = "8GB"
l1.price = 50000

l2 = Laptop()
l2.brand = "HP"
l2.ram = "16GB"
l2.price = 70000

print(l1.brand, l1.ram, l1.price)
print(l2.brand, l2.ram, l2.price)

#Challenge 10: Create a class Mobile with attributes company, model, and storage. Create multiple objects and display details.  
class Mobile:
    pass

m1 = Mobile()
m1.company = "Samsung"
m1.model = "Galaxy S23"
m1.storage = "128GB"

m2 = Mobile()
m2.company = "Apple"
m2.model = "iPhone 15"
m2.storage = "256GB"

print(m1.company, m1.model, m1.storage)
print(m2.company, m2.model, m2.storage)

#Challenge 11: Create a class Employee. Use constructor to initialize emp_id, emp_name, and salary. Display employee information. 
class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary

    def display(self):
        print(self.emp_id, self.emp_name, self.salary)

e1 = Employee(101, "Rahul", 50000)
e1.display()

#Challenge 12: Create a class BankAccount. Initialize account_number, holder_name, and balance. Create two accounts and display details. 
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def display(self):
        print(self.account_number, self.holder_name, self.balance)

a1 = BankAccount(1001, "Rahul", 25000)
a2 = BankAccount(1002, "Priya", 40000)

a1.display()
a2.display()

#Challenge 13: Create a class Movie. Initialize movie_name, hero, and rating. Display movie details. 
class Movie:
    def __init__(self, movie_name, hero, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.rating = rating

    def display(self):
        print(self.movie_name, self.hero, self.rating)

m = Movie("KGF", "Yash", 9.0)
m.display()

#Challenge 14: Create a class Product. Initialize product_id, product_name, and price. Create multiple products and print details. 
class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def display(self):
        print(self.product_id, self.product_name, self.price)

p1 = Product(1, "Laptop", 50000)
p2 = Product(2, "Mobile", 30000)

p1.display()
p2.display()

#Challenge 15: Create a class College. Initialize college_name, city, and students_count. Display details using objects.
class College:
    def __init__(self, college_name, city, students_count):
        self.college_name = college_name
        self.city = city
        self.students_count = students_count

    def display(self):
        print(self.college_name, self.city, self.students_count)

c1 = College("ABC College", "Pune", 5000)
c1.display()

#Challenge 16: Create a class Person. Use self to store name and age. Display values using a method.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

p = Person("Rahul", 25)
p.display()

#Challenge 17: Create a class Animal. Store animal_name and color. Print values using self. 
class Animal:
    def __init__(self, animal_name, color):
        self.animal_name = animal_name
        self.color = color

    def display(self):
        print(self.animal_name, self.color)

a = Animal("Tiger", "Orange")
a.display()

#Challenge 18: Create a class Vehicle. Store company and model. Display details using a method and self. 
class Vehicle:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display(self):
        print(self.company, self.model)

v = Vehicle("Toyota", "Fortuner")
v.display()

#Challenge 19: Create a class Teacher. Store teacher_name and subject. Display teacher information using self. 
class Teacher:
    def __init__(self, teacher_name, subject):
        self.teacher_name = teacher_name
        self.subject = subject

    def display(self):
        print(self.teacher_name, self.subject)

t = Teacher("Sharma", "Maths")
t.display()

#Challenge 20: Create a class Player. Store player_name and team. Print details using self. 
class Player:
    def __init__(self, player_name, team):
        self.player_name = player_name
        self.team = team

    def display(self):
        print(self.player_name, self.team)

p = Player("Virat Kohli", "India")
p.display()

#Challenge 21: Create a class Student with instance attributes name, roll_no, and marks. Create three students and display details. 
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(self.name, self.roll_no, self.marks)

s1 = Student("Rahul", 1, 90)
s2 = Student("Priya", 2, 85)
s3 = Student("Amit", 3, 95)

s1.display()
s2.display()
s3.display()

#Challenge 22: Create a class Employee with instance attributes emp_id, emp_name, and department. Display all employee details. 
class Employee:
    def __init__(self, emp_id, emp_name, department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department

    def display(self):
        print(self.emp_id, self.emp_name, self.department)

e1 = Employee(101, "Rahul", "HR")
e1.display()

#Challenge 23: Create a class Hospital with instance attributes doctor_name and specialization. Create multiple objects and display details. 
class Hospital:
    def __init__(self, doctor_name, specialization):
        self.doctor_name = doctor_name
        self.specialization = specialization

    def display(self):
        print(self.doctor_name, self.specialization)

h1 = Hospital("Dr. Sharma", "Cardiology")
h2 = Hospital("Dr. Mehta", "Neurology")

h1.display()
h2.display()

#Challenge 24: Create a class Course with instance attributes course_name, duration, and fees. Display course details. 
class Course:
    def __init__(self, course_name, duration, fees):
        self.course_name = course_name
        self.duration = duration
        self.fees = fees

    def display(self):
        print(self.course_name, self.duration, self.fees)

c = Course("Python", "3 Months", 15000)
c.display()

#Challenge 25: Create a class CricketPlayer with instance attributes player_name, runs, and matches. Display player details.  
class CricketPlayer:
    def __init__(self, player_name, runs, matches):
        self.player_name = player_name
        self.runs = runs
        self.matches = matches

    def display(self):
        print(self.player_name, self.runs, self.matches)

p = CricketPlayer("Virat Kohli", 13000, 275)
p.display()

#Challenge 26: Create a class Rectangle with an instance method calculate_area(). Take length and width from constructor. 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

r = Rectangle(10, 5)
print("Area:", r.calculate_area())

#Challenge 27: Create a class Circle with an instance method calculate_area(). Take radius from constructor. 
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

c = Circle(5)
print("Area:", c.calculate_area())

#Challenge 28: Create a class Employee with an instance method annual_salary(). Calculate yearly salary. 
class Employee:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

e = Employee(50000)
print("Annual Salary:", e.annual_salary())

#Challenge 29: Create a class Student with an instance method calculate_percentage(). Calculate percentage from marks.
class Student:
    def __init__(self, marks, total_marks):
        self.marks = marks
        self.total_marks = total_marks

    def calculate_percentage(self):
        return (self.marks / self.total_marks) * 100

s = Student(450, 500)
print("Percentage:", s.calculate_percentage())

#Challenge 30: Create a class BankAccount with methods deposit() and withdraw(). Update account balance.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Balance:", self.balance)

account = BankAccount(10000)

account.deposit(5000)
account.withdraw(3000)
account.display_balance()