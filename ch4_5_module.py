from random import randint
from math import pi
from ch4_4_class import Wizard, Knight

for i in range(10):
    a = randint(i, 10)
    print(a)

print(pi)

tom = Wizard("TOM", "Male", "korea")

tom.say_hello()
tom.level_up()
tom.level_up()
tom.level_up()