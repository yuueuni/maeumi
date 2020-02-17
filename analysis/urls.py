from django.urls import path
from analysis import views

app_name = 'analysis'

urlpatterns = [
    path('getPic/', views.getPic),
    path('inputImage/', views.inputImage, name='inputImage'),
]