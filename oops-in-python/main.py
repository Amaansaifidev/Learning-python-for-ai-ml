class Car:
    def __init__(self, model, color, no):
        self.model = model
        self.color = color
        self.no = no

    def startcar(self):
        print(f"{self.color} car has started")

car1 = Car(2010, "blue", 345)
car1.startcar()
