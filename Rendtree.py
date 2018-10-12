#comment section
#RendGeo written by Korbelz
#current scope: sparks per day

spark_tree = int(input("How many spirits does your tree have?: no commas please "))

outpost = int(input("How many outposts do you control? 0 - 9: "))

outpost_per = (outpost * 5)/1000
#print (outpost_per)

faction_total = (outpost_per + 0.02) 
human_total = (faction_total * 100)
print (f'You are gaining {human_total} percent today')

remaining_spirit = (100000 - spark_tree)
#print (remaining_sparks)

daily_sparks = (remaining_spirit * faction_total)
print (f'daily spirit generation is {daily_sparks}')

input('Press ENTER to exit')