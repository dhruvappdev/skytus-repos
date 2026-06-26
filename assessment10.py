#1. Car Class
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print("Speed:", self.speed)

    def brake(self):
        self.speed -= 10
        print("Speed:", self.speed)


car = Car("Toyota", "Fortuner", 50)

car.accelerate()
car.brake()

#2. BankAccount Class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance:", self.balance)
        else:
            print("Insufficient Balance")


account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)

#3. Student Class
class Student:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        print("Average =", avg)


student = Student(80, 90, 85)

student.average()

#4. Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(10, 5)

print("Area =", rect.area())
print("Perimeter =", rect.perimeter())

#5. Employee Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


emp = Employee("Shivam", 50000)

emp.display()

#6. Book Class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


book = Book("Python Basics", "John", 499)

book.display()

#7. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


circle = Circle(7)

print("Area =", circle.area())
print("Circumference =", circle.circumference())

#8. Laptop Class
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount):
        self.price = self.price - (self.price * discount / 100)
        print("New Price =", self.price)


laptop = Laptop("Dell", 50000)

laptop.apply_discount(10)

#9. Flight Class
class Flight:
    def __init__(self, seats):
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat Booked")
            print("Available Seats:", self.seats)
        else:
            print("No Seats Available")


flight = Flight(5)

flight.book_seat()
flight.book_seat()

#10. Shop Class
class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print("Products:")
        for product in self.products:
            print(product)


shop = Shop()

shop.add_product("Laptop")
shop.add_product("Mouse")
shop.add_product("Keyboard")

shop.list_products()

