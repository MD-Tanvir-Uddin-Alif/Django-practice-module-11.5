from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('practice/',views.practice,name='practice'),
]