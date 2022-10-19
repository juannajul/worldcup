""" redirect if user is not authenticated. """

# Django
from contextlib import redirect_stderr
from django.shortcuts import render, redirect

def user_login_required(function):
    def wrap(request, *args, **kwargs):
        authenticated = False
        token = request.COOKIES.get('access_token')
        if token:
            authenticated = True
            return function(request, *args, **kwargs)
        else:
            authenticated = False
            return redirect('qatar_2022:login')
    return wrap