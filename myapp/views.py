from django.shortcuts import render
from myapp.models import Game

# Create your views here.
def games_list_view(request):
    all_games = Game.objects.all()
    context = {
        "games": all_games
    }
    return render(
        request,
        template_name="games.html",
        context=context,
    )
def get_game_by_id(request, game_id):
    game = Game.objects.get(id = game_id)
    context = {
        "game": game
    }
    return render(
        request,
        template_name="game_details.html",
        context=context
    )