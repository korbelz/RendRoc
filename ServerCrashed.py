#comment section
#RendGeo written by Korbelz
#current scope: Time stamp for server crashes

import datetime

server = input("What server do you play on: ")

i_loop = 0

while i_loop < 5:
    print ("***")
    print ("%s crashed at:"%(server))
    print ("UTC time: ", datetime.datetime.now( datetime.timezone.utc).strftime("%Y-%m-%d %H:%M") )
    print ("***")
    input('Press ENTER to generate a new crash log')
    i_loop += 1