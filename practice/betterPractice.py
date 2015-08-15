
# Better
class Boiler:
    def safety_check(self):
        if any([self.temperature > MAX_TEMPERATURE,
                self.pressure > MAX_PRESSURE]):
            if not self.shutdown():
                self.alarm()

    def alarm(self):
        with open(BUZZER_MP3_FILE) as f:
            play_sound(f.read())

    @property
    def pressure(self):
        pressure_psi = abb_f100.register / F100_FACTOR
        return psi_to_pascal(pressure_psi)
    ...


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @classmethod
    def polar(cls, r, theta):
        return cls(r * cos(theta),
                   r * sin(theta))

point = Point.polar(r=13, theta=22.6)


class TaskSender:
    def __init__(self, task, job, obligation):
        self.task = task
        self.job = job
        self.obligation = obligation
        self.processed = []
        self.copied = []
        self.executed = []

    def __call__(self):
        self.prepare()
        self.process()
        self.execute()
    ...

if self.flags & 0b1000:  # Am I visible?
    ...

# Better
...
@property
def is_visible(self):
    return self.flags & 0b1000

if self.is_visible:
    ...


# Bad
if type(entry) is Film:
    responsible = entry.producer
else:
    responsible = entry.author

# Shouldn't use type() or isinstance() in conditional --> smelly

# Better
class Film:
    ...
    @property
    def responsible(self):
        return self.producer

entry.responsible



if type(entry) == Film:
    responsible = entry.producer
else:
    responsible = entry.author

#Better

class Film(self):


    @property
    def responsible(self):
        return self.producer

entry.responsible



class ParagraphEditor:
    ...
    def highlight(self, rectangle):
        self.reverse(rectangle)

# Better
class ParagraphEditor:
    ...
    highlight = reverse  # More readable, more composable



_DEFAULT_PORT = 1234

class SomeProtocol:
    ...
    def __enter__(self):
        self._client = socket()
        self._client.connect(
            (self.host,
            self.port or _DEFAULT_PORT)
        )
        return self

# If you want to subclass SomeProtocol, you would have to overwrite every method!

# Better
class SomeProtocol:
    _default_port = 1234
    ...
    def __enter__(self):
        self._client = socket()
        self._client.connect(
            (self.host,
            self.port or self._default_port))




class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

# Sometimes need more flexibility --> use properties

class Point:
    def __init__(self, x, y):
        self._x, self._y = x, y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

# Bad
# Can't change type of collection
#     e.g. can't change employees from a list to a set  -->> Set????????????????
class Department:
    def __init__(self, *employees):
        self.employees = employees

for employee in department.employees:
    ...

# Better
class Department:
    def __init__(self, *employees):
        self._employees = employees

    def __iter__(self):
        return iter(self._employees)

for employee in department:  # More readable, more composable
    ...




# Meh
class Rectangle:
    def bottom_right(self):
        return Point(self.left + self.width,
                    self.top + self.height)

# Better to use temporary variables for readability
class Rectangle:
    ...
    def bottom_right(self):
        right = self.left + self.width
        bottom = self.top + self.height
        return Point(right, bottom)


#Can often use sets instead of combination of for loops

item in a_set
item not in a_set

# a_set <= other
a_set.is_subset(other)

# a_set | other
a_set.union(other)

# a_set & other
a_set.intersection(other)

# a_set - other
a_set.difference(other)


#EQ


obj == obj2
obj1 is obj2

class Book:
    ...
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.author == other.author and
                self.title == other.title)






