from django.urls import path
from .views import select_tournament, tournament_detail, ResultCreateView, TournamentDeleteView
from . import views
from django.contrib.auth import views as auth_views
from .views import add_team_to_tournament, create_team, add_player_to_team, set_score, view_team_results

urlpatterns = [
    path('', views.TournamentListView.as_view(), name='tournament_list'),
    path('create/', views.create_tournament, name='tournament_create'),
    path('<int:pk>/', views.TournamentDetailView.as_view(), name='tournament_detail'),
    path('<int:pk>/update/', views.TournamentUpdateView.as_view(), name='tournament_update'),
    path('<int:tournament_id>/delete/', views.delete_tournament, name='delete_tournament'),
    path('<int:pk>/register/', views.ParticipantCreateView.as_view(), name='participant_register'),
    path('<int:pk>/schedule/', views.ScheduleListView.as_view(), name='schedule_list'),
    path('select_tournament/', select_tournament, name='select_tournament'),
    path('<int:tournament_id>/', tournament_detail, name='tournament_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('result/', ResultCreateView, name='result_form'),
    path('add-team-to-tournament/', add_team_to_tournament, name='add_team_to_tournament'),
    path('create-team/', create_team, name='create_team'),
    path('add-player-to-team/<int:team_id>/', views.add_player_to_team, name='add_player_to_team'),
    path('set-score/<int:schedule_id>/', set_score, name='set_score'),
    path('team-results/<int:team_id>/', view_team_results, name='team_results'),

]
