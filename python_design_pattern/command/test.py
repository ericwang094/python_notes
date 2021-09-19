from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class SimpleCommand(Command):

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"Simple command: see, I can do simple things like printing"
              f"({self._payload}")


class ComplexCommand(Command):

    def __init__(self, receiver: Receiver, a: str, b: str):
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        self._receiver.do_something(self._a)
        self._receiver.do_something(self._b)


class Receiver:
    def do_something(self, a: str):
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str):
        print(f"\nReceiver: Also working on ({b}.)", end="")

class Invoker:

    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_finish