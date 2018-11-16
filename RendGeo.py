#comment section
#RendGeo written by Korbelz
#current scope: Direction finder
#sample user input target: V(X=211.367, Y=-831.936, Z=45.251)
#sample user input current: V(X=100.367, Y=-831.936, Z=45.251)
#RE line: '^A-Z(),=\s'

import math
import re

i_loop = 0

x_tree = 0

y_tree = 0

user_loc_two = input("Paste loc of body or target from in-game, Ctrl + V: ")
#print (user_loc_two)
regex = re.compile('[^A-Z(),=\s]+')
s = regex.findall(user_loc_two)
#print (s)

x_two = float(s[0])
#print(x_two)

y_two = float(s[1])
#print(y_two)

def tree(x_tree , y_tree , x_one , y_one):
    rad_tree = math.atan2 ((y_tree - y_one),(x_tree - x_one))
    #print (rad_tree)
    bearing_tree = int(math.degrees(rad_tree))
    #print (bearing_tree)
    if bearing_tree < 0:
        bearing_tree = 360 + bearing_tree
    print (f'current location to tree is bearing {bearing_tree}')
    return bearing_tree

def target(x_two , y_two , x_one , y_one):
    rad_target = math.atan2 ((y_two - y_one),(x_two - x_one))
    #print (rad_target)
    bearing_target = int(math.degrees(rad_target))
    #print (bearing_target)
    if bearing_target < 0:
        bearing_target = 360 + bearing_target
    print (f'current location to target is bearing {bearing_target}')
    return bearing_target

while i_loop < 5:
    user_loc_one = input("Paste current loc from in-game, Ctrl + V: ")
    regex_one = re.compile('[^A-Z(),=\s]+')
    s_one = regex_one.findall(user_loc_one)
    x_one = float(s_one[0])
    y_one = float(s_one[1])
    heading_tree = tree(x_tree , y_tree , x_one , y_one)
    heading_target = target(x_two , y_two , x_one , y_one)
    i_loop += 1

input('Press ENTER to exit')