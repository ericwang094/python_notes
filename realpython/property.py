# https://realpython.com/python-property/
from functools import cache
from time import sleep


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def _get_radius(self):
        print("get radius")
        return self._radius

    def _set_radius(self, value):
        print("set radius")
        self._radius = value

    def _del_radius(self):
        print("delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc='The radius property'
    )
circle = Circle(40.3)
print(circle.radius)
circle.radius = 23.1
print(circle.radius)

class Circle_2:
    def __init__(self, radius, readonly_prop):
        self._radius = radius
        self._readonly_prop = readonly_prop
    @property
    def radius(self):
        print("get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("delete radius")
        del self._radius

    @property
    def readonly_prop(self):
        return self._readonly_prop

circle = Circle_2(40.3, "abc")
print(circle.radius)
circle.radius = 23.1
print(circle.radius)

# circle.readonly_prop = "cdsp"   # throw error AttributeError: can't set attribute 'readonly_prop'

### Property with cache
class MyCircle:
    def __init__(self, radius):
        self._radius = radius

    @property
    @cache
    def diameter(self):
        sleep(0.5)
        return self._radius * 2

circle_3 = MyCircle(10)
print(circle_3.diameter)
print(circle_3.diameter)

### Property with subclass
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

class Employee(Person):
    @property
    def name(self):
        return super().name.upper()

person = Person("John")
print(person.name)

employee = Employee("john in employee")
print(employee.name)