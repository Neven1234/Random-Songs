from django.shortcuts import render
from django.http import HttpResponse


import random
from .models import *

# Create your views here.
def Home(req):
	song=Song.objects.all()
	rand_idx = random.randint(0, len(song)-1)
	Rsong = song[rand_idx]
	if req.method == 'POST':
		contex={'Rsong':Rsong}
	else :
		contex={}
	return render(req,'randomSongs/home.html',contex)

def Suggestions(req):
	if req.method == 'POST':
		Name = req.POST.get('SongName')
		Name=str(Name)
		songObj=songSuggestons.objects.create(name=Name)
		songObj.save()
	return render(req,'randomSongs/suggestions.html')


