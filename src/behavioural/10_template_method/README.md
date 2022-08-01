```mermaid
  classDiagram
    AbstractClass <|-- ConcreteClass
    AbstractClass: +template_method()
    AbstractClass: +operation_one()
    AbstractClass: +operation_two()
    class ConcreteClass{
      +operation_one()
      +operation_two()
    }
```

`operation_one` and `operation_two` are abstract methods of `AbstractClass` which are implemented by a `ConcreteClass` and called by the `template_method`.
