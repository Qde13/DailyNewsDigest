import requests
from send_email import send_email

topic = "tesla"

api_key = "631e576fc57f4eac898239bbe10f438b"
url = ("https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2023-08-22&sortBy=publishedAt" \
       "&apiKey=631e576fc57f4eac898239bbe10f438b&"\
       "language=en")

request = requests.get(url)

content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject:Today's news" + "\n" \
               + body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(body)
