from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse
from .serializers import WeatherSerializer
import requests
from .models import Weather

# Create your views here.
@api_view(['GET'])
def index(request):
    # 내 PC에만 저장, github에 안올릴래
    # 프로젝트 만의 환경변수 (장고 environ 으로 저장가능)
    api_KEY = settings.API_KEY
    city = 'Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_KEY}'
    
    response = requests.get(url).json()

    return Response(response)

@api_view(['GET'])
def save_data(request):
    api_KEY = settings.API_KEY
    city = 'Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_KEY}'
    
    response = requests.get(url).json()

    for li in response.get('list'):
        save_data = {
            'dt_txt' : li.get('dt_txt'),
            'temp' : li.get('main').get('temp'),
            'feels_like' : li.get('main').get('feels_like'),
            
        }
        # 저장하기 위해 데이터를 포장
        serializer = WeatherSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 저장완료 메세지        
    return JsonResponse({ 'massage': 'okay' })

@api_view(['GET'])
def list_data(request):
    # weathers 는 데이터가 아니고, query Set임
    weathers = Weather.objects.all()
    serializer = WeatherSerializer(weathers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def hot_weathers(request):
    weathers = Weather.objects.all()
    hot_weathers = []
    for weather in weathers:
        # 섭씨 = 켈빌 - 273.15
        tmp = round(weather.temp - 273.15, 2)
        if tmp > 10:
            hot_weathers.append(weather)
    serializer = WeatherSerializer(hot_weathers, many=True)
    return Response(serializer.data)