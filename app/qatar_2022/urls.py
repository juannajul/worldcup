from django.urls import path

from .views import IndexView, PoolMatchesView, LoginView, ProfileView, RetrievePoolView, SignupView


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
    
]