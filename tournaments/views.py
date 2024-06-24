from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,  reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Tournament, Participant, Schedule, Result
from .forms import TournamentSelectionForm, UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


class LoginView(LoginView):
    template_name = 'accounts/login.html'


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)


class TournamentListView(ListView):
    model = Tournament
    template_name = 'tournaments/tournament_list.html'

from .forms import TournamentForm
@login_required
def create_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.creator = request.user
            tournament.save()
            return redirect(reverse_lazy('tournament_list'))
    else:
        form = TournamentForm()
    return render(request, 'tournaments/tournament_form.html', {'form': form})



class TournamentDetailView(DetailView):
    model = Tournament
    template_name = 'tournaments/tournament_detail.html'


class TournamentUpdateView(UpdateView):
    model = Tournament
    fields = ['name', 'description', 'start_date', 'end_date', 'location']
    template_name = 'tournaments/tournament_form.html'
    success_url = reverse_lazy('tournament_list')


class TournamentDeleteView(DeleteView):
    model = Tournament
    success_url = reverse_lazy('tournament_list')
    template_name = 'tournament/delete_tournaments.html'


class ParticipantCreateView(CreateView):
    model = Participant
    fields = ['user', 'tournament']
    template_name = 'tournaments/participant_form.html'
    success_url = reverse_lazy('tournament_list')


class ScheduleListView(ListView):
    model = Schedule
    template_name = 'tournaments/schedule_list.html'



def ResultCreateView(request):
    results = Result.objects.all()

    return render(request, 'tournaments/result_form.html', {'results': results})

def select_tournament(request):
    if request.method == 'POST':
        form = TournamentSelectionForm(request.POST)
        if form.is_valid():
            selected_tournament = form.cleaned_data['tournament']

            return redirect('tournament_detail', tournament_id=selected_tournament.id)
    else:
        form = TournamentSelectionForm()
    return render(request, 'tournaments/select_tournament.html', {'form': form})


def tournament_detail(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    return render(request, 'tournaments/tournament_detail.html', {'tournament': tournament})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправляем пользователя на страницу входа после успешной регистрации
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def delete_tournament(request, tournament_id):
    tournament = Tournament.objects.get(pk=tournament_id)
    if request.method == 'POST':
        tournament.delete()
        return redirect('tournament_list')
    context = {'tournament': tournament}
    return render(request, 'tournaments/delete_tournament.html', context)

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ParticipantForm

@login_required
def add_team_to_tournament(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tournament_list')
    else:
        form = ParticipantForm()
    return render(request, 'tournaments/add_team_to_tournament.html', {'form': form})

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TeamForm, PlayerForm
from .models import Team

@login_required
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)  # Сначала не сохраняем команду, добавляем создателя
            team.user = request.user  # Устанавливаем создателя команды
            team.save()  # Теперь сохраняем команду
            return redirect('add_player_to_team', team_id=team.id)
    else:
        form = TeamForm()
    return render(request, 'tournaments/create_team.html', {'form': form})
@login_required
def add_player_to_team(request, team_id):
    team = Team.objects.get(id=team_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.team = team
            player.save()
            return redirect('add_player_to_team', team_id=team.id)
    else:
        form = PlayerForm()
    return render(request, 'tournaments/add_player_to_team.html', {'form': form, 'team': team})


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tournament, Schedule, Result
from .forms import ResultForm

@login_required
def set_score(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    tournament = schedule.tournament
    if request.user != tournament.creator:
        return render(request, '403.html')  # Возвращаем страницу с ошибкой доступа, если пользователь не создатель турнира

    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.match = schedule
            result.save()
            return redirect('tournament_detail', pk=tournament.pk)
    else:
        form = ResultForm()
    return render(request, 'tournaments/set_score.html', {'form': form, 'schedule': schedule})


# views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Team, Participant, Result, Tournament


@login_required
def view_team_results(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    # Убедимся, что пользователь имеет право видеть результаты этой команды
    if request.user != team.user:
        return render(request,
                      '403.html')  # Возвращаем страницу с ошибкой доступа, если пользователь не владелец команды

    # Получаем все турниры, в которых участвовала команда
    tournaments = Tournament.objects.filter(participant__team=team).distinct()
    results = Result.objects.filter(team=team).select_related('match').order_by('-match__match_date')

    context = {
        'team': team,
        'tournaments': tournaments,
        'results': results
    }
    return render(request, 'tournaments/team_results.html', context)
