from abc import ABC, abstractmethod


"""
In Startbuzz, there are 2 basic beverage with a lot extra choice
"""
class Beverage(ABC):
    _description: str = "Unknown Beverage"

    @property
    def description(self):
        return self._description

    @abstractmethod
    def cost(self) -> float:
        pass


class CondimentDecorator(Beverage):
    _beverage: Beverage
    
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
        
    @property
    def beverage(self):
        return self._beverage
    
    @beverage.setter
    def beverage(self, beverage):
        self._beverage = beverage

    @abstractmethod
    def get_description(self):
        pass


class Espresso(Beverage):
    def __init__(self):
        self._description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        self._description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89


class Mocha(CondimentDecorator):

    def get_description(self):
        return self._beverage.description + ", Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.2


class Whip(CondimentDecorator):

    def get_description(self):
        return self._beverage.description + ", Whip"

    def cost(self) -> float:
        return self._beverage.cost() + 0.3


if __name__ == '__main__':
    espresso = Espresso()
    print("Cost of " + espresso.description + " and cost: " + str(espresso.cost()))

    mocha = Mocha(espresso)
    print("Cost of " + mocha.get_description() + " and cost: " + str(mocha.cost()))


    whip = Whip(mocha)
    print("Cost of " + whip.get_description()
          + " and cost: " + str(whip.cost()))
    # print("a")