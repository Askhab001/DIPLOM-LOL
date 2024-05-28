from django import forms
from .models import Tournament
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TournamentSelectionForm(forms.Form):
    tournament = forms.ModelChoiceField(queryset=Tournament.objects.all(), empty_label="Select a tournament")


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
