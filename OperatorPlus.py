class Plus:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Plus(self.value + other.value)
    
    def __str__(self):
        return f"Число: {self.value}"

a = Plus(10)
b = Plus(20)
c = a + b
print(c) 