from django.urls import path
from cartsapp import views


app_name = 'cartsapp'

urlpatterns = [
    path('add/<slug:product_slug>/', views.cart_add, name='add'),
    path('change/<slug:product_slug>/', views.cart_change, name='change'),
    path('remove/<int:cart_id>/', views.cart_remove, name='remove'),
] 
