from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def oven(self):
        pass


class CheesePizza(Pizza):

    def prepare(self):
        print("prepare cheese pizza")

    def oven(self):
        print("cook cheese pizza")


class VeggiePizza(Pizza):

    def prepare(self):
        print("prepare veggie pizza")

    def oven(self):
        print("cook veggie pizza")


class MeatLover(Pizza):

    def prepare(self):
        print("prepare meat lover pizza")

    def oven(self):
        print("cook meat lover pizza")


class SimplePizzaFactory:
    def createPizza(self, pizza_type: str):
        pizza: Pizza = None

        if pizza_type == "cheese":
            pizza = CheesePizza()
        elif pizza_type == "veggie":
            pizza = VeggiePizza()
        elif pizza_type == "meat_lover":
            pizza = MeatLover()

        return pizza


class PizzaStore:
    _simple_pizza_factory: SimplePizzaFactory

    def __init__(self, simple_pizza_factory: SimplePizzaFactory):
        self._simple_pizza_factory = simple_pizza_factory

    def order_pizza(self, pizza_type: str):
        pizza: Pizza = self._simple_pizza_factory.createPizza(pizza_type)
        pizza.prepare()
        pizza.oven()


if __name__ == '__main__':
    pizza_store: PizzaStore = PizzaStore(SimplePizzaFactory())
    pizza_store.order_pizza("meat_lover")
    pizza_store.order_pizza("cheese")
    pizza_store.order_pizza("veggie")
