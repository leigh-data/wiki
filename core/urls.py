from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('encyclopedia.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('pages/', include('pages.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
