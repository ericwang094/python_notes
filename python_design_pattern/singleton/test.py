from abc import ABC, abstractmethod
from typing import List
from threading import Thread, Lock

class SingletonMeta(type):

    _instance = {}

    _lock = Lock()

    def __call__(cls, *args, **kwargs):

        with cls._lock:
            if cls not in cls._instance:
                instance = super().__call__(*args, **kwargs)
                cls._instance[cls] = instance

        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):

    value: str = None

    def __init__(self, value: str):
        self.value = value



def test_singleton(value: str):

    instance = Singleton(value)
    print(instance.value)


if __name__ == '__main__':
    instance1 = Thread(target=test_singleton, args=("FOO",))
    instance2 = Thread(target=test_singleton, args=("BAR",))
    instance1.start()
    instance2.start()