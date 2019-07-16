import requests
import time
import sys

def requestAPI(payload={}):
    '''Send request to https://api.ssllabs.com/api/v2/analyze'''
    url = 'https://api.ssllabs.com/api/v2/analyze'
    try:
        response = requests.get(url, params=payload)
    except Exception as e:
        print('ERROR IN REQUESTS!\n' + repr(e) + '\n')
    data = response.json()
    return data
	
def newScan(domain):
    '''Create new scan domain'''
    payload = {
                'host': domain,
                'publish': 'off',
                'startNew': 'on',
                'all': 'done',
                'ignoreMismatch': 'on'
              }
    results = requestAPI(payload)
    payload.pop('startNew')
    try:
        while results['status'] != 'READY' and results['status'] != 'ERROR':
            time.sleep(30)
            results = requestAPI(payload)
    except KeyError as e:
        print("ERROR IN results['status']!\n" + repr(e) + '\n')
    return results
