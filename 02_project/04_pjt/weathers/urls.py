from django.urls import path
from . import views

urlpatterns = [
    path('problem1/', views.problem1),
    path('problem2/', views.problem2),
    path('', views.problem3),
    path('', views.problem4),
    
    
]
