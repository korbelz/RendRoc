# Comment section
# RendRoc written by Korbelz
# current scope: Spark Calc

spark_ref = [0, 3333, 15000, 40000, 100000]

tier = input("what tier are you reseaching? ")
tier = int(tier)

#print (spark_ref[tier])

done = input("what percent is the reseach complete? ")
done = int(done)

#print (done)

bonus = input("what is your war observation bonus? ")
bonus = int(bonus)

completed = spark_ref[tier] * (done/100)
left = spark_ref[tier] - completed

print(f'{left} sparks left with no war bonus')

war = (bonus/100)
#print (war)

warleft = left - (war * spark_ref[tier])
print (f'{warleft} sparks left with war bonus' )
