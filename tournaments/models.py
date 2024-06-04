from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tournament.name}"


class Schedule(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.tournament.name} - {self.match_date}"


class Result(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def str(self):
        return f'{self.name} - {self.score}'

    class MatchResult(models.Model):
        team1 = models.CharField(max_length=100)
        team2 = models.CharField(max_length=100)
        score1 = models.IntegerField()
        score2 = models.IntegerField()
        date = models.DateField()

        def __str__(self):
            return f"{self.team1} vs {self.team2} on {self.date}"



