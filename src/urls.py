from django.contrib import admin
from django.urls import path, include

from src.apps.middlewares import urls as middlewares_urls

app_name = 'core'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(middlewares_urls, namespace='middleware')),
]
