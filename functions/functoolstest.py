

from functools import partial, wraps

basetwo = partial(int, base=2)
basetwo.__doc__ = "test"
print basetwo('0010')
print int('0010', base=2)

print('-'*30)

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('calling decorated func')
        f(*args, **kwargs)
        return

    return wrapper

@my_decorator
def example():
    """
    This is an example func()
    """
    print 'called example func()'


example()
print example.__name__
print example.__doc__




