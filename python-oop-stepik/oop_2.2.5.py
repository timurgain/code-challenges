class Car:
    def __init__(self, model=None):
        self.__model = model

    def __str__(self):
        return f"Марка {self.__model}"

    @staticmethod
    def check_model(model: str) -> bool:
        MIN = 2
        MAX = 100
        return isinstance(model, str) and MIN <= len(model) <= MAX

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.check_model(model):
            self.__model = model

    # model = property()

    # @model.getter
    # def model(self):
    #     return self.__model

    # @model.setter
    # def model(self, model):
    #     if self.check_model(model):
    #         self.__model = model


car = Car()

car.model = 'Toyota'
print(car)
print(car.__dict__)
