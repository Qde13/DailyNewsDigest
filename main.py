import requests

api_key = "e49117d391ec46d89bf0ccc2e297bebc"
url = ("https://newsapi.org/v2/everything?q=tesla" \
       "&from=2023-08-21&sortBy=publishedAt&apiKey=" \
       "e49117d391ec46d89bf0ccc2e297bebc")

request = requests.get(url)

content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
