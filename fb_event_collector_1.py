FACEBOOK_USER_ACCESS_TOKEN = "EAAFB1Et4EnkBAJmH7gYpBXLdjtl5kGcuvZAZBebSSH91TFt2oRyrUBRHeYXyAR7mh3qppZBicZAoo6ImzbWaohhOQW9Ogf3hUhnR2ll6hAYk4kjtqCZBK0DPLLmAB7o3rilOguJMrai0HAxJi22xx2GJk63NJwoVXIWCiAtVDlnuLfsJHOMPrL6GtvHng3SzdmpEq6ALHfjzTQDNv3C3MZBBMTUwM0W7tviIkH5vZA37QZDZD"

import requests




def get_interested_events():

    # curr_url = 'https://graph.facebook.com/v5.0/me/events?fields=category,cover,description,start_time,is_canceled,name,owner,updated_time,id,place,maybe_count,noreply_count,interested_count,attending_count,end_time,event_times'
    curr_url = 'https://graph.facebook.com/v5.0/me/events'


    total = 0
    page_num = 0
    events = []

    while (curr_url):

        search_args = {
            # 'fields': "category,cover,description,start_time,is_canceled,name,owner,updated_time,id,place,maybe_count,noreply_count,interested_count,attending_count,end_time,event_times",
            # 'fields': "category,cover,description,start_time,name,updated_time,id,place,end_time,event_times",
            'fields': "id,name,cover,description,start_time,end_time,place,event_times",
            'access_token': FACEBOOK_USER_ACCESS_TOKEN,
            'limit': 100,
            
        }

        


        resp = requests.Session().get(curr_url, params=search_args)

        data = resp.json()


        # try:
        print (curr_url)

        # if page_num == 0:
        #     events += data['events']['data']

        #     total += len(data['events']['data'])
        #     curr_url = data['events']['paging']['next']

        #     print(page_num)
        #     print(data['events']['data'])

        # elif page_num >= 1:
        events += data['data']

        total += len(data['data'])
        if 'next' in data['paging']:
            curr_url = data['paging']['next']
        else:
            break

        print(page_num)
        print(data)

        # print(page_num)
        page_num += 1
        # except KeyError:
        #     break

        # check if there is a next page of results
        # if 'paging' not in data or 'next' not in data['paging']:
        #     # no more responses
        #     curr_url = ""
        #     break
        # else:
        #     curr_url = data['paging']['next']
        #     print(curr_url)

    # print(total)
    print(len(events))
    # print(data['events']['data'])
    # print(len(data['events']['data']))
    # print(events)

    return events

# Process for frontend to use it 
def process_events(all_events):

    filtered_events = []

    # print(all_events)

    # for event in all_events:

    #     # some events don't have a place, if they don't maybe just remove them for now and later try to get the place
    #     # TODO: find place from owner's location if place is not present
    #     if "place" not in event:
    #         print("no place")
    #         print(event)
    #         # don't add to filtered_events
    #         continue

    #     # some events have "place" but no "place.location"
    #     # this happens with some events that are imported to facebook from eventbrite
    #     # I.E. they have "owner" == Eventbrite
    #     # if this happens we can just exclude them from the facebook database collection
    #     # this might even be a good thing because if they are eventbrite events, it would be difficult to dedupe across collections anyways
    #     if "location" not in event["place"]:
    #         print ("no location")
    #         print(event)
    #         continue

    #     # change "zip" of place.location to "zipcode"
    #     if 'location' in event['place'] and 'zip' in event['place']['location']:
    #         event['place']['location']['zipcode'] = event['place']['location'].pop('zip')
        
    #     # if event does not have an endtime, give it an endtime 1 hour into the future
    #     if "end_time" not in event:
    #         print("no end_time")
    #         event["end_time"] = (datetime.datetime.strptime(event["start_time"], '%Y-%m-%dT%H:%M:%S%z') + datetime.timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%S%z')
    #         print(event["end_time"])


    #     filtered_events.append(event)

    # # URL parameters for refreshing / updating events info, including subevents
    # sub_event_call_args = {
    #     'fields': ','.join(EVENT_FIELDS),
    #     'access_token': app_access_token
    # }

    # additional_events = []
    # # check for multiday events
    # for event in all_events:
    #     expanded_event_dict = {}
    #     # check for multi-day events, need API call again
    #     if 'event_times' in event:
    #         # need to call API again for event fields
    #         # batch call with multiple IDs: slightly faster from less network traffic, Facebook's end
    #         sub_ids = []
    #         for sub_event_header in event['event_times']:
    #             sub_ids.append(sub_event_header['id'])
    #         # sub_event_call_args['ids'] = ','.join(sub_ids)

    #         for id in sub_ids:
                
    #             resp = s.get(BASE_EVENT_URL + id, params=sub_event_call_args)
    #             # print(resp.url)
    #             if resp.status_code != 200:
    #                 print(
    #                     'Error trying to retrieve sub-event data of event {0}: Status code {1}'
    #                     .format(event['id'], resp.status_code)
    #                 )
    #                 # just skip this multi-day event if sub-events not successfully retrieved
    #                 continue
                
    #             expanded_event_dict = resp.json()

    #             # not sure if this is needed --haki
    #             # # add special "duplicate_occurrence" tag for event occurrences in the future that
    #             # # won't be searchable, because the 1st event start time has passed already
    #             # # don't need to refresh for the 1st event, since that matches the total event start time
    #             # for sub_event in expanded_event_dict.values():
    #             #     # using dict.values() and editing each item in list still changes original dictionary
    #             #     if sub_event['start_time'] != event['start_time']:
    #             #         sub_event['duplicate_occurrence'] = True

    #             additional_events.append(expanded_event_dict)
    #     # I have no idea what this else statement is doing --haki
    #     # else:
    #     #     expanded_event_dict.update({event['id']: event})


    # print("additional events")
    # print(len(additional_events))

    # filtered_events.extend(additional_events)

    # print("filtered events")
    # print(len(filtered_events))

    # # need to map facebook categories to bmaps categories
    # # also do we need to run the ML for figuring out the categories?
    # categorized_clean_events = categorizeEvents(filtered_events)
    # categorized_clean_events = labelFreeFood(categorized_clean_events)
        
    # # Autocategorization has a cleaner way to do this path switching
    # savedPath = os.getcwd()
    # os.chdir(API_UTILS_PATH)
    # with open('facebk.json', 'w') as f:
    #     json.dump(categorized_clean_events, f, sort_keys=True, indent=4, separators=(',', ': '))
    # os.chdir(savedPath)

    # # add filtered events to database
    # events_facebook_processed_collection.delete_many({})
    # events_facebook_processed_collection.insert_many(categorized_clean_events)

    # return categorized_clean_events
        

"""
hakan added for facebook events testing
"""
fb_events = get_interested_events()
# fb_events_cleaned = process_events(fb_events)
# print(len(fb_events_cleaned))
# return jsonify(len(fb_events_cleaned))