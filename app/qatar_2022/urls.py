from django.urls import path

from . import views

app_name = 'qatar_2022'

urlpatterns = [
    path('', views.index, name='index'),
    path('pool_matches/', views.pool_matches, name='pool_matches'),
    path('login/', views.login, name='login'),
]