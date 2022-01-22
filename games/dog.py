class Dog:

    species = 'Canis Familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #Instance method
    #def description(self):
    def __str__(self) :
        return f"{self.name} is {self.age} years old"
    
    #Another instance method
    def speak(self, sound):
        return f"{self.name} says: {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        #return f"{self.name} says {sound}"
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
tom = GoldenRetriever("Tom", 2)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))
print(miles.speak())
print(miles.speak("Grrr"))
print(tom.speak())

print(type(miles))
print(isinstance(miles,Dog))
print(isinstance(miles, Bulldog))
print(isinstance(jack, Dachshund))

''' for pet in (miles, jack, buddy, jim):
    print(f"This dog is {pet.name} and he is {pet.age} years old ") '''