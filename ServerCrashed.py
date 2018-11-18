#comment section
#RendGeo written by Korbelz
#current scope: Time stamp for server crashes

import datetime
import csv

i_loop = 0

server = input("What server do you play on: ")
file_date = datetime.datetime.now( datetime.timezone.utc).strftime("%Y-%m-%d")
#print ((file_date) + " " + (server))
file_name = (file_date) + " " + (server)

with open(f'{file_name}.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(['date ', 'time ', f'{server} '])
    


while i_loop < 24:
    print ("***")
    print ("%s crashed at:"%(server))
    print ("UTC time: ", datetime.datetime.now( datetime.timezone.utc).strftime("%Y-%m-%d %H:%M") )
    print ("***")
    log_time = datetime.datetime.now( datetime.timezone.utc).strftime("%H:%M")
    log_date = datetime.datetime.now( datetime.timezone.utc).strftime("%Y-%m-%d")
    with open(f'{file_name}.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow([f'{log_date}  ', f'{log_time} '])
    input('Press ENTER to generate a new crash log or CLOSE terminal to exit')
    i_loop += 1