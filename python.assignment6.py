
#Question 1 (Hybrid Inheritance) Create a School Management System using Person, Student, Teacher and TeachingAssistant classes. Display complete details of a Teaching Assistant. 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, roll_no, subject):
        Student.__init__(self, name, age, roll_no)
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)

ta = TeachingAssistant("Rahul", 22, 101, "Python")
ta.display()

#Question 2 (Hybrid Inheritance) Create a Vehicle Management System using Vehicle, Car, Bike, ElectricCar and SportsElectricCar classes. 
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class ElectricCar(Car):
    def __init__(self, brand, battery):
        super().__init__(brand)
        self.battery = battery

class SportsElectricCar(ElectricCar):
    def display(self):
        print("Brand:", self.brand)
        print("Battery:", self.battery)

car = SportsElectricCar("Tesla", "100 kWh")
car.display()

#Question 3 (Hybrid Inheritance) Create an Employee System using Employee, Developer, Manager and TechLead classes. Show coding and team-management functionalities. 
class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def code(self):
        print(self.name, "is coding.")

class Manager(Employee):
    def manage_team(self):
        print(self.name, "is managing team.")

class TechLead(Developer, Manager):
    def display(self):
        self.code()
        self.manage_team()

t = TechLead("Amit")
t.display()

#Question 4 (Hybrid Inheritance) Create a Hospital System using Person, Doctor, Nurse and HeadNurse classes. 
class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def diagnose(self):
        print(self.name, "diagnoses patients.")

class Nurse(Person):
    def assist(self):
        print(self.name, "assists doctors.")

class HeadNurse(Nurse, Doctor):
    def display(self):
        self.assist()
        self.diagnose()

h = HeadNurse("Priya")
h.display()

#Question 5 (Hierarchical Inheritance) Create an Animal class and derive Dog, Cat and Cow classes. Implement sound() method in each class. 
class Animal:
    pass

class Dog(Animal):
    def sound(self):
        print("Dog: Bark")

class Cat(Animal):
    def sound(self):
        print("Cat: Meow")

class Cow(Animal):
    def sound(self):
        print("Cow: Moo")

Dog().sound()
Cat().sound()
Cow().sound()

#Question 6 (Hierarchical Inheritance) Create a BankAccount class and derive SavingsAccount, CurrentAccount and FixedDepositAccount classes. 
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(BankAccount):
    pass

class CurrentAccount(BankAccount):
    pass

class FixedDepositAccount(BankAccount):
    pass

s = SavingsAccount(10000)
print("Savings Balance:", s.balance)

#Question 7 (Hierarchical Inheritance) Create an Employee class and derive Developer, Tester and Designer classes. Override work() method. 
class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Tester(Employee):
    def work(self):
        print("Tester tests software")

class Designer(Employee):
    def work(self):
        print("Designer creates UI")

Developer().work()
Tester().work()
Designer().work()

#Question 8 (Hierarchical Inheritance) Create a Shape class and derive Circle, Rectangle and Square classes. Display area calculations. 
class Shape:
    pass

class Circle(Shape):
    def area(self, r):
        return 3.14 * r * r

class Rectangle(Shape):
    def area(self, l, b):
        return l * b

class Square(Shape):
    def area(self, s):
        return s * s

print("Circle Area:", Circle().area(5))
print("Rectangle Area:", Rectangle().area(4, 6))
print("Square Area:", Square().area(4))

#Question 9 (Polymorphism) Create Shape, Circle, Rectangle and Triangle classes. Override area() method and call it using a loop.
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Circle Area = 78.5")

class Rectangle(Shape):
    def area(self):
        print("Rectangle Area = 24")

class Triangle(Shape):
    def area(self):
        print("Triangle Area = 20")

shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    shape.area()

#Question 10 (Polymorphism) Create Payment, CreditCardPayment, UPIPayment and NetBankingPayment classes. Override pay() method. 
class Payment:
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def pay(self):
        print("Paid using Credit Card")

class UPIPayment(Payment):
    def pay(self):
        print("Paid using UPI")

class NetBankingPayment(Payment):
    def pay(self):
        print("Paid using Net Banking")

payments = [CreditCardPayment(), UPIPayment(), NetBankingPayment()]

for p in payments:
    p.pay()

#Question 11 (Polymorphism) Create Notification, EmailNotification, SMSNotification and PushNotification classes. Override send() method. 
class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Email Sent")

class SMSNotification(Notification):
    def send(self):
        print("SMS Sent")

class PushNotification(Notification):
    def send(self):
        print("Push Notification Sent")

notifications = [EmailNotification(), SMSNotification(), PushNotification()]

for n in notifications:
    n.send()

#Question 12 (Polymorphism) Create Animal, Dog, Cat and Lion classes. Override make_sound() method. 
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Lion(Animal):
    def make_sound(self):
        print("Roar")

animals = [Dog(), Cat(), Lion()]

for animal in animals:
    animal.make_sound()

#Question 13 (Polymorphism) Create Employee, Developer, Tester and Manager classes. Override role() method. 
class Employee:
    def role(self):
        pass

class Developer(Employee):
    def role(self):
        print("Developer")

class Tester(Employee):
    def role(self):
        print("Tester")

class Manager(Employee):
    def role(self):
        print("Manager")

employees = [Developer(), Tester(), Manager()]

for emp in employees:
    emp.role()

#Question 14 (Polymorphism) Create Vehicle, Car, Bike and Bus classes. Override start() method. 
class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")

class Bike(Vehicle):
    def start(self):
        print("Bike Started")

class Bus(Vehicle):
    def start(self):
        print("Bus Started")

vehicles = [Car(), Bike(), Bus()]

for v in vehicles:
    v.start()

#Question 15 (Polymorphism + Inheritance) Create Device, Camera, Phone and SmartPhone classes. Demonstrate runtime polymorphism.
class Device:
    def operate(self):
        print("Device Operating")

class Camera(Device):
    def operate(self):
        print("Camera Taking Photos")

class Phone(Device):
    def operate(self):
        print("Phone Making Calls")

class SmartPhone(Phone):
    def operate(self):
        print("SmartPhone Calling, Browsing and Taking Photos")

devices = [Camera(), Phone(), SmartPhone()]

for device in devices:
    device.operate()