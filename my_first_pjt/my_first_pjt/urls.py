from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main:index'),
    path('search/', views.search, name='search:search'),
    # ... 다른 URL 패턴 추가
]
