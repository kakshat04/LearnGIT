class Employee:
    # id = 10
    # name = "Akshat"

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display_data(self):
        print(self.id, self.name)
        # print(Employee.id, Employee.name)


obj1 = Employee(20, "Kumar")
obj1.display_data()
obj2 = Employee(10, "Akshat")
obj2.display_data()

print(getattr(obj1, 'id'))
print(setattr(obj1, "Name", "Anjul"))
print(obj1.__dict__)
print(obj1.__dir__())
print(obj1.__module__)

class Test:
    count = 0

    def __init__(self):
        Test.count += 1


# class Animal:
#     def speak(self):
#         print("Speakindg")
#
#     def walk(self):
#         print("General Walk")
#
#
# class Dog(Animal):
#     def walk(self):
#         print("Dog walk")
#
#     def bark(self):
#         print("Barking")
#         print(Animal.walk(self))
#         print(self.walk())
#
#
# class DogChild(Dog):
#     def eat(self):
#         print("Eating")
#         print(Animal.walk(self))
#         print(Dog.walk(self))
#
#     def walk(self):
#         print("Dog Child Walk")
#
#
# d1 = DogChild()
# # d1.speak()
# # d1.bark()
# d1.walk()


class Animal:
    def speak(self):
        print("Speakindg")

    def walk(self):
        print("General Walk")
class Dog:
    def bark(self):
        print("Barking")

    def walk(self):
        print("Dog walk")
class DogChild(Dog):
    def eat(self):
        print("Eating")

    # def walk(self):
    #     print("Dog Child Walk")


d1 = DogChild()
d1.walk()
# d1.speak()
print(issubclass(DogChild, Animal))
print(isinstance(d1, Animal))


class Employee:
    __count = 0;
    def __init__(self):
        Employee.__count = Employee.__count+1
    def display(self):
        print("The number of employees",Employee.__count)

obj1 = Employee()
print(obj1.display())
print(obj1.__dir__())
print(obj1._Employee__count)
print(obj1._Employee__count)


## Learning super() function
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def tes1(self):
        print(self.a)

    def test2(self):
        print(self.b)


class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def test1(self):
        # super(B, self).tes1()
        super().tes1()
        # A.tes1(self)
        print(self.a, self.b, self.c)



obj = B(10, 20, 30)
print(obj.test1())  # this will call test1 of child class


####################################################
class Animal:
    def __init__(self, legs, eyes):
        self.__legs = legs
        self.__eyes = eyes

    def walk(self):
        print("Using {} number Legs".format(self.__legs))

    def sleep(self):
        print("Using {} number eyes".format(self.__eyes))

    def speak(self):
        print("Animals Talk")


class Dogs(Animal):
    def __init__(self, legs, eyes, pet):
        super().__init__(legs, eyes)
        self.pet = pet

    def dog_walk(self):
        print("Using {} number Legs".format(self.__legs))

    def dog_sleep(self):
        print("Using {} number eyes".format(self.__eyes))

    def isPet(self):
        print("{} Dog is pet".format(self.pet))

    def speak(self):
        print("Dogs Bark")


class Human(Animal):
    def __init__(self, legs, eyes):
        super().__init__(legs, eyes)

    def dog_walk(self):
        print("Using {} number Legs".format(self.__legs))

    def dog_sleep(self):
        print("Using {} number eyes".format(self.__eyes))

    # def isPet(self):
    #     print("{} Dog is pet".format(self.pet))

    def speak(self):
        super().speak()
        # print("Humans Talk")


# obj = Animal(4, 2)
obj = Human(2, 2)
obj.speak()
obj.walk()
obj.sleep()
# obj.isPet()