from threading import Thread, Lock
from abc import ABC


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

    _value: str

    def __init__(self, value: str):
        self._value = value


def test_instance(value: str):

    instance = Singleton(value)
    print(instance._value)


if __name__ == '__main__':
    instance1 = Thread(target=test_instance, args=("FOO",))
    instance2 = Thread(target=test_instance, args=("BAR",))

    instance1.start()
    instance2.start()