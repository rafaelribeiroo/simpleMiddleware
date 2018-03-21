from django.urls import path
from .views import (
    home,
)

app_name = 'apps.middleware'
urlpatterns = [
    path('', home, name='homepage'),
]
