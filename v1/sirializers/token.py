from abc import ABC

from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    """
    トークン登録APIのSerializer
    """
    token = serializers.CharField()
