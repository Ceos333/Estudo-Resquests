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

url2 = requests.get("https://twitter.com/_Astor_333")

arq2= open("arq_2.txt",'w')
arq2.write(str(url2.text))
arq2.close()

print(url2.cookies)
