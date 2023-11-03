from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import pandas as pd
import numpy as np
import csv

array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)


@api_view(['GET'])
def file_open(request):
    df = pd.read_csv('data/test_data.CSV', encoding='cp949')
    data = df.to_dict('records')

    return JsonResponse({ 'dat': data })


@api_view(['GET'])
def data_return(request):
    df = pd.read_csv('data/test_data_has_null.CSV', encoding='cp949')
    data = df.fillna('Null', inplace=True)
    
    data = df.to_dict('records')
    return JsonResponse({'dat': data})


@api_view(['GET'])
def find_similar_ages(request):
    # CSV 파일을 읽어 DataFrame을 만듬.
    df = pd.read_csv('data/test_data.CSV', encoding='cp949')

    # '나이' 필드의 평균값을 계산 (결측치를 제외한).
    average_age = df['나이'].mean()

    # '나이'와 평균 나이 간의 차이를 계산함.
    df['차이'] = abs(df['나이'] - average_age)

    # 차이를 기준으로 DataFrame을 정렬
    df = df.sort_values(by='차이')

    # 가장 비슷한 10개 행을 선택
    similar_ages = df.head(10)

    # 필요에 따라 결과를 JSON 형식으로 반환
    similar_ages_json = similar_ages.to_dict('records')
    return JsonResponse({'similar_ages': similar_ages_json})
