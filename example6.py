class Animal:
    def sound(self):
        print("Animal makes sound")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow")

c = Cat()
c.sound()