from rest_framework import serializers

class NewsListSerializer(serializers.Serializer):
    # news_id = serializers.PrimaryKeyRelatedField(read_only=True, many = True)
    title = serializers.CharField(max_length = 50)
    link = serializers.CharField(max_length = 100)
    rate = serializers.IntegerField()
    date = serializers.DateField()
    author = serializers.CharField(max_length = 15)
    comm_count = serializers.IntegerField()
    # author = serializers.CharField(source='author.username', max_length=200)

class NewsInfoSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=50)
    rate = serializers.IntegerField()

class CommentSerializer(serializers.Serializer):
    text = serializers.CharField(max_length = 255)
    child_com = serializers.CharField(source = 'id_child.text', max_length = 255)