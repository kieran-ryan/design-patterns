from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self):
        self.operation_one()
        self.operation_two()

    @abstractmethod
    def operation_one(self):
        pass

    @abstractmethod
    def operation_two(self):
        pass


class ConcreteClass(AbstractClass):
    def operation_one(self):
        print("First operation")

    def operation_two(self):
        print("Second operation")


if __name__ == "__main__":
    concrete = ConcreteClass()
    concrete.template_method()
    # 'First operation'
    # 'Second operation'
