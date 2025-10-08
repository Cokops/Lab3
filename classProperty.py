class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def info(self):
        return f"{self.name}, {self.age} лет"

person = Person("Иисус", 2025)
print(person.info)