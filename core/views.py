from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters, generics
from .models import News
from .serializers import NewsSerializer
# Create your views here.

class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']


    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title')
        content = self.request.query_params.get('content')

        if title:
            queryset = queryset.filter(title__icontains = title)
        if content:
            queryset = queryset.filter(content__icontains = content)
        
        return queryset

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer