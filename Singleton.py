class singleton ():
    intance = None

    def __init__(self) -> None:
        if singleton.intance is not None:
            raise  Exception("Esta clase ya esta intanciada")
        singleton.intance = self #Algo falta revisar 
        self.opcion_1 = 'opcion 1'
        self.opcion_2 = 'opcion 2'
    
    @classmethod
    def get_Instancia():
        if singleton.intance is None:
            singleton.intance = singleton

        return singleton.intance

singleton_1 = singleton.get_Instancia() #revisar que esta mal 
singleton_2 = singleton.get_Instancia()

print(singleton_1)
print(singleton_2)

singleton_1.opcion_1 = 'prueba'
print(singleton_1.opcion_1)
print(singleton_2.opcion_1)