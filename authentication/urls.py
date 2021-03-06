from django.urls import path, include
from django_cas_ng import views as cas_views
from .views import loginApi, loginView, signupApi, signupView, logoutView

urlpatterns = [
  path('api/login/', loginApi, name='loginapi'),
  path('api/signup/', signupApi, name='signupapi'),
  path('login/', loginView, name='login'),
  path('signup/', signupView, name='signup'),
  path('logout/', logoutView, name='logout'),
  path('loginsso/', cas_views.LoginView.as_view(), name='loginsso'),
  path('logoutsso/', cas_views.LogoutView.as_view(), name='logoutsso'),
]