from django.db import models

# Create your models here.
# 클래스 명 convention 파스칼 케이스로 만듬
class Product(models.Model):
    name = models.CharField(max_length=100)    
    desciption = models.TextField() 
    price = models.IntegerField() 
    is_published = models.BooleanField() 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)