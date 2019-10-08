from django.urls import path
from bigday import views


urlpatterns = [
    path('', views.index, name='index'),
]