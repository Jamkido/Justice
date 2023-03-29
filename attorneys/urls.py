from django.urls import path
from .views import index, attorneys, single

app_name = 'huquqshunoslar'

urlpatterns = [
    path('',index, name='home' ),
    path('attorneys/',attorneys, name='attorneys'),
    path('detail/<int:pk>/', single, name='single'),
]

