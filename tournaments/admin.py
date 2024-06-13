from django.contrib import admin
from .models import Profile,Participant,Schedule, Result,Player,Team,Tournament

admin.site.register(Profile)
admin.site.register(Participant)
admin.site.register(Schedule)
admin.site.register(Result)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Tournament)
