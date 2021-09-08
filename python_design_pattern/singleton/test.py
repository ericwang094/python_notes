from threading import Lock, Thread


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


def test_singleton(value: str) -> None:
    instance = Singleton(value)
    print(instance.value)


if __name__ == "__main__":
    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
