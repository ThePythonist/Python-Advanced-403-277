class SedanCar:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def startengine(self):
        pass

    def accelerate(self):
        print(f"{self.name} is accelerating ...")

    def brake(self):
        pass

    def horn(self):
        pass


# Instance(Nemone) - Object(Shey)
car1 = SedanCar("persia", "1399", "white")
car2 = SedanCar("dena", "1397", "black")
car3 = SedanCar("samand", "1402", "blue")

car3.accelerate()
