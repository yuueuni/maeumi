from django.urls import path
from bigday import views

app_name = 'bigday'

urlpatterns = [
    path('', views.home, name='home'),
    path('testView/', views.testView, name='testView'),
]