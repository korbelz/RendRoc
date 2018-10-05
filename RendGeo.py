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

bearing = math.degrees(rad)
#print (bearing)

compass =  360 % bearing
if bearing < 0:
    bearing = 360 + bearing

print (f'Outbound from tree bearing {bearing}')


print ("Conclave tree is outbound at 102 deg")
print ("A number less than the tree is left, more then the tree is right")


print ("Rev tree is at outbound 344 deg")
print ("A number less than the tree is left, more then the tree is right")


print ("Order tree is at outbound 226 deg")
print ("A number less than the tree is left, more then the tree is right")



input('Press ENTER to exit')