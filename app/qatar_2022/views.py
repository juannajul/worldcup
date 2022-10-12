from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, '../templates/qatar/index.html')

def pool_matches(request):
    return render(request, '../templates/qatar/pool_matches.html')

def login(request):
    return render(request, '../templates/users/login.html')
