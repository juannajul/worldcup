from django.urls import path

from .views import IndexView, PoolMatchesView, LoginView, ProfileView, RetrievePoolView, SignupView, ManageMatchesView, RetrievePoolKeyView, RankingsView, InfoView, RetrieveRakingPoolView


app_name = 'qatar_2022'

urlpatterns = [
    #path('', views.index, name='index'),
    #path('pool_matches/', views.pool_matches, name='pool_matches'),
    #path('login/', views.login, name='login'),
    path('', IndexView.as_view(), name='index'),
    path('pool_matches/', PoolMatchesView.as_view(), name='pool_matches'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('retrieve_pool/<int:id>/', RetrievePoolView.as_view(), name='retrieve_pool'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('manage_matches/', ManageMatchesView.as_view(), name='manage_matches'),
    path('pool_key_matches/<int:id>/', RetrievePoolKeyView.as_view(), name='pool_key_matches'),
    path('rankings/', RankingsView.as_view(), name='rankings'),
    path('info/', InfoView.as_view(), name='info'),
    path('retrieve_pool_ranking/<int:id>/', RetrieveRakingPoolView.as_view(), name='retrieve_pool_ranking'),
]