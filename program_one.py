def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

        >>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)

# #python string
# print("Auntor");

# #python number
# print("AJ Auntor \n 014008800XX");
