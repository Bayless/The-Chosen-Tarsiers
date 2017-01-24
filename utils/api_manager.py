import requests

def issue_request(url, data_encoded = None, headers = None):
    if not data_encoded or not headers:
        r = urllib2.Request(url)
    else:
        r = urllib2.Request(url, data_encoded, headers) # Setups the object

    response = urllib2.urlopen(r, timeout = 30).read()
    response_data = json.loads(response)
        
    return response_data
    
