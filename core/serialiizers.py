from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class meta:
        models = News
        fields = '__all__'