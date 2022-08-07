class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    ...


if __name__ == "__main__":
    singleton_one = Singleton()
    singleton_two = Singleton()
    is_same_instance = id(singleton_one) == id(singleton_two)
    print(is_same_instance)  # True
