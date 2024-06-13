from django.urls import path
from .views import select_tournament, tournament_detail, ResultCreateView, TournamentDeleteView
from . import views
from django.contrib.auth import views as auth_views

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


]
