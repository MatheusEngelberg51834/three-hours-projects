import requests

top_url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
id_url = "https://hacker-news.firebaseio.com/v0/item/"

r1 = requests.get(top_url).json()
for item in r1:
    r2 = requests.get(id_url + str(item) + ".json?print=pretty").json()
    try:
        print(r2['title'])
        print(r2['url'])
    except:
        pass