# ref: https://stackoverflow.com/questions/43388476/how-could-spacy-tokenize-hashtag-as-a-whole
# ref: https://universaldependencies.org/docs/u/pos/
# ref: https://www.dataquest.io/blog/tutorial-text-classification-in-python-using-spacy/

# ref: https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
# ref: https://medium.com/@m.treerungroj/machine-learning-supervised-learning-with-basic-scikit-learn-part1-99b8b2327c9
# ref: https://spacy.io/api/pipeline-functions#merge_entities
# ref: https://spacy.io/api/token
import spacy
from nltk.corpus import stopwords
import csv
from spacy.lang.en.stop_words import STOP_WORDS
from pythainlp import*
from pythainlp.corpus import*
import pandas as pd
import re
import time
import unittest
from datetime import datetime
from tempfile import NamedTemporaryFile
import shutil
import en_core_web_sm
from API import *

class NLP:
    def __init__(self):
        #Build file csv
        print('hello')

    #select th or en word to analysis and count them
    def save_analysis(self, lang, data,since,until):
        self.csvfile_input = open('C:\\Users\\non42\\Documents\\GitHub\\API_Search\\Data\\'+str(data)+'_Data.csv', 'r',newline='', encoding="utf-8")
        self.csv_reader = csv.reader(self.csvfile_input, delimiter=',')
            
        fieldnames = ['10 ranking','number']
        self.csvfile_output = open('C:\\Users\\non42\\Documents\\GitHub\\API_Search\\Data\\'+str(data)+'_NLP.csv', 'w', newline='', encoding="utf-8")
        self.writer_output = csv.DictWriter( self.csvfile_output, fieldnames=fieldnames )
        self.writer_output.writeheader()

        dict_temp = {}
        first = 0
        self.nlp = en_core_web_sm.load()
        
        for row in self.csv_reader:
            print(first)
            if(first > 0):
                if(lang == "th"):
                    temp = self.analyze_word_th(row[2],data)  #ทำงานใน functionนี้มาเก็บใน temp
                elif(lang == "en"):
                    temp = self.analyze_word_en(row[2],data)

                for i in temp:  #ได้temp มาแล้วก็เอามา วนนับ
                    message = i.lower()
                    if( message not in dict_temp ):
                        dict_temp[message] = 1
                    elif( message in dict_temp ):
                        dict_temp[message] += 1
                if(first == 5):
                    break
            first += 1
        self.dict_sort = self.bubbleSort(dict_temp) #ได้temp มาแล้วก็เอามา วน10คำ
        for temp in self.dict_sort:
            self.writer_output.writerow({'10 ranking':temp, 'number':dict_temp[temp]})
        self.csvfile_output.close()
        self.csvfile_input.close()
        self.re_search(lang,data,since,until)

    #analysis th word
    def analyze_word_th(self, data , search):
        words = thai_stopwords()  #ตัดคำฟุ่มเฟือย พวกสระเกิน
        V = []
        data = re.sub("[0-9]",'',data)  #ใช้ regular ตัด 0-9 ออก
        data = re.sub("[a-z A-Z]",'',data) #ใช้ re ตัด  A-Z
        nlp = word_tokenize(data , engine='newmm',keep_whitespace=False)  #เก็บข้อมูลคล้าย อาเรย์?
        nlp1 = [data for data in nlp if data not in words] #เอาข้อมูลที่คลีนแล้ว ?
        for i in nlp1:
            r = re.sub('\w','',i)
            if i != search:     #ไม่เอาที่จะ query
                if i not in r and data:
                    V.append(i)
        return V

    #analysis en word
    def analyze_word_en(self, data , search):
        data = re.sub("[0-9]",'',data)
        data = re.sub("#",'',data)
        data = re.sub("|",'',data)
        data = re.sub("-",'',data)
        self.output = []
        self.check = {}
        self.data = data
        self.docs = self.nlp(self.data)
        for word in self.docs:
            self.twitter_check =( word.text[0]!="#"
                                    and word.text[0]!="@"
                                    and "#"+word.text not in self.check
                                    and "@"+word.text not in self.check
                                    and word.text not in self.nlp.Defaults.stop_words 
                                    and word.text not in stopwords.words('english')
                                    and not word.is_punct 
                                    and "https:" not in word.text 
                                    and self.filter_type(word)
                                    and word.text.lower() != search.lower())
            if( self.twitter_check ):
                self.output.append(word.text)
        return self.output

    def merge_noun(self):
        merge_nps = self.nlp.create_pipe("merge_noun_chunks")
        self.nlp.add_pipe(merge_nps)
        self.docs = self.nlp(self.data)

    def filter_type(self, word):
        type_word = ["ADJ", "INTJ","NOUN", "PROPN", "VERB", "NUM"]
        if( word.pos_ in type_word ):
            return True
        else:
            return False

    def bubbleSort(self, dict_temp):
        first = 0
        key = [i for i in dict_temp.keys()]
        value = [i for i in dict_temp.values()] #เก็บค่าที่ถูกนับ
        sort = {}
        for f in range(len(value)): 
            for s in range(len(value)-f-1): 
                if value[f] <= value[f+s] : 
                    value[f], value[f+s] = value[f+s], value[f]
                    key[f], key[f+s] = key[f+s], key[f]   #สลับตำแหน่ง value 
        for fi in range(len(dict_temp)):
            if first < 10:
                sort[key[fi]] = value[fi]
                first += 1

        return sort
    #research ข้อมูล
    def re_search(self,lang,data,since,until):
        #research
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        headers = ["update_time",'file_name']
        file_name = 'file_list_API.csv'
        try:
            csvfile = open(file_name, 'r', encoding="utf8")
            reader = csv.reader(csvfile, delimiter=',') # Checkink NotFoundError 

            tempfile = NamedTemporaryFile(mode='w', delete=False, newline='',encoding='utf-8')
            writer_re = csv.DictWriter(tempfile, fieldnames=headers)
            writer_re.writeheader()
            print("111111111111111")
            first = 0
            n = []
            for row in reader:
                if(first > 0):
                    if(row[1] == str(data)+'.csv'):
                        writer_re.writerow( {'update_time':date_time, 'file_name':str(data)+'.csv'} )
                    else:
                        writer_re.writerow( {'update_time':row[0], 'file_name':row[1]} )
                n.append(row[1])
                first += 1

            if(str(data)+'.csv' not in n):
                writer_re.writerow( {'update_time':date_time, 'file_name':str(data)+'.csv'} )
            
            self.update_time(lang,data,since,until)
            
            tempfile.close()
            csvfile.close()

            shutil.move(tempfile.name, file_name)
            
        except FileNotFoundError:
            print("2222222222222")
            csvfile = open(file_name, 'w', newline='', encoding="utf8")
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            
            csvfile = open(file_name, 'a', newline='', encoding="utf8")
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writerow( {'update_time':date_time, 'file_name':str(data)+'.csv'} )
            csvfile.close()

    def update_time(self,lang,data,since,until):
        D = 'D'
        time1 = []
        with open('file_list_API.csv', 'rt', encoding="utf8") as f:
            reader = csv.reader(f, delimiter=',') # good point by @paco
            for row in reader:
                for field in row:
                    if field == (data+'.csv'):

                        date_list = pd.date_range(since, until, freq=D)

                        # if you want dates in string format then convert it into string
                        time2 = date_list.strftime("%Y-%m-%d")

                        pan = pd.read_csv('C:\\Users\\non42\\Documents\\GitHub\\API_Search\\Data\\' + str(data)+'_Data.csv')
                        colume1 = pan['time'] >= f'{since} 00:00:00'
                        colume2 = pan['time'] <= f'{until} 23:59:59'
                        between = pan[colume1 & colume2]
                        df = pd.DataFrame({'time': between['time'],'tweet': between['tweet'],'places': between['places']})
                        
                        for i in df['time']:
                            time1.append(i[:10])
                        print("time1 =", time1)

                        result1 = list(set(time2) - set(time1))  #หาตัวที่ต่างกันของdf กับ เวลาที่เราต้องการ
                        result1 = sorted(result1, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))
                        try: 
                            print(result1[0])
                            print(result1[-1])
                            obj1 = Twitter_API(data,lang,result1[0],result1[-1])
                            obj1.search()
                        except IndexError:
                            print("Do nothing")

if __name__ == "__main__":
    
    class Unit_test(unittest.TestCase):
        def test_NLP(self):
            obj = NLP()
            obj.save_analysis('en','eversoul','2023-03-12','2023-03-21')
            self.assertIsNotNone(obj)

    unittest.main()
