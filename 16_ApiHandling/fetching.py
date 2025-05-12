# learn basic about how to fetch from an API easily

import requests

def fetch_random_users():
    url = 'https://api.freeapi.app/api/v1/public/randomusers'
    res = requests.get(url)     # res is in text format

    data = res.json()           # converting it to json make data handling more efficient

    if data['success']:
        print("Yes")

        siz = len(data['data']['data'])
        for ind in range(0,siz):
            # we derived this format by checking resposne style of data i.e. check freeapi website
            print(data['data']['data'][ind]['name'])      
            print(data['data']['data'][ind]['cell'])      


    # print(res[0])

fetch_random_users()    