from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def appUser_list(request):
    return render(request, "appUser/appUser_List.html")


def appUser_form(request):
    form = UserForm()
    return render(request, "appUser/appUser_form.html", {'form': form})


def appUser_delete(request):
    return render(request, "appUser/appUser_delete.html")