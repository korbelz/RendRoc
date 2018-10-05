#comment section
#RendGeo written by Korbelz
#currnet scope: Direction finder
import math

x_one = input("what is current x? no decimals please: ")
x_one = int(x_one)

y_one = input("what is current y? no decimals please: ")
y_one = int(y_one)

x_two = input("what is the x you need to go to? no decimals please: ")
x_two = int(x_two)

y_two = input("what is the y you need to go to? no decimals please: ")
y_two = int(y_two)

rad = math.atan2 ((y_two - y_one),(x_two - x_one))
#print (rad)

bearing = 90 - (180/3.14) * rad
#print (bearing)

Con_bearing = ((bearing) + 180)
print ("Conclave tree is at 180 deg")
print ("A number less than the tree is left, more then the tree is right")
print (f'{Con_bearing} is the bearing you need to walk')


Rev_bearing = ((bearing) + 315)
print ("Rev tree is at 315 deg")
print ("A number less than the tree is left, more then the tree is right")
print (f'{Rev_bearing} is the bearing you need to walk')


Order_bearing = ((bearing) + 45)
print ("Order tree is at 45 deg")
print ("A number less than the tree is left, more then the tree is right")
print (f'{Order_bearing} is the bearing you need to walk')


input('Press ENTER to exit')