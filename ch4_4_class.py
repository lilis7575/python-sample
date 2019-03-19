class Hero:
    level = 1
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        
    def level_up(self):
        self.level += 1
        print("<" + self.name, " 의 레벨이 ", str(self.level), "으로 업그레이드 되었음")
        
    def say_hello(self):
        print("내 이름은", self.name, ", 나는", self.__class__.__name__, " 이다.")
        print("현재 레벨은 ", str(self.level), " 이다")

    def attack(self):
        pass

class Knight(Hero):

    def __init__(self, name, gender, country):
        Hero.__init__(self, name, gender)
        self.country = country

    def attack(self):
        print("내 칼을 받아라")

class Wizard(Hero):

    def __init__(self, name, gender, country):
        Hero.__init__(self, name, gender)
        self.country = country

    def attack(self):
        print("내 칼을 받아라")

    def healing(self):
        print("회복되었음")

class Dark(Hero):
    pass


knight_tom = Knight("Tom", "Male", "wonderland")
wizard_jane = Wizard("Jane", "Female", "wolf")
dark_dan = Dark("Dan", "Male")

knight_tom.say_hello()
knight_tom.attack()

wizard_jane.healing()
wizard_jane.attack()
knight_tom.level_up()

dark_dan.level_up()
dark_dan.attack()


