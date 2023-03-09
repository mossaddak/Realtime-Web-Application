from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('create_account/', views.CreateAcoount, name="create_account"),
    path('login/', views.Login, name="login"),
    path('logout/', views.Logout, name="logout"),
    path('messaging/<int:pk>/', views.Messaging, name="messaging"),
    #path('messagesend/<int:pk>/<str:messages>/', views.SendMessage, name='messagesend'),
    path('messagesend/<int:pk>/', views.SendMessage, name='messagesend'),
    path('GetMessage/<int:pk>/', views.GetMessage, name="GetMessage"),

    #get user-------------
    path('GetUser/', views.GetUser, name="GetUser"),

]
