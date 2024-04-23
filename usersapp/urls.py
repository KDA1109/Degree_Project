from django.urls import path
from usersapp import views


app_name = 'usersapp'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
] 
