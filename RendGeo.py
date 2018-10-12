#comment section
#RendGeo written by Korbelz
#current scope: Direction finder
import math

i_loop = 0

x_tree = 0

y_tree = 0

x_two = input("what is the x you need to go to? no decimals please: ")
x_two = int(x_two)

y_two = input("what is the y you need to go to? no decimals please: ")
y_two = int(y_two)

def tree(x_tree , y_tree , x_one , y_one):
    rad_tree = math.atan2 ((y_tree - y_one),(x_tree - x_one))
    #print (rad)
    bearing_tree = int(math.degrees(rad_tree))
    #print (bearing)
    #compass =  360 % bearing
    if bearing_tree < 0:
        bearing_tree = 360 + bearing_tree
    print (f'current location to tree is bearing {bearing_tree}')
    return bearing_tree

def target(x_two , y_two , x_one , y_one):
    rad_target = math.atan2 ((y_two - y_one),(x_two - x_one))
    #print (rad)
    bearing_target = int(math.degrees(rad_target))
    #print (bearing)
    #compass =  360 % bearing
    if bearing_target < 0:
        bearing_target = 360 + bearing_target
    print (f'current location to target is bearing {bearing_target}')
    return bearing_target

while i_loop < 5:
    x_one = input("what is current x? no decimals please: ")
    x_one = int(x_one)
    y_one = input("what is current y? no decimals please: ")
    y_one = int(y_one)
    heading_tree = tree(x_tree , y_tree , x_one , y_one)
    heading_target = target(x_two , y_two , x_one , y_one)
    #direction = heading_target - heading_tree
    #print (f' degrees offset {direction}')
    #if direction < 0: 
    #    left_dir = abs(direction)
    #    print (f'turn {left_dir} degrees left from the tree to head toward target')
    #else:
    #    print (f'turn {direction} degress right from the tree to head towards target')
    i_loop += 1

#print ("Conclave base to tree centerline is at 102 deg")

#print ("Rev base to tree centerline is at 344 deg")

#print ("Order base to tree centerline is at 226 deg")

input('Press ENTER to exit')