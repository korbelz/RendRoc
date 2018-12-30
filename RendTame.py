#comment section
#RendGeo written by Korbelz
#current scope: Taming info


print ('*** This app is a failed taming calc :P ***')
print ('*** Written by Korbelz ***')
print ('*** Feedback/Bugs: Discord: Korbelz#3504 ***')
input('Press ENTER to continue')

import array

arrow = int(input("What tier taming arrow are you using? 0 - 4: "))

arr_dmg = array.array('i', [2,2,5,8,15])

raw_dmg = (arr_dmg[arrow] * 25)
print (raw_dmg)