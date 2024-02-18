from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
category =[
    ('art', 'Art'),
    ('choreography', 'Choreography'),
    ('drama', 'Drama'),
    ('faith', 'Faith'),
    ('food', 'Food'),
    ('music', 'Music'),
    ('politic', 'Politic'),
    ('sport', 'Sport'),
]
class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length= 100000)
    categoy = models.CharField(max_length=100, choices=category)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title