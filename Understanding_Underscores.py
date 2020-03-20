def _internal1(self):
    return "Internal1"


class A:
    def __init__(self):
        self.a = 10
        self._b = 20
        self.__c = 30

    def _internal(self):
        return "Internal"

    def external(self):
        return "External "

    # class = 10 # this will give error, as keyword class is already taken
    # class_ = 10 # this will not give error, as keyword is appended with _ to make it a normal name and can be used.

class B(A):
    def __init__(self):
        super().__init__()
        self.a = 100
        self._b = 200
        self.__c = 300

    def checkDunder(self):
        return self.__c


if __name__ == "__main__":
    obj1 = A()
    obj2 = B()
    print(dir(obj2))
    # pri nt(obj2.a)
    print(obj2._b)
    print(obj2._B__c)
    print(obj2._A__c)
    print(obj2.checkDunder()) # This will not give error but obj2.__c will give.
    
    print(obj1.a)
    print(obj1._b)
    print(obj1._internal())
    print(obj1.external())