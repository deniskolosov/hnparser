from django.test import TestCase
from django.urls import reverse
from freezegun import freeze_time

from hackernews_parser.tests.factories import PostFactory


@freeze_time("2019-01-01")
class GetPostsTestCase(TestCase):
    def setUp(self):
        self.post = PostFactory(title='Foo Bar', url='http://foo.bar')
        self.post1 = PostFactory(title='Bar Baz', url='http://bar.baz')
        self.url = reverse('posts-list')
        self.expected_results = [
            {'id': 1, 'title': 'Foo Bar', 'url': 'http://foo.bar', 'created_at': '2019-01-01T00:00:00Z'},
            {'id': 2, 'title': 'Bar Baz', 'url': 'http://bar.baz', 'created_at': '2019-01-01T00:00:00Z'},
        ]

    def test_get_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        results = response.json()['results']
        self.assertEqual(len(results), 2)

