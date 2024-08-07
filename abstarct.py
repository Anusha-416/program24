from abc import ABC
class Animal(ABC):
   def make_sound(self):
      return "pass"
class dog(Animal):
    def make_sound(self):
        return "bowww"

class cat(dog):
    def make_sound(self):
        return "meoww"
d=dog()
c=cat()
print(d.make_sound())
print(c.make_sound())
