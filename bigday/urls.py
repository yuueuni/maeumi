from django.urls import path
from bigday import views


urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('report/', views.report, name='report'),
]