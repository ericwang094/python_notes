from abc import ABC, abstractmethod


class FlyBehavior(ABC):

    @abstractmethod
    def fly(self):
        pass


class QuackBehavior(ABC):

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

    @property
    def quack_behavior(self):
        return self._quack_behavior

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior: FlyBehavior):
        self._fly_behavior = fly_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior: QuackBehavior):
        self._quack_behavior = quack_behavior

    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()


class FlyWithWings(FlyBehavior):

    def fly(self):
        print("fly with wings")


class FlyNoWay(FlyBehavior):

    def fly(self):
        print("fly no way")


class QuackLoad(QuackBehavior):

    def quack(self):
        print("Quack load")


class QuackNoWay(QuackBehavior):

    def quack(self):
        print("Quack no way")


class NormalDuck(Duck):
    pass


class SuperDuck(Duck):
    pass


if __name__ == "__main__":
    print("normal duck with normal ability")
    normal_duck = NormalDuck(FlyWithWings(), QuackLoad())
    normal_duck.perform_fly()
    normal_duck.perform_quack()

    # promote normal duck
    print("normal duck with no ability")
    normal_duck.fly_behavior = FlyNoWay()
    normal_duck.quack_behavior = QuackNoWay()
    normal_duck.perform_fly()
    normal_duck.perform_quack()

    print("super duck with super ability")
    super_duck = SuperDuck(FlyNoWay(), QuackNoWay())
    super_duck.perform_fly()
    super_duck.perform_quack()
