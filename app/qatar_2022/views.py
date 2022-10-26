import requests
from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser
from users.permissions.user_authentication import user_login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = '../templates/qatar/index.html'

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        r = requests.get('http://127.0.0.1:8000/api/worldcup/worldcup_matches/get_started_matches/')
        context['started_matches'] = r.json()
        groups = ["A", "B", "C", "D", "E", "F", "G", "H"]
        context['groups'] = groups
        return context

class PoolMatchesView(TemplateView):
    template_name = '../templates/qatar/pool_matches.html'

class LoginView(TemplateView):
    template_name = '../templates/users/login.html'

class SignupView(TemplateView):
    template_name = '../templates/users/signup.html'

@method_decorator(user_login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = '../templates/users/profile.html'

@method_decorator(user_login_required, name='dispatch')
class RetrievePoolView(TemplateView):
    template_name = '../templates/qatar/retrieve_pool.html'
