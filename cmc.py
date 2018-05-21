import requests
import json
import os
import time
import sys

service = False

if len(sys.argv) > 0:
    if sys.argv[1] == 'start':
        service = True

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
print(DATA_DIR)

def collect_data(limit=10000):
    URL = 'https://api.coinmarketcap.com/v1/ticker/?limit=%s' % str(limit)
    response = requests.get(URL)

    data_file_name = os.path.join(DATA_DIR, "cmc-%s.json" % time.strftime('%Y%m%d%H%M%S'))
    print("New file: %s" % data_file_name)
    with open(data_file_name, 'w') as data_file:
        data_file.write(response.text)
    data_file.close()
    #json_data = json.loads(response.text)

class Service:

    def __init__(self):
        while True:
            begin_time = time.time()
            collect_data()
            end_time = time.time()
            time.sleep(60 - (end_time - begin_time))

if service:
    service = Service()
else:
    collect_data()

#hello this is Ehsan
