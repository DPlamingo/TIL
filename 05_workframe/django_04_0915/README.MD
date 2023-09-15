# ORM
## 조회
1. ORM -> python Object 다루는법
2. myModel ClassName.manager.QuerySet API
```python
garages = Garage.object.all()
```

## 생성
1. Python Object
2. 객체 하나 생성(인스턴스 생성)
```python
garage = Garage()
garage.location = '부산시 강서구'
garage.capacity = 10
garage.is_parking_avaliable = True
garage.opening_time = '07:00'
garage.closing_time = '23:00'
print(garage.location)
garage.save()

garage_2 = Garage.objects.create(location = '경상남도 창원시',
                       capacity=20,
                       is_parking_avaliable = False,
                       opening_time='07:00',
                       closing_time = '23:00',
                       
                       )
```

## 삭제
1. 삭제 완료 된 경우, 완료된 객체 반환
```python
garage_2.delete()

garages = <querySet []>
```