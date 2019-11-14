import logging

from bs4 import BeautifulSoup
from django.conf import settings
from test_appfollow.celery import app
import requests

from hackernews_parser.models import Post

logger = logging.getLogger(__name__)


@app.task(name='Fetch HN frontpage')
def process_request():
    url = settings.HN_URL
    response = requests.get(url)

    # Check if fetch is successful.
    if "https://news.ycombinator.com" in response.text:
        soup = BeautifulSoup(response.text, 'html.parser')
        text_to_url = [{"title": link.text, "url": link.get("href")} for link in soup.find_all(class_="storylink")]
        Post.objects.bulk_create([Post(title=i["title"], url=i["url"]) for i in text_to_url], ignore_conflicts=True)
    else:
        logger.warning("Could not fetch the page!")
