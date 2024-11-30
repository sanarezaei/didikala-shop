from django.urls import path 

from .views import login_user, register, logout

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]

