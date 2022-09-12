from django.urls import path
from .import views

urlpatterns=[
    path('register/',views.register,name='signup' ),
    path('login/',views.Login,name='login'),
     path('profile/',views.user_profile,name='profile'),
    path('logout/', views.user_logout, name='logout')

]