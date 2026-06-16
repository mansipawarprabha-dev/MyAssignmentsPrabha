
#Question 1: Abstract Class & Abstract Method 
#Create an abstract class Vehicle. 
#• Create an abstract method start(). 
#• Create a child class Car. 
#• Implement the start() method in Car. 
#• Create an object of Car and call start(). 

#Expected Output: Car is starting... 
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car is starting...")

c = Car()
c.start()

#Question 2: Abstract Class with Multiple Child Classes 
#Create an abstract class Animal. 
#• Create an abstract method sound(). 
#• Create two child classes: Dog and Cat. 
#• Implement the sound() method in both classes. 
#• Create objects and call sound(). 

#Expected Output: Dog barks 
#                 Cat meows 
 from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog barks")

class Cat(Animal):

    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()
 
#Question 3: Polymorphism Using Method Overriding 
#Create a class Shape. 
#• Create a method draw(). 
#• Create child classes: Circle and Rectangle. 
#• Override the draw() method in both child classes. 
#• Call the draw() method using objects. 

#Expected Output: Drawing Circle 
#                 Drawing Rectangle 
class Shape:

    def draw(self):
        print("Drawing Shape")

class Circle(Shape):

    def draw(self):
        print("Drawing Circle")

class Rectangle(Shape):

    def draw(self):
        print("Drawing Rectangle")

c = Circle()
r = Rectangle()

c.draw()
r.draw()

#Question 4: Polymorphism with Loop Create a class Bird. 
#• Create a method fly(). 
#• Create child classes: Sparrow and Eagle. 
#• Override the fly() method. 
#• Store objects in a list and call fly() using a loop. 

#Expected Output: Sparrow flies low 
#                 Eagle flies high
class Bird:

    def fly(self):
        pass

class Sparrow(Bird):

    def fly(self):
        print("Sparrow flies low")

class Eagle(Bird):

    def fly(self):
        print("Eagle flies high")

birds = [Sparrow(), Eagle()]

for bird in birds:
    bird.fly()

#Question 5: Abstract Class + Polymorphism 
#Create an abstract class Employee. 
#• Create an abstract method work(). 
#• Create two child classes: Developer and Designer. 
#• Implement the work() method in both classes. 
#• Store objects in a list and call work() using a loop 

#Expected Output: Developer writes code 
#                 Designer creates UI designs
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):

    def work(self):
        print("Developer writes code")

class Designer(Employee):

    def work(self):
        print("Designer creates UI designs")

employees = [Developer(), Designer()]

for emp in employees:
    emp.work()