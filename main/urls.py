from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('genre/<int:genre_id>', views.genre, name='genre'),
	path('book/<int:book_id>', views.book, name='book'),
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('signup', views.signup, name='signup')
]