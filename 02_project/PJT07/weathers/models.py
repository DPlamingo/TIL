from django.db import models

# 저장하도록 models.py 를 지정
class Weather(models.Model):
    # 온도(기본값 : 켈빈(K))
    temp = models.FloatField()
    # 체감온도(기본값: 켈빈(K))
    feels_like = models.FloatField()
    # 데이터 측정시간
    dt_txt = models.DateTimeField()