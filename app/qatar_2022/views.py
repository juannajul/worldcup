from urllib import request
from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser
from users.permissions.user_authentication import user_login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

# Create your views here.

# @method_decorator(user_login_required)
# def index(request):
#     user = request.user
#     authenticated = True
#     print(user)
#     print(request)
#     token = request.COOKIES.get('access_token')
#     if token:
#         authenticated = True
#     else:
#         authenticated = False
#         return render(request, '../templates/users/login.html')
    
#     return render(request, '../templates/qatar/index.html')

# def pool_matches(request):
#     return render(request, '../templates/qatar/pool_matches.html')

# def login(request):
#     return render(request, '../templates/users/login.html')

class IndexView(TemplateView):
    template_name = '../templates/qatar/index.html'

class PoolMatchesView(TemplateView):
    template_name = '../templates/qatar/pool_matches.html'

class LoginView(TemplateView):
    template_name = '../templates/users/login.html'

@method_decorator(user_login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = '../templates/users/profile.html'

@method_decorator(user_login_required, name='dispatch')
class RetrievePoolView(TemplateView):
    template_name = '../templates/qatar/retrieve_pool.html'
