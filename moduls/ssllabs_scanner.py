import requests
import time
import sys


def requestAPI(payload={}):
    '''Send request'''
    
    url = 'https://api.ssllabs.com/api/v2/analyze'
    try:
        response = requests.get(url, params=payload)
    except Exception as e:
        print('ERROR IN REQUESTS!\n{}\n'.format(repr(e)))
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
        while results['status'] != 'READY' and
        results['status'] != 'ERROR':
            time.sleep(30)
            results = requestAPI(payload)
    except KeyError as e:
        print("ERROR IN results['status']!\n{}\n".format(repr(e)))
    return results
