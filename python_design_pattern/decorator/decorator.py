class Component:
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """
    def operation(self):
        pass


class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """
    def operation(self):
        return "Concrete component"


class Decorator(Component):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    _component: Component = None

    def __init__(self, component: Component):
        self._component = component

    @property
    def component(self):
        """
        The Decorator delegates all work to the wrapped component.
        """
        return self._component

    @component.setter
    def component(self, component):
        self._component = component


class ConcreteDecoratorA(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """
    def operation(self):
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """
        return f"Concrete DecoratorA {self.component.operation()}"


class ConcreteDecoratorB(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """

    def operation(self):
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """
        return f"Concrete DecoratorB {self.component.operation()}"


def client_code(component: Component):
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """
    print(f"Result: {component.operation()}", end="")


if __name__ == '__main__':
    simple = ConcreteComponent()
    print("client: I've got a simple component")
    client_code(simple)
    print("\n")

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)