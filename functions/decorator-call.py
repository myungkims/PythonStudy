from functools import wraps

class EnterExitParam(object):
    def __init__(self, p1):
        self.p1 = p1

    def __call__(self, f):
        @wraps(f)
        def new_f():
            print("Entering", f.__name__)
            print("p1=", self.p1)
            f()
            print("Leaving", f.__name__)
        return new_f


@EnterExitParam("foo bar")
def hello():
    """
    hello function
    """
    print("Hello")


if __name__ == "__main__":
    hello()
    print hello.__name__
    print hello.__doc__

    a = 1
    b = 1
    if a is b:
        print 'same id'
    else:
        print 'not same id'

    if a is a:
        print 'same id'
    else:
        print 'not same id'

    if a == b:
        print 'same value'
    else:
        print 'not same value'

    # is : check whether it points same obj or not
    print 'a id==>{}',id(a)
    print 'b id ==>{}',id(b)



#cascading

# Instead of this
self.release_water()
self.shutdown()
self.alarm()

class Reactor:
    ...
    def release_water(self):
        self.valve.open()
        return self

self.release_water().shutdown().alarm()




# Meh
def match(self, items):
    for each in items:
        if each.match(self):
            return each
# Is this supposed to reach the end? Is this a bug?

# Better
def match(self, items):
    for each in items:
        if each.match(self):
            return each
    return None

#Explicit better than implicit
#Include return value if it's interesting (even if it's None)





