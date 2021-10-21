from abc import ABC, abstractmethod


class Beverage(ABC):
    _description: str

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class Latte(Beverage):

    def __init__(self):
        self._description = "Latte"

    def get_description(self):
        return "This is Latte"

    def cost(self):
        return 5


class Topping(Beverage, ABC):

    _beverage: Beverage

    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @property
    def beverage(self):
        return self._beverage

    @beverage.setter
    def beverage(self, beverage):
        self._beverage = beverage


class Cream(Topping):

    def get_description(self):
        return self.beverage.get_description() + " with cream and cost " + str(self.cost())

    def cost(self):
        return self.beverage.cost() + 0.5


class Sugar(Topping):
    _cost: float = 0.2

    def get_description(self):
        return self.beverage.get_description() + " with sugar and cost " + str(self.cost())

    def cost(self):
        return self.beverage.cost() + 0.2

if __name__ == '__main__':
    latte = Latte()
    print(latte.get_description())

    latte_cream = Cream(latte)
    print(latte_cream.get_description())

    latte_cream_sugar = Sugar(latte_cream)
    print(latte_cream_sugar.get_description())




