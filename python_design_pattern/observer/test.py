from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Publisher:

    _state: int

    _subscriber: List

    def __init__(self):
        self._subscriber = []

    def attach(self, subscriber: Subscriber):
        self._subscriber.append(subscriber)

    def detach(self, subscriber: Subscriber):
        self._subscriber.remove(subscriber)

    def notify(self):
        for subs in self._subscriber:
            subs.execute()


class Subscriber(ABC):

    _publisher: Publisher

    def subscribe(self):
        self._publisher.attach(self)

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        self._publisher = publisher

    @abstractmethod
    def execute(self):
        pass


class ConcreteSubscriber1(Subscriber):
    def execute(self):
        print("concrete subscriber1 subscribed")


class ConcreteSubscriber2(Subscriber):
    def execute(self):
        print("concrete subscriber2 subscribed")


if __name__ == '__main__':
    publisher = Publisher()
    concreteSub1 = ConcreteSubscriber1()
    concreteSub2 = ConcreteSubscriber2()

    publisher.attach(concreteSub1)
    # publisher.notify()
    #
    publisher.attach(concreteSub2)
    # publisher.notify()

    publisher.detach(concreteSub1)
    publisher.notify()