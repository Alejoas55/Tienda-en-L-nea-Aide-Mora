class Singleton ():
    intance = None

    def __new__(cls, *args, **kwargs): #se ejecuta antes que el contructor
        if cls.intance is None: 
            cls.intance = super().__new__(cls, *args, **kwargs)
        return cls.intance
    
    def __init__(self):
        self.opcion_1 = 'opcion 1'
        self.opcion_2 = 'opcion 2'
        
singleton_1 = Singleton()
singleton_2 = Singleton()

print(singleton_1)
print(singleton_2)
