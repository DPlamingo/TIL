from django.shortcuts import render
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
csv_path = 'weathers/data/austin_weather.csv'


# Create your views here.
def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df': df,
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    df = pd.read_csv(csv_path)
    plt.clf()
    df['Date'] = pd.to_datetime(df['Date'])
    plt.plot(df['Date'], df['TempHighF'], label='High Temperature')
    plt.plot(df['Date'], df['TempAvgF'], label='Avg Temperature')
    plt.plot(df['Date'], df['TempLowF'], label='Low Temperature')
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.legend(bbox_to_anchor=(0.3, 0.22))
    buffer = BytesIO()

    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    # x = [1, 2, 3, 4]
    # y = [2, 4, 8, 16]
    # # 다른 View 함수에서 plt 를 이미 그린 상태에서
    # # 다시 그리는 경우를 대비하여, 초기화를 진행
    # plt.clf()

    # plt.plot(x, y)
    # plt.title("Graph")
    # plt.ylabel('y label')
    # plt.xlabel('x label')

    # # 비어있는 버퍼를 생성
    # buffer = BytesIO()

    # # 버퍼에 그래프를 저장
    # plt.savefig(buffer, format='png')

    # # 버퍼의 내용을 base64 로 인코딩
    # image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    
    # # 버퍼를 닫아줌
    # buffer.close()

    # # 이미지를 웹 페이지에 표시하기 위해
    # # URI 형식(주소 형식)으로 만들어진 문자열을 생성
    # context = {
    #     # chart_image: 저장된 이미지의 경로
    #     'chart_image': f'data:image/png;base64,{image_base64}',
    # }
    
    return render(request, 'problem2.html', context)

def problem3(request):
    return render(request, 'problem3.html')

def problem4(request):
    return render(request, 'problem4.html')


