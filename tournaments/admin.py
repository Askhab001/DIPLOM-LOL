from django.contrib import admin
from .models import Profile,Participant,Schedule, Result

admin.site.register(Profile)
admin.site.register(Participant)
admin.site.register(Schedule)
admin.site.register(Result)
