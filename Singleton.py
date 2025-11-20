class Singleton:
    single = None
    
    def __new__(cls):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance

a = Singleton()
b = Singleton()
print(a is b) 