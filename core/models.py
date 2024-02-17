from django.db import models
from datetime import datetime
# Create your models here.
category =[
    ('art' 'Art'),
    ('dhoreographyy', 'Choreography'),
    ('drama', 'Drama'),
    ('Faith', 'Faith'),
    ('Food', 'Food'),
    ('Music', 'Music'),
    ('politic', 'politic'),
    ('sport', 'sport'),
]
class News(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length= 100000)
    categoy = models.ChoiceField(category, choices=category)
    created_at = models.datetime(auto_now=True)

    def __str__(self):
        return self.title