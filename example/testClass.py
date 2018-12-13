class People:

    def init(self):
        print("I'm a people!")

class Man(People):

    def get_gender(self):
        return 'man'

max = Man()
max.init()
print(max.get_gender())

print(issubclass(Man, People))
print(Man.__base__)

print(isinstance(max, Man))
print(isinstance(max, People))
print(max.__class__)
print(type(max))
print(hasattr(max, 'get_gender'))
