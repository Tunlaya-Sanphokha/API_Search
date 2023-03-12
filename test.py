import csv
from tempfile import NamedTemporaryFile

file_name = 'file_list_API.csv'
csvfile = open(file_name, 'r', encoding="utf8")
headers = ["update_time",'file_name']
reader = csv.reader(csvfile, delimiter=',') # Checkink NotFoundError 
tempfile = NamedTemporaryFile(mode='w', delete=False, newline='',encoding='utf-8')
writer_re = csv.DictWriter(tempfile, fieldnames=headers)
writer_re.writeheader()
for row in reader:
    print(row[1])
print("111111111111111")