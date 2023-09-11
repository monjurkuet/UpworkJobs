import feedparser
from dateutil.parser import parse
from datetime import datetime, timezone 
import json
import requests
import time
from config import FEED_LIST

for feed_url in FEED_LIST:
    response=feedparser.parse(feed_url)
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