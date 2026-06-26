#1. Animal → Dog and Cat (Inheritance)
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Cat(Animal):
    def meow(self):
        print("Cat meows")


dog = Dog()
dog.sound()
dog.bark()

cat = Cat()
cat.sound()
cat.meow()

#2. Vehicle → Car → ElectricCar (Multilevel Inheritance)
class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


e = ElectricCar()

e.start()
e.drive()
e.charge()

#3. Method Overriding
class Animal:
    def sound(self):
        print("Animal Sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()

#4. Multiple Inheritance
class Father:
    def skill1(self):
        print("Driving")


class Mother:
    def skill2(self):
        print("Cooking")


class Child(Father, Mother):
    pass


c = Child()

c.skill1()
c.skill2()

#5. Polymorphism with Shapes
class Rectangle:
    def area(self):
        print("Area of Rectangle")


class Circle:
    def area(self):
        print("Area of Circle")


def show_area(shape):
    shape.area()


r = Rectangle()
c = Circle()

show_area(r)
show_area(c)

#6. Bank System
class BankAccount:
    def __init__(self, balance):
        self.balance = balance


class SavingsAccount(BankAccount):
    def show_balance(self):
        print("Savings Balance:", self.balance)


class CurrentAccount(BankAccount):
    def show_balance(self):
        print("Current Balance:", self.balance)


s = SavingsAccount(10000)
c = CurrentAccount(5000)

s.show_balance()
c.show_balance()

#7. Private Attributes with Getter and Setter
class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


s = Student()

s.set_marks(85)

print("Marks:", s.get_marks())

#8. Teacher and Student Class
class Teacher:
    def teach(self):
        print("Teaching students")


class Student(Teacher):
    def study(self):
        print("Studying")


s = Student()

s.teach()
s.study()

#9. MusicPlayer and Spotify (Method Overriding)
class MusicPlayer:
    def play(self):
        print("Playing music")


class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")


music = Spotify()

music.play()

#10. Using super() in Inheritance
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s = Student("Shivam", 20)

s.display()