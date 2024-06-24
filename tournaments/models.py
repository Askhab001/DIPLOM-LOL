from django.db import models
from django.contrib.auth.models import User


from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Player(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Team(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Participant(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team.name} - {self.tournament.name}"


class Schedule(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.tournament.name} - {self.match_date}"


class Result(models.Model):
    match = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()
