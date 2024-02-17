from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News
from .serializers immport NewsSerializer
# Create your views here.

clas NewsListCreateView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=201)
        return response(serializer.error, status=400)