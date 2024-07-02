from django.contrib import admin
from django.urls import path
# from django.contrib.auth import views as auth
from user.views import login_user
urlpatterns = [
    path('login/',login_user,name='login')
]

# from django.urls import path
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path("login/",auth_views.LoginView.as_view(template_name="user/login.html"))
# ]