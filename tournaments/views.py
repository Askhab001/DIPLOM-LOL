from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Tournament, Participant, Schedule, Result
from .forms import TournamentSelectionForm, UserRegistrationForm


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
    template_name = 'tournaments/tournament_confirm_delete.html'
    success_url = reverse_lazy('tournament_list')


class ParticipantCreateView(CreateView):
    model = Participant
    fields = ['user', 'tournament']
    template_name = 'tournaments/participant_form.html'
    success_url = reverse_lazy('tournament_list')


class ScheduleListView(ListView):
    model = Schedule
    template_name = 'tournaments/schedule_list.html'


class ResultCreateView(CreateView):
    model = Result
    fields = ['schedule', 'result']
    template_name = 'tournaments/result_form.html'
    success_url = reverse_lazy('tournament_list')


def select_tournament(request):
    if request.method == 'POST':
        form = TournamentSelectionForm(request.POST)
        if form.is_valid():
            selected_tournament = form.cleaned_data['tournament']
            # Выполните действия с выбранным турниром, например, добавьте его к пользователю
            # Здесь вы можете выполнить логику для участия пользователя в выбранном турнире
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