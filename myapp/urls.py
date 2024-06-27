from django.urls import path
import myapp.views as ma_views

urlpatterns = [
    path("", ma_views.games_list_view, name = "games"),
    path("<int:game_id>/", ma_views.get_game_by_id, name = "game_details")
]