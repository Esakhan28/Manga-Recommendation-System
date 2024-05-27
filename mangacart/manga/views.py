from django.http import HttpResponse
from django.template import loader
from .models import Mangacard
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib import messages
from .scripts.popular_recommendations import get_popular_books
from .scripts.prerecommendation import recommend

@login_required
def members(request):
  query = request.GET.get('search','')
  filter_type = request.GET.get('filter', '')
  query = request.GET.get('search', '')
  if query:
      search_results = Mangacard.objects.filter(title__icontains=query)
      return render(request, 'f1.html', {'books': search_results})
  else:
    if filter_type == 'top10':
            books = get_popular_books()[:10]
    elif filter_type == 'top50':
        books = get_popular_books()
    elif filter_type == 'harryPotter':
        books = Mangacard.objects.filter(author__iexact='J.K. Rowling')
    elif filter_type == 'lotr':
        books = Mangacard.objects.filter(title__iexact='Lord of the rings')
    elif filter_type == 'danBrown':
        books = Mangacard.objects.filter(author__iexact='Dan Brown')
    else:
        books = get_popular_books()
    return render(request, 'f1.html', {'books': books})
  return render(request, 'f1.html', {'books': popular_books_data})

def signup(request):
  return render(request, 'signup.html')

def read(request, title):
  filter_type = request.GET.get('filter', '')
  recommended_books_titles = recommend(title)
  book = Mangacard.objects.filter(title=title).first()
  if recommended_books_titles != 'Book Not Found':
        recommended_books = Mangacard.objects.filter(title__in=recommended_books_titles)
  else:
      recommended_books = []
  popular_books_data = get_popular_books()
  query = request.GET.get('search','')
  if query:
    search_results = Mangacard.objects.filter(title__icontains=query)
    return render(request, 'f1.html', {'books': search_results})
  else:
     if filter_type == 'top10':
            books = get_popular_books()[:10]
     elif filter_type == 'top50':
        books = get_popular_books()
     elif filter_type == 'harryPotter':
        books = Mangacard.objects.filter(author__iexact='J.K. Rowling')
     elif filter_type == 'lotr':
        books = Mangacard.objects.filter(author__iexact='J.R.R Tolkien')
     elif filter_type == 'danBrown':
        books = Mangacard.objects.filter(author__iexact='Dan Brown')
     else:
        books = recommended_books    
  return render(request, 'read.html', {'books': books, 'book':book})

def admin_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username = username, password = password)
    if user is not None:
      if user.is_staff:
        login(request, user)
        return redirect('members')
      else:
        messages.error(request, 'You are not authorized to view this page.')
    else:
      messages.error(request, 'Invalid username or password.')
  return render(request, 'login.html')

def admin_logout(request):
  auth_logout(request)
  return redirect('signup')