from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('view_movie/<id>',views.view_movie),
    
    
]