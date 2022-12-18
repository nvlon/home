class Ein:
    def __init__(self,name):
        self.name=name
class Zwei:
    def __init__(self,age):
        self.age=age
class Drei(Ein):
    def frasa1 (self):
        print(f'сабр это больше чем терпение')

class Vier(Zwei):
    def frasa2 (self):
        print(f'сабр это смирение с волей Аллаха в какой бы ситуации ты не оказался')


class Funf(Drei,Vier):
    def __init__(self,name,age):
        Drei.__init__(self,name)
        Vier.__init__(self,age)






n=Funf('name',7)
n.frasa1()
n.frasa2()
print(n)