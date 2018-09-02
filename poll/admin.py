from django.contrib import admin
from .models import Question, GameLog

# Register your models here.
admin.site.register(Question)
admin.site.register(GameLog)