import ftplib
import csv
import glob
import os
from datetime import date
from datetime import datetime

def main():

    now = datetime.now() 
    date_time = now.strftime("%Y-%m-%d-%H%M%S")
    
    FTP_HOST = "*********"
    FTP_USER = "*******"
    FTP_PASS = "***********"
    try:
        ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)

        ftp.encoding = "utf-8"

        data = []

        ftp.dir(data.append)

        latest_name = data[-2]
        latest_name = latest_name[::-1]
        latest_name = latest_name[0:27]
        latest_name = latest_name[::-1]

        print(latest_name,"er downloadet")

        with open(latest_name, 'wb') as f:
         ftp.retrbinary('RETR '+ latest_name, f.write)

        ftp.quit()
    except:
        print("Problemer med FTP eller " + latest_name +" er åben")
    
    print("Viser data fra sidst indlæste fil tryk enter for at fortsætte")
    input()

    csvfile = latest_name

    list_of_files = glob.glob('c:/py/ftp/*.csv') # *.csv means csv if need specific format then *.format
    latest_file = max(list_of_files, key=os.path.getctime)
    
    file = open(latest_file)

    type(file)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    header
    rows = []
    for row in csvreader:
            rows.append(row)
    rows
    with open(latest_file, encoding='utf-8-sig') as file:
        content = file.readlines()
    header = content[:1]
    rows = content[1:]
    #print(header)
    #print(rows)
    file.close()
    a = open(str(date_time)+".txt", "w")
    i = 0
    while i < len(rows):
     a.write(str((rows[i].split(";")[0],
     (rows[i].split(";")[4]),
     (rows[i].split(";")[7]),
     (rows[i].split(";")[2]),
     (rows[i].split(";")[3]),
     (rows[i].split(";")[9]),
     (rows[i].split(";")[10]),
     (rows[i].split(";")[8]))))
     i = i + 1
    a.close

    i = 0
    while i < len(rows):
     print(rows[i].split(";")[0],
     (rows[i].split(";")[4]),
     (rows[i].split(";")[7]),
     (rows[i].split(";")[2]),
     (rows[i].split(";")[3]),
     (rows[i].split(";")[9]),
     (rows[i].split(";")[10]),
     (rows[i].split(";")[8]))
     i = i + 1

    print(len(rows)," målere er på listen i filen",csvfile)
    print("Tryk enter for at afslutte")
    input()
if __name__ == '__main__':
    main()