from rest_framework import serializers

class NewsSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=50)
    rate = serializers.IntegerField()
    # author = serializers.CharField(source='author.username', max_length=200)