import feedparser
from dateutil.parser import parse
from datetime import datetime, timezone 
import json
import requests
import time
from config import feed_url,slack_hook

def write_file(id):
   with open('donejobs.txt', 'a') as f:
      f.write(id) 
      f.write('\n')

def read_file():
   my_file = open("donejobs.txt", "r")
   data = my_file.read()
   data_into_list = data.split("\n")
   return data_into_list

while True:   
   response=feedparser.parse(feed_url)
   data_into_list=read_file()
   for entry in response.entries: 
      id=entry['id'] 
      if id not in data_into_list:  
         createdAt=entry['updated']
         if (datetime.now(timezone.utc) - parse(createdAt, ignoretz=False)).seconds<600:
            write_file(id)
            print(entry)
            webhook_json={'text': 'Link: {link}, Job Title: {jobtitle}, Job Details: {jobdetails}'.format(link=entry['link'] ,jobtitle=entry['title'],jobdetails=entry['summary']),}
            requests.post(slack_hook,json=webhook_json)
         print('Sleeping.......')   
         time.sleep(60)  