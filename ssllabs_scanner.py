import requests
import time
import sys

API = 'https://api.ssllabs.com/api/v2/'

def requestAPI(path, payload={}):
    url = API + path
    try:
        response = requests.get(url, params=payload)
    except Exception as e:
        print('ERROR IN REQUESTS!\n' + repr(e) + '\n')

    data = response.json()
    return data
	
def newScan(host, publish='off', startNew='on', all='done', ignoreMismatch='on'):
    path = 'analyze'
    payload = {
                'host': host,
                'publish': publish,
                'startNew': startNew,
                'all': all,
                'ignoreMismatch': ignoreMismatch
              }
    results = requestAPI(path, payload)
    payload.pop('startNew')
    
    try:
        while results['status'] != 'READY' and results['status'] != 'ERROR':
            time.sleep(60)
            results = requestAPI(path, payload)
    except KeyError as e:
        print("ERROR IN results['status']!\n" + repr(e) + '\n')

    return results
