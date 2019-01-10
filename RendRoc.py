# Comment section
# RendRoc written by Korbelz
# current scope: Spark Calc


print ('*** This app is a research spark calc ***')
print ('*** Written by Korbelz ***')
print ('*** Feedback/Bugs: Discord: Korbelz#3504 ***')
input('Press ENTER to continue')

spark_ref = [0, 500, 3750, 15000, 40000, 100000]

tier = input("what tier are you reseaching? ")
tier = int(tier)

#print (spark_ref[tier])

done = input("what percent is the reseach complete? ")
done = float(done)

#print (done)

bonus = input("what is your war observation bonus? ")
bonus = int(bonus)

completed = spark_ref[tier] * (done/100)

war = ((bonus/100) * spark_ref[tier])
war_total = spark_ref[tier] - war 
war_completed = war_total * (done/100) 
#print (war_total)

left = 0
warleft = 0

if war > 0:
    warleft = war_total - war_completed
    print (f'{warleft} sparks left till complete' )
else:
    left = spark_ref[tier] - completed
    print(f'{left} sparks left with till complete')



input('Press ENTER to exit')
