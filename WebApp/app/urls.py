from django.urls import path
from . import views

urlpatterns = [
    path('',views.req, name='Data Analytics'),
]