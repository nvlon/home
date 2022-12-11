class SuperHero:
    people='people'
    def __int__(self, name, nickname, superpower, health_points, catchphrase):
        self.name =name
        self.nickname =nickname
        self.superpower =superpower
        self.health_points= health_points
        self.catchphrase =catchphrase

    def nameHero(self):
        print(f'Heros name ist {self.name}')
    def hp(self):
        self.health_points *=2
    def __str__(self):
        return (f'ihr nickname {self.nickname}'
                f'\nseine Macht ist {self.superpower}'
                f'\nihr health_ist {self.health_points}'
                f'\nihr catchphrase ist {self.catchphrase}')
    def desti(self):
        print(self.desti())
    def __len__(self):
        return len (self.catchphrase)

hero = SuperHero('Hinata', 'Seyo', 'abheben', 2, 'Pass den Ball zu mir!')
hero.nameHero()
hero.hp()
print(hero)
print(SuperHero.desti())
print(len(hero))

# наследованный класс 1
class SuperHero1(SuperHero):
    kraft=1
    sprung=1
    def __init__(self,name, nickname, superpower, health_points, catchphrase,fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        SuperHero.__init__(self,name, nickname, superpower, health_points, catchphrase)
        self.fly=fly

    def SuperHero1(damage='damage', fly='fly'):
        print(f'damage: {damage.title(False)}, fly: {fly.title()}')


hero1=SuperHero('волейбол','поле', 'мяч','6','сетка',False)
def frasa(self):
    print(f'{self.name} is fly in the True_phrase')
def den_x():
    print(den_x())

def crit(hp):

    print(hp, '^2', hp ** 2)



print(hero.fly)



# наследованный класс 2
class SuperHero2(SuperHero1):
    punkt=1
    form=True
    SuperHero=None
    def desti(self,SuperHero=1):
        print(f'{SuperHero} is fly ')

hero2=SuperHero2('касание','шансбол','аут','пас', False)
hero2.desti()

class villiam:
    people='monster'

    print(crit)
