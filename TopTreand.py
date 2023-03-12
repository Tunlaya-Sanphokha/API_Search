# import the module
import tweepy
import configparser
import csv
import pandas
# assign the values accordingly
config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config['Twitter_API']['consumer_key']
consumer_key_secret = config['Twitter_API']['consumer_key_secret']

access_token = config['Twitter_API']['access_token']
access_token_secret = config['Twitter_API']['access_token_secret']
 
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
 
# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)
 
# calling the api
api = tweepy.API(auth)
 
# WOEID of London
woeid = 23424960
 
# fetching the trends
trends = api.trends_place(woeid)
 
array_top = []

# printing the information
print("The top trends for the location are :")
 
for value in trends:
    for trend in value['trends'][:10]:
        array_top.append(trend['name'])

fieldnames = ['tweet_volume', 'url', 'query', 'name', 'promoted_content']
csvfile_output = open('C:\\Users\\User\\Documents\\GitHub\\API_Search\\Data\\10_TopTreand.csv', 'w', newline='', encoding="utf-8")
writer_output = csv.DictWriter(csvfile_output, fieldnames=fieldnames )
writer_output.writeheader()
for value in trends:
    for trend in value['trends'][:10]:
        writer_output.writerow(trend)
csvfile_output.close()

pan = pandas.read_csv('C:\\Users\\User\\Documents\\GitHub\\API_Search\\Data\\10_TopTreand.csv')
print(type(pan["name"]))