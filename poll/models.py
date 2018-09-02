from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	def __str__(self):
		return self.question_text;
	
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days = 1);
	
	question_text = models.CharField(max_length = 200);
	pub_date = models.DateTimeField('data published');
	
class Choice(models.Model):
	def __str__(self):
		return self.choice_text;
	
	question = models.ForeignKey(Question, on_delete=models.CASCADE);
	choice_text = models.CharField(max_length = 200);
	votes = models.IntegerField(default=0);
	
class GameLog(models.Model):
	def __str__(self):
		return self.player_name + ': ' + self.date.strftime('%Y-%m-%d %H:%M')
	
	playerName = models.CharField(max_length = 30);
	playerClass = models.CharField(max_length = 30, blank=True);
	playerLevel = models.IntegerField(default=0);
	time = models.CharField(max_length=30, blank=True);						
	date = models.DateTimeField('date', blank=True);
	text = models.CharField(max_length = 300, blank=True);
	zoneName = models.CharField(max_length = 30, blank=True);
	zoneLevel = models.IntegerField(default=0);
	