class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print(self.name + " гавкает " + self.sound)

test_dog = Dog("Слоняра","Гав-Гав")
test_dog.speak()