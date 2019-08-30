from django.urls import path
from . import views
app_name = 'regandloginapp'
urlpatterns=[
    path('home', views.home),
    path('reg', views.reg),
    path('login', views.login),
]