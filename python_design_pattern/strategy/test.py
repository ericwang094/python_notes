from abc import ABC, abstractmethod


class FlyBehavior:

    @abstractmethod
    def fly(self):
        pass


class QuackBehavior:

    @abstractmethod
    def quack(self):
        pass


class Duck(ABC):

    _fly_behavior: FlyBehavior

    _quack_behavior: QuackBehavior

    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior

    @property
    def fly_behavior(self):
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior):
        self._fly_behavior = fly_behavior

    @property
    def quack_behavior(self):
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior):
        self._quack_behavior = quack_behavior

    def display(self):
        self.fly_behavior.fly()
        self.quack_behavior.quack()


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("fly with wings")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("fly no way")


class QuackLoad(QuackBehavior):
    def quack(self):
        print("quack load")


class QuackNoWay(QuackBehavior):
    def quack(self):
        print("quack no way")


class NormalDuck(Duck):
    pass


class SuperDuck(Duck):
    pass


if __name__ == '__main__':
    print("Normal Duck")
    normal_duck = NormalDuck(FlyWithWings(), QuackLoad())
    normal_duck.display()

    print("Super Duck")
    super_duck = SuperDuck(FlyNoWay(), QuackNoWay())
    super_duck.display()

    print("Promote normal duck")
    normal_duck.fly_behavior = FlyNoWay()
    normal_duck.quack_behavior = QuackNoWay()
    normal_duck.display()
