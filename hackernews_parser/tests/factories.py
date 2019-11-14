import factory

from hackernews_parser.models import Post


class PostFactory(factory.DjangoModelFactory):
    class Meta:
        model = Post
