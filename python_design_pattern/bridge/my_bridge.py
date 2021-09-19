class Target:
    def request(self):
        return "this is target request"


class Adaptee:
    def specific_request(self):
        return "this is specific request"


class Adapter_Inheritance(Target, Adaptee):
    def request(self):
        return self.specific_request() + " from target inheritance"


class Adapter_Object(Target):
    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def request(self):
        return self._adaptee.specific_request() + " from target from object"


if __name__ == '__main__':
    target_inheritance = Adapter_Inheritance()
    print(target_inheritance.request())

    target_object = Adapter_Object(Adaptee())
    print(target_object.request())
