from django.urls import path
from .views import services_view

app_name = 'services'


urlpatterns = [
    path('', services_view, name='services')
]