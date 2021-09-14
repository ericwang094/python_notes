from abc import ABC, abstractmethod


class IFlyBehavior:

    @abstractmethod
    def fly(self):
        pass


class IQuackBehavior:

    @abstractmethod
    def quack(self):
        pass


class IDuck:

    _fly_behavior: IFlyBehavior

    _quack_behavior: IQuackBehavior

    def __init__(self, fly_behavior: IFlyBehavior, quack_behavior: IQuackBehavior) -> None:
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior

    @property
    def fly_behavior(self):
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior: IFlyBehavior):
        self._fly_behavior = fly_behavior

    @property
    def quack_behavior(self):
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior):
        self._quack_behavior = quack_behavior

    def display(self):
        self._fly_behavior.fly()
        self._quack_behavior.quack()


class FlyWithWings(IFlyBehavior):
    def fly(self):
        print("fly with wings")


class FlyNoWay(IFlyBehavior):
    def fly(self):
        print("Fly no way")


class QuackLoad(IQuackBehavior):
    def quack(self):
        print("quack load")


class QuackNoWay(IQuackBehavior):
    def quack(self):
        print("quack no way")


class NormalDuck(IDuck):
    pass


class SpecialDuck(IDuck):
    pass


if __name__ == '__main__':

    normal_duck = NormalDuck(FlyWithWings(), QuackLoad())
    normal_duck.display()

    special_duck = NormalDuck(FlyNoWay(), QuackNoWay())
    special_duck.display()

    # promote normal duck to be special
    normal_duck.fly_behavior = FlyNoWay()
    normal_duck.quack_behavior = QuackNoWay()
    normal_duck.display()