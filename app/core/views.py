from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse

def index(request):
    return HttpResponseRedirect(reverse('qatar_2022:index'))