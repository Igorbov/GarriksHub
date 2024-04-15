from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News, Comment
from .serializers import NewsListSerializer, NewsInfoSerializer, CommentSerializer
  
def index(request):
    return HttpResponse("Hello world!")

class GetNewsView(APIView):
    def get(self, request):
        nums = int(request.query_params.get('nums_of_news'))
        queryset = News.objects.all().order_by('-date', 'title')[:nums]
        # print(request)
        serializer_for_queryset = NewsListSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)
    
    def get_info_by_id(self, request):
        queryset = News.objects.all()
        serializer_for_queryset = NewsInfoSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)

class GetCommentsView(APIView):
    def get(self, request):
        # nums = int(request.query_params.get('nums_of_news'))
        queryset = Comment.objects.all()
        serializer_for_queryset = CommentSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)