from rest_framework import serializers

from hackernews_parser.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'created_at']
