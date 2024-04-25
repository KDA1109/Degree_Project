from django.urls import path
from cartsapp import views


app_name = 'cartsapp'

urlpatterns = [
    path('add/', views.cart_add, name='add'),
    path('change/', views.cart_change, name='change'),
    path('remove/', views.cart_remove, name='remove'),
] 
