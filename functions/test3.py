


class P:

    def __init__(self,x):
        self.setX(x)

    def getX(self):
        print('get X1')
        return self.__x

    def setX(self, x):
        print('set X1')
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


p = P(1001)
print(p.getX())

print('-'*20)

class P2(object):

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        print('get x2')
        return self.__x

    @x.setter
    def x(self, x):
        print('set x2')
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


p2 = P2(1001)
print(p2.x)

print('-'*20)

class P3:

    def __init__(self,x):
        self.setX(x)

    def getX(self):
        print('get x3')
        return self.__x

    def setX(self, x):
        print('set x3')
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(getX, setX)


p3 = P3(1001)
print(p3.x)

print('^'*30)

class Robot:

    def __init__(self, name, build_year, lk = 0.5, lp = 0.5 ):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"

if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4 )
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)