from django.urls import path
from views import *

urlpatterns = [
    path('info', search_info, name='info'),
    path('vuls', search_vuls, name='vuls'),
]
