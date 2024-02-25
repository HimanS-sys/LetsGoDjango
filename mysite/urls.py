"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp.views import welcome
from myapp.views import hello_world
from myapp.views import profile_view
from myapp.views import get_profile_by_name
from myapp.views import update_email
from myapp.views import profile_view_json
from myapp.views import profile_detail_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", welcome, name = "welcome"),
    path("hello/", hello_world, name = "hello"),
    path("name/", profile_view, name = "profile"),
    path("profiles/", profile_view_json, name = "profile_view_json"),
    path("profiles/<int:pk>/", profile_detail_view, name = "profile_detail_view"),
    path("profile/<str:name>/", get_profile_by_name, name = "get_profile_by_name"),
    path("profile/<str:name>/email/", update_email, name = "update_email"),
]
