from django.urls import path
from . import views

'''
app_name과 pattern_name은 왜 정의해 주는가?
1. 하드코딩을 피하기 위해서 -> 수정사항 발생시 손으로 일일히 다 바꿔준느일..
ex) print('반갑습니다') * 13095810958
-> 일하다보니까 반갑습니다 말고, 다른 문자가 출력되야 하는디..
코드 돌아다니면서 13095810958 개의 print문 손으로 수정해야함...

hello = '반갑습니다'
print(hello) * 13095810958
-> 일하다보니까 반갑습니다 말고, 다른 문자를 출력해야 되면?
hello = '밥먹으러 갑시다.'
'''


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]