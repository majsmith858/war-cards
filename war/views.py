from django.shortcuts import render
from war.models import Player

#This is the index page
def index(request):
    return render(request,'war/index.html')
