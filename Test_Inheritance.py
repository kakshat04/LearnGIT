class Taxi:
    def __init__(self, model, capacity, variant):
        self.model = model
        self.capacity = capacity
        self.variant = variant

    def getModel(self):
        return self.model

    def getCapacity(self):
        return self.capacity

    def setCapacity(self, capacity):
        self.capacity = capacity

    def getVariant(self):
        return self.variant

    def setVariant(self, variant):
        self.variant = variant

    def vehicleInfo(self):
        return self.getModel() + " " + self.getCapacity() + " " + self.getModel()


class Vehicle(Taxi):
    def __init__(self, model, capacity, variant, color):
        super().__init__(model, capacity, variant)
        self.__color = color
        self.model = model
        self.capacity = capacity
        self.variant = variant

    def vehicleInfo(self):
        # return self.getModel() + " " + self.getCapacity() + " " + self.getModel() + " " + self.__color
        return Taxi(self.model, self.capacity, self.variant).getModel()


if __name__ == '__main__':
    obj1 = Taxi("kwid", "1000CC", "RXT")
    print(obj1.getModel())
    obj2 = Vehicle("Kwid", "1000CC", "RXT", "Red")
    print(obj2.vehicleInfo())
