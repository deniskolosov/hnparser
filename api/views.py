from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.serializers import PostSerializer
from hackernews_parser.models import Post


class ModifiedLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = ModifiedLimitOffsetPagination
