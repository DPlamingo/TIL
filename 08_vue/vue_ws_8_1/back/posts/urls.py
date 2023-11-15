from django.urls import path
from . import views

urlpatterns = [
    path('categories/',views.category_list),
    path('posts/', views.post_list_created),
    path('posts/<int:post_pk>/', views.post_detail_update_delete)
]
