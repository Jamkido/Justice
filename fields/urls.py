from django.urls import path
from .views import Fields


app_name = 'areas'

urlpatterns = [
    path('',Fields, name='fields')
]