from django.shortcuts import render
# from world .models import world

def home(request):
    return render(request, 'home.html')