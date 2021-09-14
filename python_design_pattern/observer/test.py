from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):

    @property
    @abstractmethod
    def state(self):
        pass

    @property
    @abstractmethod
    def subscribers(self):
        pass

    @abstractmethod
    def attach(self, subscriber: Subscriber):
        pass

    @abstractmethod
    def detach(self, subscriber: Subscriber):

