class Animal :
    def speak (self):
        print("Animal Makes sound")


class Dog(Animal):
    def bark (self):
        print("Barking...")


d = Dog()
d.speak()
d.bark()