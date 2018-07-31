import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=94074cd9596f4e2a812c7e6eb286ac7f')
response = requests.get(url)
response.json()
