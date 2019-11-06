from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bigday.urls'), name='bigday'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('analysis/', include('analysis.urls'), name='analysis'),
]
