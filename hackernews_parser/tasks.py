from bs4 import BeautifulSoup
from django.conf import settings
from celery import task
import requests

from hackernews_parser.models import Post


@task(name='Fetch HN frontpage')
def process_request():
    # TODO: check if response.text is empty
    url = settings.HN_URL
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text_to_url = [{"title": link.text, "url": link.get("href")} for link in soup.find_all(class_="storylink")]
    Post.objects.bulk_create([Post(title=i["title"], url=i["url"]) for i in text_to_url], ignore_conflicts=True)
