from django.urls import path
from . import views

urlpatterns = [
    path('normal_sort/', views.normal_sort),
    path('priority_queue/', views.priority_queue),
    path('bubble_sort/', views.bubble_sort),
    path('file_open/', views.file_open),
    path('data_return/', views.data_return),
    path('find_similar_ages/', views.find_similar_ages),
]

