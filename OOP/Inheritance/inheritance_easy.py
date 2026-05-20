class Animal():
    def make_sound(self):
        print("make_sound() called.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

d= Dog()
d.make_sound()
d.bark()