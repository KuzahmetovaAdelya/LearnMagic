from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='startPage'),
    path('auth', views.auth, name='auth'),
    path('reg', views.reg, name='reg'),
    path('desktop-child', views.desktopChild, name='desktop-child'),
    path('desktop-pup', views.desktopPup, name='desktop-pup'),
    path('games-child', views.gamesPageChild, name='games-child'),
    path('games-pup', views.gamesPagePup, name='games-pup'),
    path('child-game-one', views.childGameOne, name='child-game-one'),
    path('child-game-two', views.childGameTwo, name='child-game-two'),
    path('pup-game-one', views.pupGameOne, name='pup-game-one'),
    path('pup-game-two', views.pupGameTwo, name='pup-game-two'),
    path('exit', views.exit, name='exit'),
]