import csv
import pandas as pd
from tempfile import NamedTemporaryFile
from API import *
import unittest

from datetime import datetime
time1 = []
check = 'eversoul'
lan = 'en'
since = "2023-03-15"
until = "2023-03-21"
D = 'D'

def update():
    with open('file_list_API.csv', 'rt', encoding="utf8") as f:
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
                    return True


if __name__ == "__main__":
    
    class Unit_test(unittest.TestCase):
        def test_update(self):
            test = update()
            self.assertTrue(test)

    unittest.main()








