from abc import ABC, abstractmethod

class People(ABC):

    def __init__(self):
        print('init people class')

    @abstractmethod
    def get_name(self):
        pass

class Man(People):

    name = None

    gender = None

    def __init__(self, name):
        self.name = name
        self.gender = 'man'
        print('init man class')
        super().__init__()

    def __getattr__(self, item):
        return 'prefix_'+item

    def __getattribute__(self, item):
        return super().__getattribute__(item)

    @staticmethod
    def static_method():
        print('Man have a static method')

    @classmethod
    def class_method(cls):
        print('This is a class method of', cls)

    def get_name(self):
        return self.name

max = Man('max')
print('My name is {}, I\'m a {}'.format(max.name, max.gender))
print('Man is a subclass of People :{}'.format(issubclass(Man, People)))
print('What\'s Man base class :{}'.format(Man.__base__))
print('max is instance of Men :{}'.format(isinstance(max, Man)))
print('max is instance of People :{}'.format(isinstance(max, People)))
print('max\'s class is :{}'.format(max.__class__))
print('max\'s type is :{}'.format(type(max)))
print('max has attribute name :{}'.format(hasattr(max, 'name')))

Man.static_method()
Man.class_method()
print('get max\'s name :{}'.format(max.name))
print('get max\'s ages :{}'.format(max.ages))
print(max.__dict__)
