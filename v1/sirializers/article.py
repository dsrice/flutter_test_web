from abc import ABC

from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    """
    記事取得APIのSerializer
    """
    id = serializers.IntegerField(required=False)