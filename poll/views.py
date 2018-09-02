from django.shortcuts import render
from django.http import HttpResponse
from .models import GameLog
from datetime import datetime
from django.utils import timezone
import json

# Create your views here.
def index (request):
	timezone.activate('America/Vancouver')
	
	
	gameLogList = GameLog.objects.order_by('date');
	
	output = '<b>Games:</b><br><br>';
	for gameLog in gameLogList:
		output += gameLog.playerName + ' - ';
		output += gameLog.date.strftime('%Y-%m-%d %H:%M') + ' - ';
		output += gameLog.zoneName + '[';
		output += str(gameLog.zoneLevel) + '] - ';
		output += gameLog.time + ' - '
		output += 'Level ' + str(gameLog.playerLevel) + ' ' + gameLog.playerClass + ' ';
		output += gameLog.text + '.';
		
		output += '<br>';
		
	
	return HttpResponse(output)

def submit (request):
	timezone.activate('America/Vancouver')
	
	data = json.loads(request.body);
	
	gameLog = GameLog(playerName = data['playerName'], date = datetime.now())
	gameLog.text = data['text'];
	gameLog.zoneName = data['zoneName'];
	gameLog.zoneLevel = data['zoneLevel'];
	gameLog.playerClass = data['playerClass'];
	gameLog.playerLevel = data['playerLevel'];
	gameLog.time = data['time'];
	
	gameLog.save();
	
	return HttpResponse("Your response")
	