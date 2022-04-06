from django.urls import path
from . import views

#urlConfiguration
urlpatterns = [
   path('hello/', views.say_hello)
]