####
"""
Fontes de estudo 
https://code.tutsplus.com/tutorials/using-the-requests-module-in-python--cms-28204
http://zetcode.com/web/pythonrequests/
http://www.pt.w3eacademy.com/python/python_dictionary.htm
http://www.w3big.com/pt/python/att-dictionary-get.html

"""
####

import requests
from urllib.request import urlopen

url = requests.get("http://freegeoip.net/json/50.78.253.58")

print(url.encoding)    
print(url.status_code)


print("\n")

url2 = urlopen("http://freegeoip.net/json/50.78.253.58")

print(url2.status_code)
print(url2.encoding)    

