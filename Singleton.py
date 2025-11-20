class Singleton:
    single = None
    
    def __new__(cls):
        if not cls.single:
            cls.single = object.__new__(cls)
        return cls.single

a = Singleton()
b = Singleton()
print(a is b) 