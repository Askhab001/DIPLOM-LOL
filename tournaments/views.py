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


class TournamentCreateView(CreateView):
    model = Tournament
    fields = ['name', 'description', 'start_date', 'end_date', 'location']
    template_name = 'tournaments/tournament_form.html'
    success_url = reverse_lazy('tournament_list')


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


