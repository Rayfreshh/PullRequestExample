class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."
    
# Example usage
if __name__ == "__main__":
    my_dog = Dog("Buddy", 3)
    print(my_dog.bark())
    print(my_dog.get_info()) #fixed the closed parentheses
    
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        return "Meow!"

    def get_info(self):
        return f"{self.name} is a {self.color} cat."
    
# Example usage
if __name__ == "__main__":
    my_cat = Cat("Whiskers", "black")
    print(my_cat.meow())
    print(my_cat.get_info())