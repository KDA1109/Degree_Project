from django.urls import path
from goodsapp import views


app_name = 'goodsapp'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]
