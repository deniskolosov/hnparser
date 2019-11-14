from bs4 import BeautifulSoup
from django.conf import settings
from test_appfollow.celery import app
import requests

from hackernews_parser.models import Post


@app.task(name='Fetch HN frontpage')
def process_request():
    # TODO: check if response.text is empty
    print('hello')
    url = settings.HN_URL
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text_to_url = [{"title": link.text, "url": link.get("href")} for link in soup.find_all(class_="storylink")]
    print(text_to_url)
    Post.objects.bulk_create([Post(title=i["title"], url=i["url"]) for i in text_to_url], ignore_conflicts=True)
