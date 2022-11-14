import requests
from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser
from users.permissions.user_authentication import user_login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from worldcup.models.worldcup_matches import WorldcupMatch
from worldcup.models.worldcup_key_matches import WorldcupKeyMatch
from worldcup.models.worldcup_pools import WorldcupPool
from worldcup.models.worldcup_key_matches import WorldcupKeyMatch


class IndexView(TemplateView):
    template_name = '../templates/qatar/index.html'

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        r_key_matches = WorldcupKeyMatch.objects.filter(started=True, finished=False)
        context['started_key_matches'] = r_key_matches
        r = WorldcupMatch.objects.filter(started=True, finished=False)
        context['started_matches'] = r
        groups = ["A", "B", "C", "D", "E", "F", "G", "H"]
        pools_number = WorldcupPool.objects.all().count()
        reward = pools_number * 10
        context['reward'] = reward
        context['groups'] = groups
        return context

class PoolMatchesView(TemplateView):
    template_name = '../templates/qatar/pool_matches.html'

class LoginView(TemplateView):
    template_name = '../templates/users/login.html'

class SignupView(TemplateView):
    template_name = '../templates/users/signup.html'

#@method_decorator(user_login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = '../templates/users/profile.html'

#@method_decorator(user_login_required, name='dispatch')
class RetrievePoolView(TemplateView):
    template_name = '../templates/qatar/retrieve_pool.html'

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        group_round_finished = False
        context['group_round_finished'] = group_round_finished
        """last_match = WorldcupMatch.objects.get(match_number=48)
        first_key_match = WorldcupKeyMatch.objects.get(match_number=49)
        if last_match.finished:
            group_round_finished = True
            context['group_round_finished'] = group_round_finished
        else:
            context['group_round_finished'] = group_round_finished
        if first_key_match.started:
            group_round_finished = False
            context['group_round_finished'] = group_round_finished"""
        groups = ["A", "B", "C", "D", "E", "F", "G", "H"]
        context['groups'] = groups
        """ pool_id = self.kwargs['id']
        pool = WorldcupPool.objects.get(pk=pool_id)
        group_round_finished = pool.group_analized
        if group_round_finished == False:
            token = 'Token ac035ea97f8471496bf749184f1ed5e85b4ff768'
            headers = {'Authorization': token}
            r = requests.patch(f'http://127.0.0.1:8000/api/worldcup/pool_group_teams/{pool_id}/analize_pool_group_matches/', headers=headers)"""
        return context

#@method_decorator(user_login_required, name='dispatch')
class RetrievePoolKeyView(TemplateView):
    template_name = '../templates/qatar/pool_key_matches.html'

class RankingsView(TemplateView):
    template_name = '../templates/qatar/rankings.html'

class RetrieveRakingPoolView(TemplateView):
    template_name = '../templates/qatar/ranking_pool_retrieve.html'
    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        groups = ["A", "B", "C", "D", "E", "F", "G", "H"]
        context['groups'] = groups
        return context

class InfoView(TemplateView):
    template_name = '../templates/qatar/info.html'

#@method_decorator(user_login_required, name='dispatch')
class ManageMatchesView(TemplateView):
    template_name = '../templates/qatar/manage_matches.html'
