from django.urls import path
from .views import *


urlpatterns = [
    path('user-information/<str:name>', UserInformation.as_view(), name='user-information'),
]
