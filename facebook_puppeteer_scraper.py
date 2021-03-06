'''
In this file, I want to query the Facebook Graph API to get the event objects that the Mappening Facebook Account (Selim Alpay) is interested in.
Once I have those event objects, I want to push them to the test data facebook collection
'''

import requests
import json
import time, datetime, dateutil.parser, pytz
from dateutil.tz import tzlocal
from pprint import pprint
from tqdm import tqdm   # a progress bar, pretty


# for sys.exit()
import os

# from definitions import CENTER_LATITUDE, CENTER_LONGITUDE, BASE_EVENT_START_BOUND

# need this to run file locally, or else won't know where to find mappening.utils.*
import sys
sys.path.insert(0, './../../..')

# from mappening.utils.database import events_fb_puppeteer_collection
# from mappening.utils.secrets import FACEBOOK_USER_ACCESS_TOKEN_2

import facebook

import json

# Problem 1: need to refresh accesstoken each time
accessToken = 'EAAFB1Et4EnkBAK68ZAR09HfIUDrIjZA6a7OECo5DSotHRGQki8C9YOxpAzaSUZAY1GwLcpWXjGs6I1WKN2DLUZChI7fXNkFxMQyrAvLBbApRgQdYeZBNGqAwBXAhBNZAQmkxjiK0yTDLVN9WyOITWgy2EXcjtrySZCNpl3ja9LRo1Jcw2WzQgpGKmWUl4U7pY1I6IIgt6tsEy99y8639BRJSHVyctfTD91cqg2cyx5p3wZDZD'

def facebook_scrape():

    graph = facebook.GraphAPI(access_token=accessToken) 

    # selim's facebook id
    profile = graph.get_object(id='100035494397802')

    events = graph.get_connections("me", "events")

    events_json = json.dumps(events['data'])

    print('got following events from Selim Alpay, mappening test account')
    # print(type(events))
    print(events_json)
    # print(type(json.loads(events_json)))

    # datastore = json.loads(events_json)
    datastore = events['data']
    print(type(datastore))

    # change "zip" to "zipcode" to align data with backend!!
    for event in datastore:
        if 'location' in event['place'] and 'zip' in event['place']['location']:
            event['place']['location']['zipcode'] = event['place']['location'].pop('zip')
            print(event['place']['location'])

    # get all cover images
    event_covers = graph.get_connections("me", "events{covers}")

    print(event_covers)


    # # remove all the events from collection hehe
    # events_fb_puppeteer_collection.remove( {} )

    # for event in datastore:
    #     # insert_one all events object
    #     events_fb_puppeteer_collection.insert_one(event)
        
    # # print(len(datastore))


    return events_json

facebook_scrape()