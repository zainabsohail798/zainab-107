#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# In[1]:


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person1 = Person("Alice", 25, "New York")
print(person1.name, person1.age, person1.city)


# ## Question 2

# In[2]:


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2020)
print(car1.make, car1.model, car1.year)


# ## Question 3

# In[3]:


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

circle1 = Circle(5)
print("Area:", circle1.area())
print("Circumference:", circle1.circumference())


# ## Question 4

# In[4]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect1 = Rectangle(4, 3)
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())


# ## Question 5

# In[5]:


class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

student1 = Student("John", "R123", [80, 90, 85])
print("Average Marks:", student1.average_marks())


# ## Questionn 6

# In[6]:


class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

book1 = Book("1984", "George Orwell", 1949)
print(book1.title, "-", book1.author, "(", book1.publication_year, ")")


# ## Question 7

# In[7]:


class Employee:
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

emp1 = Employee("Sara", 70000, "Manager")
print(emp1.name, "-", emp1.designation, "-", emp1.salary)


# ## Question 8

# In[8]:


class Bank:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

bank1 = Bank("Ali", "123456", 1000)
bank1.deposit(500)
bank1.withdraw(300)
print("Final Balance:", bank1.balance)


# ## Question 9

# In[9]:


import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

c = Circle(3)
r = Rectangle(4, 5)
t = Triangle(6, 4)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
print("Triangle Area:", t.area())


# ## Question 10

# In[10]:


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog", "Woof")

class Cat(Animal):
    def __init__(self):
        super().__init__("Cat", "Meow")

class Cow(Animal):
    def __init__(self):
        super().__init__("Cow", "Moo")

dog = Dog()
cat = Cat()
cow = Cow()

print(dog.make_sound())
print(cat.make_sound())
print(cow.make_sound())


# In[ ]:




