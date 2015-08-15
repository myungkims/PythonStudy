import re

print('-'*30)
print('X'*10 + '  recursive  ' + 'X'*10)
print('-'*30)

L = [1, 2, 3]

iterator = iter(L)
a, b, c = iterator
print(a)

print(iterator)

print('-'*10)

def mygen(N):
    yield N**2
    yield N**3

def getSet(N, dist):
    if dist == 0:
        return [N]

    numbers = []
    for n in getSet(N, dist-1):
        #print('==>{}'.format(n) )
        listA = list(mygen(n))
        #print(('*{}'.format(listA)))
        numbers += listA
        #print('@->{}'.format(numbers))

    print('@@->{}'.format(numbers))
    return numbers

print(getSet(2, 0))
print(getSet(2, 1))
print(getSet(2, 2))
print('+'*20)
for item in getSet(2, 3):
    print item

print('-'*30)
print('X'*10 + '  type  ' + 'X'*10)
print('-'*30)

print('-'*30)

foo = [42, 'hurz', lambda x: x**2, [47, '11']]

print(foo)

print(foo[0])
print(foo[3][0])
print(foo[2](2))
foo[3][0] = 99
print(foo)

for i in foo:
    print('{} ==> {}'.format(i, type(i)))

print('-'*30)
print('X'*10 + '  closure  ' + 'X'*10)
print('-'*30)


def multiplier_of(n):
    def multiplier(x):
        return n * x

    return multiplier

times3 = multiplier_of(3)
time5 = multiplier_of(5)

print(times3(3))
print(time5(5))

# print(multiplier_of().__closure__)
# times3.__closure__[0].cell_contents   # print nothing ?????


print('-'*30)
print('X'*10 + '  decorator  ' + 'X'*10)
print('-'*30)

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner

@make_pretty
def ordinary():
    print('I am ordinary')


ordinary()
# pretty = make_pretty(ordinary)
# pretty()

print('-'*10)

def smart_divider(func):
    # def inner(a, b):
    def inner(*args, **kwargs):
        print('check params')
        if b == 0:  # add get second param from *args or *kwargs
            print('divide by 0')
            return
        # return func(a, b)
        # func(a, b)
        return func(*args, **kwargs)
    print('before return inner')
    return inner

# @smart_divider
def divide(a, b):
    return a / b

divide = smart_divider(divide)
print(divide(2, 1))

print('-'*10)

def star(func):
    def inner(*args, **kwargs):
        # print('*'*len(msg))
        print('*' * 30)
        func(*args, **kwargs)
        print('*' * 30)

    return inner

def percent(func):
    def inner(*args, **kwargs):
        # print('*'*len(msg))
        print('%' * 30)
        func(*args, **kwargs)
        print('%' * 30)

    return inner

# @star
# @percent
def printer(msg):
    print(msg)

printer = star(percent(printer))

printer('Hello World')

print('-'*30)
print('X'*10 + '  property  ' + 'X'*10)
print('-'*30)


class Celsius(object):
    def __init__(self, temp=0):
        self.temperature = temp
        # self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    def get_temperature(self):
        print('getting value')
        return self._temperature

    def set_temperature(self, value):
        print('setting value')
        if value < -273:
            print('Error')
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)

c = Celsius()
print(c.temperature)

c.temperature = 300
print(c.temperature)

print('--- Cesius2 ------')

class Celsius2(object):
    def __init__(self, temp=0):
        self.temperature = temp
        # self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print('getting value')
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print('setting value')
        if value < -273:
            print('Error')
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

    # temperature = property(get_temperature, set_temperature)

c2 = Celsius2()
print(c2.temperature)

c2.temperature = 300
print(c2.temperature)



