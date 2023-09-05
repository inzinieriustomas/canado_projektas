from django.urls import path
from . import views


app_name = 'car'
urlpatterns = [

    path('add_car', views.add_car, name='add_car'),
    path('car_list', views.car_list, name='car_list'),


]



