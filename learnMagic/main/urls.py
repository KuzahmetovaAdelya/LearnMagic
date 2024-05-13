from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='startPage'),
    path('auth', views.auth, name='auth'),
    path('reg', views.reg, name='reg'),
    path('desktop', views.desktop, name='desktop'),
    path('games', views.gamesPage, name='games'),

]