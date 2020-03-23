import requests
import json
import re
url = ('http://newsapi.org/v2/top-headlines?'
       'country=ru&'
       'apiKey=244c87d893404b998d472d3212b0ab64')
params = {'from-param': '2020-03-20'}
response = requests.get(url).json()

with open ('data_headlines.txt', 'w') as f:
    json.dump(response, f)
with open ('data_headlines.txt') as f:
    data = json.load(f)

#print(data)
articles = ''
for key, value in data.items():
    if key == 'articles':
        articles = str(value)

for element in articles:
    if element == '[' or element == ']':
        articles = articles.replace(element, '')

result_headlines = []
result_headlines = re.findall("(?<='title': ')(.*?)(?=', 'description')", articles)
for headlines in result_headlines:
    print(headlines)



#API key a41ac16803825519ca3b42bccd5769f6

#244c87d893404b998d472d3212b0ab64 NewsAPI