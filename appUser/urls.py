from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.appUser_form),
    path('list/', views.appUser_list),

]