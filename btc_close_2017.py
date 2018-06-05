from __future__ import  (absolute_import, division, print_function, unicode_literals)

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen 

import json
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)

#read data
req = response.read()
# writa data into file
with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)
# load json format
file_urllib = json.loads(req)
print(file_urllib)
