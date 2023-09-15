from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    autor = models.TextField()
    pubdate = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    adult = models.BooleanField()