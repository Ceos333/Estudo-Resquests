import requests
scraping = requests.get("http://freegeoip.net/json/50.78.253.58")
scraping2 = requests.get('https://github.com/timeline.json')
print(type(scraping))
print("\n")
print(scraping.text)
print("\n")
print(scraping.headers['content-type'])
print("\n")
print(scraping.encoding)
print("\n")
print("2",type(scraping2))
print("\n")
print("2",scraping2.text)
print("\n")
print("2",scraping2.headers['content-type'])
print("\n")
print("2",scraping2.encoding)

url2 = requests.get("https://twitter.com/_Astor_333")
print("\n")
print(url2.headers['content-type'])
print("\n")

