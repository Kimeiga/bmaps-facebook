FACEBOOK_USER_ACCESS_TOKEN = "EAAFB1Et4EnkBAFm4Ftm1oaFZCMalNQITGHzCeBT7nMh08qfvNuxLZB5cGuRJrDBqnjwX0ndZAHwB2D2MlCx653SfHfuc4wKRgXabamtBfjtpwxZBAeKho9KpVprFE6F4VftnrdMDa5Qm4aPoKqoJJ7ZBCkScWCpGEiN6JpvZCtigZDZD"

import requests

curr_url = 'https://graph.facebook.com/v5.0/me?fields=events'

total = 0

while (curr_url):

    search_args = {
        'access_token': FACEBOOK_USER_ACCESS_TOKEN,
        'limit': 100
    }

    resp = requests.Session().get(curr_url, params=search_args)

    data = resp.json()


    try:
        total += len(data['events']['data'])
        curr_url = data['events']['paging']['next']

        print (curr_url)
    except KeyError:
        break

    # check if there is a next page of results
    # if 'paging' not in data or 'next' not in data['paging']:
    #     # no more responses
    #     curr_url = ""
    #     break
    # else:
    #     curr_url = data['paging']['next']
    #     print(curr_url)

print(total)
# print(data['events']['data'])
# print(len(data['events']['data']))