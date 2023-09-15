from django.db import models

# Create your models here.
# 파이썬 클래스 정의 -> 아이디어 스케치
class Garage(models.Model):
    # id 컬럼은 직접 정의 안한다.
    # 주소
    location = models.CharField(max_length=200)
    # 용량
    capacity = models.IntegerField()
    # 주차 가능 여부
    is_parking_avaliable = models.BooleanField()
    # 여는 시간/ 닫는시간
    opening_time = models.TimeField()
    closing_time = models.TimeField()

garages = Garage.objects.all()
print(garages)

garage = Garage()
garage.location = '부산시 강서구'
garage.capacity = 10
garage.is_parking_avaliable = True
garage.opening_time = '07:00'
garage.closing_time = '23:00'
# print(garage.location)
garage.save()

garage_2 = Garage.objects.create(location = '경상남도 창원시',
                       capacity=20,
                       is_parking_avaliable = False,
                       opening_time='07:00',
                       closing_time = '23:00',
                       
                       )