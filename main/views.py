from django.contrib.auth import authenticate, login as login_, logout as logout_
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Genre, Book

# Create your views here.
def index(request):
	return render(request, 'main/index.html', {
		'genres': Genre.objects.all(),
	})

def genre(request, genre_id):
	return render(request, 'main/genre.html', {
		'genre': Genre.objects.get(id=genre_id),
		'books': Book.objects.filter(genre_id=genre_id),
		'genres': Genre.objects.all()
	})

def book(request, book_id):
	return render(request, 'main/book.html', {
		'book': Book.objects.get(id=book_id),
		'genres': Genre.objects.all()
	})

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login_(request, user)
			return HttpResponseRedirect(reverse('index'))
		else:
			return render(request, 'main/login.html', {
				'message': 'Invalid credentials',
				'genres': Genre.objects.all()
			})
	return render(request, 'main/login.html', {
		'genres': Genre.objects.all()
	})

def logout(request):
	logout_(request)
	return HttpResponseRedirect(reverse('index'))

def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login_(request, user)
			return HttpResponseRedirect(reverse('index'))
	else:
		form = UserCreationForm()
	return render(request, 'main/signup.html', {
		'form': form,
		'genres': Genre.objects.all()
	})