from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('encyclopedia.urls')),
    path('goaway/', admin.site.urls),
]
