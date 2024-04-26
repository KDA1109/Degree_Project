from django.urls import path
from ordersapp import views


app_name = 'ordersapp'

urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
    
] 
