from rest_framework import viewsets

from api.serializers import PostSerializer
from hackernews_parser.models import Post


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
