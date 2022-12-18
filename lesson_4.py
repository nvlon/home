class Nurel:
    head=1
    hands=2
    foots=2
    def __init__(self, name='Nurel',age=18):
        self.__name=name
        self.__age=age

    def __str__(self):
        return f'{self.__name}'\
               f'{self.__age}'

    def get_nurel(self):
        return f'{self.__name} {self.__age}'


    def set_nurel(self, name,age): #set-переопределяет
        self.__name=name
        self.__age=age


    @property
    def azaliya(self):
        return f'{self.__name} {self.__age}'
    @azaliya.setter
    def azaliya(self,name,age):
        self.__name=name
        self.__age=age


bayel=Nurel('azaliya', 4)
print(bayel.azaliya)

# bayel.set_nurel('Amir', 12)
# print(bayel.get_nurel())



#множественное наследование
class One :
    def __init__(self, name):
        self.name=name

class tho(One):
    def f(self):
        print('эта функция tho')
class tho2(One):
    def f(self):
        print('амир молчит')
class Tho(One):
    def f(self):
        print('амир говорит')

class Three (Tho,tho2):

# print(Three.mro())


class Name:
    def __init__(self, name):
        self.name = name


class Age:
    def __init__(self, age):
        self.age = age


class Beer(Name):
    def beer(self):
        print(f'{self.name} is drinking beer')


class Born(Age):
    def year(self):
        print(f'He was born in {2022 - self.age}')


class Both(Beer, Born):
    def __init__(self, name, age):
        Beer.__init__(self, name)
        Born.__init__(self, age)


test = Both('Loic', 20)
test.beer()
test.year()




