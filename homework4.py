class Ein:
    def __init__(self,name):
        self.name=name
class Zwei:
    def __init__(self,age):
        self.age=age
class Drei:
    def f (self,frasa1):
        self.f(frasa1)
        print('Амир говорит')

class Vier:
    def f (self,frasa2):
        self.f(frasa2)
        print('Амир молчит')


class Funf(Drei,Vier):
    def __init__(self , name,age):
        super().__init__(name, age)
        Ein.__init__( name,age)




n=Funf('name',33)
print(n)
