import requests

articles = requests.get("https://api.spaceflightnewsapi.net/v3/articles?_limit=10")
# print(url.text)
articles_json = articles.json()
print(articles_json)
print("--------------------------------------------------")

n = 1
for i in articles_json[0:10]:
    print(n, i['newsSite'], "\n", i['title'], "\n", i['url'], "\n", i['summary'], "\n", i['publishedAt'])
    n = n + 1
