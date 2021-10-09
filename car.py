print("######################## Car Class #########################")
class Car:

	def __init__(self,color,mileage):
		self.color= color
		self.mileage= mileage

	def __str__(self):
		return f"The {self.color} car has {self.mileage} miles "

car1= Car(color="blue", mileage=20000)
car2= Car(color="red", mileage=30000)

print(car1)
print(car2)




print("\n######################## Dog Class #########################")
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):

    def speak(self, sound="Bark"):
        return super().speak(sound)

miles= GoldenRetriever(name="Miles",age=4)
miles.speak("bow bow")
isinstance(miles,Dog) #returns True

print(miles)
print("Type of miles= ",type(miles))
print(miles.speak())
