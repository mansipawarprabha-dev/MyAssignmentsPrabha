
#Question 1: Create a Student class with instance variables name and age. Create 3 objects and display their details. 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name, "Age:", self.age)

s1 = Student("Rahul", 20)
s2 = Student("Priya", 21)
s3 = Student("Amit", 19)

s1.display()
s2.display()
s3.display()

#Question 2: Create an Employee class with a constructor to initialize employee id, name, and salary. 
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.emp_id, self.name, self.salary)

e1 = Employee(101, "John", 50000)
e1.display()

#Question 3: Create a Car class with instance variables brand and model. Write an instance method to display car details. 
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

c1 = Car("Toyota", "Fortuner")
c1.display()

#Question 4: Create a BankAccount class with deposit() and withdraw() instance methods. 
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print("Balance:", self.balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
acc.display()

#Question 5: Create a Book class and create multiple objects to store book information. 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(self.title, "-", self.author)

b1 = Book("Python", "Guido")
b2 = Book("Java", "James Gosling")

b1.display()
b2.display()

#Question 6: Create a Mobile class with a constructor and display mobile details using an instance method. 
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

m1 = Mobile("Samsung", 30000)
m1.display()

#Question 7: Create a Company class with a class variable company_name shared by all employees. 
class Company:
    company_name = "ABC Pvt Ltd"

    def __init__(self, emp_name):
        self.emp_name = emp_name

    def display(self):
        print(self.emp_name, "-", Company.company_name)

e1 = Company("Rahul")
e2 = Company("Priya")

e1.display()
e2.display()

#Question 8: Create a Product class with a class variable tax_rate and calculate the final product price. 
class Product:
    tax_rate = 0.18

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price + (self.price * Product.tax_rate)

p = Product(1000)
print("Final Price:", p.final_price())

#Question 9: Create a Student class with a class method to update the school name for all students. 
class Student:
    school_name = "ABC School"

    @classmethod
    def update_school(cls, new_name):
        cls.school_name = new_name

print(Student.school_name)

Student.update_school("XYZ School")
print(Student.school_name)

#Question 10: Create a Vehicle class with a class variable vehicle_count. Count the total number of vehicles created. 
class Vehicle:
    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1

v1 = Vehicle()
v2 = Vehicle()
v3 = Vehicle()

print("Total Vehicles:", Vehicle.vehicle_count)

#Question 11: Create a Calculator class with static methods add(), subtract(), multiply(), and divide(). 
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

print(Calculator.add(10, 5))
print(Calculator.subtract(10, 5))
print(Calculator.multiply(10, 5))
print(Calculator.divide(10, 5))

#Question 12: Create a TemperatureConverter class with a static method to convert Celsius to Fahrenheit. 
class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))

#Question 13: Create a Utility class with a static method to check whether a number is even or odd. 
class Utility:

    @staticmethod
    def check_number(num):
        if num % 2 == 0:
            return "Even"
        return "Odd"

print(Utility.check_number(10))

#Question 14: Create a Person class and a Student class that inherits from Person. Display inherited properties. 
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

s = Student("Rahul", 101)

print(s.name)
print(s.roll)

#Question 15: Create a Vehicle class and a Bike class that inherits from Vehicle. Add extra properties in Bike. 
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, mileage):
        super().__init__(brand)
        self.mileage = mileage

b = Bike("Honda", 50)

print(b.brand)
print(b.mileage)

#Question 16: Create a Shape class and inherit Circle and Rectangle classes from it. 
class Shape:
    pass

class Circle(Shape):
    def area(self, r):
        return 3.14 * r * r

class Rectangle(Shape):
    def area(self, l, b):
        return l * b

c = Circle()
r = Rectangle()

print(c.area(5))
print(r.area(4, 6))

#Question 17: Create an Animal class and inherit Dog and Cat classes. Display different sounds using methods. 
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()

#Question 18: Create a Person class with private variable __salary and access it using getter and setter methods. 
class Person:
    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

p = Person()

print(p.get_salary())

p.set_salary(60000)

print(p.get_salary())

#Question 19: Create a BankAccount class and implement encapsulation using private balance variable. 
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()

acc.deposit(1000)

print(acc.get_balance())

#Question 20: Create an Employee class with private data and update it using setter methods. 
class Employee:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

e = Employee()

e.set_salary(50000)

print(e.get_salary())

#Question 21: Create a Library Management System using classes, objects, constructors, and methods. 
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

lib = Library()

lib.add_book("Python")
lib.add_book("Java")

lib.display_books()

#Question 22: Create a Hospital Management System using inheritance and encapsulation concepts. 
class Person:
    def __init__(self, name):
        self.name = name

class Patient(Person):
    def __init__(self, name, disease):
        super().__init__(name)
        self.__disease = disease

    def display(self):
        print(self.name, self.__disease)

p = Patient("Rahul", "Fever")
p.display()

#Question 23: Create a School Management System using class variables, class methods, and instance methods.
class School:
    school_name = "ABC School"

    def __init__(self, student):
        self.student = student

    @classmethod
    def change_school(cls, name):
        cls.school_name = name

    def display(self):
        print(self.student, School.school_name)

s = School("Rahul")
s.display()

School.change_school("XYZ School")

s.display()

#Question 24: Create an Online Shopping System using OOP concepts including inheritance. 
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    def display(self):
        print(self.name, self.price)

e = Electronics("Laptop", 50000)
e.display()

#Question 25: Create a Mini ATM System using encapsulation, constructors, and instance methods.
class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Balance:", self.__balance)

atm = ATM(5000)

atm.deposit(1000)
atm.withdraw(2000)

atm.check_balance()