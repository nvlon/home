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

#
#     def set_nurel(self, name,age):
#         self.__name=name
#         self.__age=age
#
#
#     @property
#     def azaliya(self):
#         return f'{self.__name} {self.__age}'
#     @azaliya.setter
#     def azaliya(self,name,age):
#         self.__name=name
#         self.__age=age
#
#
# bayel=Nurel('azaliya', 4)
# print(bayel.azaliya)

# bayel.set_nurel('Amir', 12)
# print(bayel.get_nurel())



#множественное наследование

class O:...

class A(O):...
class B(O):...
class C(O):...
class D(O):...
class E(O):...


class K1(A,B,C):...
class K2(B,D):...
class K3(C,D,E):...

class Z(K1,K2,K3):...
# print(Z.mro())








# неправильное множественное наследование ,потому что здесь 2 конструктора
class One :
    def __init__(self, name):
        self.name=name

class Tho():
    def __init__(self,age):
        self.age=age
    def f(self):
        print('Амир молчит')
class Tho2(One):
    def f(self):
        print('Амир говорит')

    def tho2(self):
        print('эта функция Tho2')

class Three(Tho ,Tho2):
    def __init__(self,name, age):
        Tho.__init__(self,age)
        Tho2.__init__(self,name)
    def __str__(self):
        return f'{self.name} {self.age}'

c=Three('name',99)
print(c)



