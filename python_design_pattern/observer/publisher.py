from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Publisher(ABC):

    @property
    @abstractmethod
    def state(self) -> int:
        pass

    @property
    @abstractmethod
    def observers(self):
        pass

    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class Observer(ABC):

    @abstractmethod
    def subscribe(self, publisher: Publisher) -> None:
        """
        Receive update from subject.
        """
        pass


class ConcreteObserverA(Observer):

    def subscribe(self, publisher: Publisher) -> None:
        if publisher.state < 3:
            print("ConcreteObserverA: React to the event")


class ConcreteObserverB(Observer):

    def subscribe(self, publisher: Publisher) -> None:
        if publisher.state >= 3:
            print("ConcreteObserverB: React to the event")


class ConcretePublisher(Publisher):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None

    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """
    _observers: List[Observer] = []

    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """
    @property
    def state(self) -> int:
        return self._state

    @state.setter
    def state(self, state: int):
        self._state = state

    @property
    def observers(self):
        return self._observers

    @observers.setter
    def observers(self, observers: List[Observer]):
        self.observers = observers

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """
    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """
        for observer in self._observers:
            observer.subscribe(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


if __name__ == '__main__':
    subject = ConcretePublisher()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)
    subject.some_business_logic()
