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
import requests as req

url = req.get("https://twitter.com/_Astor_333")

arq= open("arq_1.txt",'w')
arq.write(str(url.text))
arq.close()
#print(url.text)

url2 = requests.get("https://twitter.com/_Astor_333")

arq2= open("arq_2.txt",'w')
arq2.write(str(url2.text))
arq2.close()

## Ambas as chamadas das funções possuem o mesmo resultado prático
## mas a uma pequena alteração que aparentemente seria o "para identificar cada chamada"

# ao passar a url para pelo get para uma variavel esta se torna um objeto 
#cujo a codificação é em UTF-8
#e a resposta ao seu status, seguindo os padrões do HTTP, é 200 o que significa que o pedido de requisição do site foi cumprido com sucesso 

print(url.encoding)     # returns 'utf-8'
print(url.status_code)  # returns 200

print("\n")

print(url2.encoding)     # returns 'utf-8'
print(url2.status_code)  # returns 200





