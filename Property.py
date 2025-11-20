class Person:
    def __init__(self, age):
        self._age = age 
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print("Возраст не может быть отрицательным!")
        elif value > 150:
            print("Слишком большой возраст!")
        else:
            self._age = value

person = Person(25)
print(person.age)

person.age = -5     
person.age = 30      
print(person.age)    