from rest_framework import serializers
from .serializers import Article


class ArticleSerializer(serializers):

    class Meta:
        model = Article
        fields = '__all__'