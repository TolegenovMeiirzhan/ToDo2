from django.urls import path
from .views import *

urlpatterns =[
    path('',index, name='index' ),
    path('add/', add_todo, name = 'add'),
    path('update/<int:pk>', complete_todo, name = 'update' ),
    path('delete/<int:pk>', delete, name = 'delete' )
]