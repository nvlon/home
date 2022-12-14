class bank:

    def __init__(self, name,balanse):
        self._name=name
        self._balanse=balanse
    def __str__(self):
        return f'{self.name}'\
               f'{self.balanse}'



    def moneyX(self):
        self._balanse += int(input('Введите сумму:'))


    def _kill(self):
        self._balanse = 0


    def __jackpot(self):
        return (self._balanse *10)


    def _summa(self,other):
        return (self._balanse + other.balanse())


    def _qqqq(self,other):
        self._balanse += other._balanse
        other._balanse = 0

a=bank('nvlon' , 770)
b=bank('svlon', 450)
a.moneyX()
a._kill()
a._bank__jackpot()
a._summa()
a._qqqq()
print(a._balanse)
print(b._balanse)





class calculator:
    def __init__(self, number):
        self.number=number
    def __add__(self, other):
        return self.number + other.number
    def __sub__(self, other):
        return self.number - other.number
    def __mul__(self, other):
        return self.number * other.number
    def __truediv__(self, other):
        return self.number / other.number

q=calculator(81)
w=calculator(9)
r=q+w
p=q-w
l=q*w
wq=q/w
print(r,p,l,wq)