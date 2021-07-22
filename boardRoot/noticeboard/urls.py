from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'gun'

urlpatterns = [
    path('', views.index, name='index'),
    path('unemployment/', views.unemployment, name='unemployment'),
    path('race/', views.race, name='race'),
    path('intro/', views.intro, name='intro'),
    path('result/', views.result, name='result'),
    path('poverty/', views.poverty, name='poverty'),
]
