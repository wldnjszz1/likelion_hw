from rest_framework import serializers
from .models import Post

class PostSerialzers(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id','author_username','message']