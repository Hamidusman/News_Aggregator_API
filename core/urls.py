from django.urls import path
from .views import NewsList, NewsDetail

urlpatterns = [
    path('news', NewsList.as_view(), name='news'),
    path('article/<str:pk>', NewsDetail.as_view(), name='article')
]
