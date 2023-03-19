import csv
import pandas as pd
from tempfile import NamedTemporaryFile
from API import *

file_name = 'file_list_API.csv'
csvfile = open(file_name, 'r', encoding="utf8")
headers = ["update_time",'file_name']
reader = csv.reader(csvfile, delimiter=',') # Checkink NotFoundError 
tempfile = NamedTemporaryFile(mode='w', delete=False, newline='',encoding='utf-8')
writer_re = csv.DictWriter(tempfile, fieldnames=headers)
writer_re.writeheader()
for row in reader:
    print(row[1])
print("---------------------check file list API :>----------------")

from datetime import datetime
time1 = []
check = 'eversoul'
lan = 'en'
since = "2023-03-12"
until = "2023-03-18"
D = 'D'
"""start_date = datetime.strptime(since, "%Y-%m-%d")
end_date = datetime.strptime(until, "%Y-%m-%d")"""
with open('file_list_API.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',') # good point by @paco
    for row in reader:
        for field in row:
            if field == (check+'.csv'):

                date_list = pd.date_range(since, until, freq=D)

                # if you want dates in string format then convert it into string
                time2 = date_list.strftime("%Y-%m-%d")

                pan = pd.read_csv('C:\\Users\\User\\Documents\\GitHub\\API_Search\\Data\\' + str(check)+'_Data.csv')
                colume1 = pan['time'] >= f'{since} 00:00:00'
                colume2 = pan['time'] <= f'{until} 23:59:59'
                between = pan[colume1 & colume2]
                df = pd.DataFrame({'time': between['time'],'tweet': between['tweet'],'places': between['places']})
                
                for i in df['time']:
                    time1.append(i[:10])
                print("time1 =", time1)
                print(time2)

                result1 = list(set(time2) - set(time1))  #หาตัวที่ต่างกันของdf กับ เวลาที่เราต้องการ
                result1 = sorted(result1, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))
                print(result1)
                #obj = Twitter_API(check,lan,result1[0],result1[-1]) #คิวรี่เฉพาะวันที่ต่างกัน จากเริ่มถึง สิ้นสุด
                #obj.search()






