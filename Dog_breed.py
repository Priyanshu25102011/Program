class Dog:
    def __init__(him, name, age, height):
        him.name = name
        him.age = age
        him.height = height

GermanShepherd = Dog("German Shepherd", 5, 24)
Bulldog = Dog("Bulldog", 6, 15)
print("1st dog is a {}".format(GermanShepherd.name))
print("2nd dog is a {}".format(Bulldog.name))
print("{} is {} years old and {} inches tall".format(GermanShepherd.name, GermanShepherd.age, GermanShepherd.height))
print("{} is {} years old and {} inches tall".format(Bulldog.name, Bulldog.age, Bulldog.height))