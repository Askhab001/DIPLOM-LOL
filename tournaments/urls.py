from django.urls import path
from .views import select_tournament, tournament_detail, register
from . import views

urlpatterns = [
    path('', views.TournamentListView.as_view(), name='tournament_list'),
    path('create/', views.TournamentCreateView.as_view(), name='tournament_create'),
    path('<int:pk>/', views.TournamentDetailView.as_view(), name='tournament_detail'),
    path('<int:pk>/update/', views.TournamentUpdateView.as_view(), name='tournament_update'),
    path('<int:pk>/delete/', views.TournamentDeleteView.as_view(), name='tournament_delete'),
    path('<int:pk>/register/', views.ParticipantCreateView.as_view(), name='participant_register'),
    path('<int:pk>/schedule/', views.ScheduleListView.as_view(), name='schedule_list'),
    path('<int:pk>/result/', views.ResultCreateView.as_view(), name='result_create'),
    path('select_tournament/', select_tournament, name='select_tournament'),
    path('<int:tournament_id>/', tournament_detail, name='tournament_detail'),
    path('register/', register, name='register')
]
