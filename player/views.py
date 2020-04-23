from django.shortcuts import render
from gameplay.models import Game
def home(request):
    my_games=Game.objects.game_for_user(request.user)
    active_game=my_games.active()
    return render(request,"players/home.html", {'games' : Game.objects.all()})
