class Robot:
    brain= True
    def __init__(self, name,model,color,destination):
        self.name=name
        self.model=model
        self.color=color
        self.destination=destination
    def __str__(self):
        return f'name is {self.name} \n'\
               f'color is {self.color} \n'\
               f'model is {self.model}'
    def desti(self):
        print(self.desti())
robot = Robot ('Vlad', 'a4', 'blue', 'snimat video')
print(robot)
print(robot.desti())

#дочерний класс
class Robot2(Robot):
    def __init__(self , name, model, color, destination,fly):
        super().__init__(name, model, color, destination)
        Robot.__init__(self, name, model, color, destination)
        self.fly=fly
robot2=Robot2('termonator', 'T1001', 'pink' , 'otbiraet odejdu')
print(robot2.fly)

robot.desti()
robot2.desti()
print(robot2.brain,robot.brain)

class Robot3(Robot2):
    def desti(self):
        print(f'{self} теперь летает' )

MegaTron=Robot3('TRANSformer', 'Desipticon', 'RED', 'WARS', False)
MegaTron.desti()

class Human:
    #атрибуты уровня класса
    head=1
    body=1
    #метод конструктор
    def __init__(self, name ,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'name is {self.name}\n'\
               f'age is {self.age}\n'\
               f'head id {self.head}'
hum = Human ('nvlon', 18)

Robot3.desti(hum.name)