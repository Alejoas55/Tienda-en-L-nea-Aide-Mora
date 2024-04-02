class ISuscriber():
    def update(self, message):
        pass

class Notifier():

    def __init__(self) -> None:
        self._susbribers = []
    def attach(self, susvriber:ISuscriber):
        if susvriber not in self._susbribers:
            self._susbribers.append(susvriber)

    def detach(self, susvriber:ISuscriber):
        if susvriber in self._susbribers:
            self._susbribers.remove(susvriber)
    
    def notify(self, message):
        for susvriber in self._susbribers:
            susvriber.update(message)

class subscriber(ISuscriber):
    def __init__(self, name):
        super().__init__()
        self._name=name

    def update(self, message):
        print(f"{self._name} recibio el mensaje :{message}")

if __name__ == '__main__':
    notifier = Notifier()
    subscriber_1 =  subscriber("Juan")
    subscriber_2 = subscriber("Pedro")

    notifier.attach(subscriber_1)
    notifier.attach(subscriber_2)

    notifier.notify("Ha ocurrido un evento")

    notifier.detach(subscriber_2)
    notifier.notify("Se ha eliminado a Pedro")