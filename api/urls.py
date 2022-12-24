"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
urlpatterns = [
    path('',views.FrontPage),
    path('get_all_data',views.GetData),
    path('check_user_already_login',views.UserAlreadyInside),
    path('get_already_login_user',views.get_already_login_user),
    path('create_new_note',views.create_new_note),
    path('login_user',views.LoginUser),
    path('regester_new_user',views.RegesterNewUser),
    path('get_a_note/<str:id>',views.GetANote),
    path('delete_a_note/<str:id>',views.DeleteANote),
    path('update_note/<str:id>',views.update_a_note),
]
