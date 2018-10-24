#comment section
#RendGeo written by Korbelz
#current scope: sparks per day

spirit_tree = int(input("How many spirits does your tree have?: no commas please "))

outpost = int(input("How many outposts do you control? 0 - 9: "))

remaining_spirit = (100000 - spirit_tree)

outpost_per = (outpost * 5)/1000
#print (outpost_per)

faction_total = (outpost_per + 0.02) 
human_total = (faction_total * 100)
print (f'You are gaining {human_total} percent today')

daily_spirits = 0 

def gen_spirits(st , fp):
    remaining_spirit = (100000 - st)
    #print (remaining_sparks)
    daily_spirits = (remaining_spirit * fp)
    #print (f'daily spirit generation is {daily_spirits}')
    return daily_spirits


print ("your daily spirit generation today is %s"%(gen_spirits(spirit_tree , faction_total)))

new_spirit_tree = (gen_spirits(spirit_tree , faction_total)) + spirit_tree
#print (new_spirit_tree)

days = 0
while new_spirit_tree < 98000:
    new_daily_spirit = (gen_spirits(new_spirit_tree , faction_total))
    new_spirit_tree = (new_daily_spirit + new_spirit_tree)
    days += 1

print ("Days remaining until you reach 98000 spirits: %s"%(days))

input('Press ENTER to exit')