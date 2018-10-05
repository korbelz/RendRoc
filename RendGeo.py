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

print (f'start location to end location bearing is {bearing}')


print ("Conclave base to tree centerline is at 102 deg")
print ("A number less than the centerline is left, more then the centerline is right")


print ("Rev base to tree centerline is at 344 deg")
print ("A number less than the centerline is left, more then the centerline is right")


print ("Order base to tree centerline is at 226 deg")
print ("A number less than the centerline is left, more then the centerline is right")



input('Press ENTER to exit')