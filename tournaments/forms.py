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


from django import forms
from .models import Tournament

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'description', 'start_date', 'end_date', 'location']


# forms.py
from django import forms
from .models import Team, Tournament, Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['team', 'tournament']
        widgets = {
            'team': forms.Select(attrs={'class': 'form-control'}),
            'tournament': forms.Select(attrs={'class': 'form-control'})
        }
# forms.py
from django import forms
from .models import Team, Player

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'age', 'phone_number']

# forms.py
from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['team', 'score']
        widgets = {
            'team': forms.Select(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control'})
        }
