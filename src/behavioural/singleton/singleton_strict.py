from threading import Lock, Thread


class SingletonMeta(type):

    _instances = {}

    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    process_one = Thread(target=test_singleton, args=("One",))
    process_two = Thread(target=test_singleton, args=("Two",))
    process_one.start()  # 'One'
    process_two.start()  # 'One'
