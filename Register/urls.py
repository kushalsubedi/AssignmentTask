from django.urls import path
from . import views

app_name = 'Register'
urlpatterns = [
    path('', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout')
]
