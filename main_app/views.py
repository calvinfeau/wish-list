from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Wish

def home(request):
    wish = Wish.objects.all()
    return render(request, 'home.html', {'wish': wish})

class WishCreate(CreateView):
    model = Wish
    fields = ['description']
    success_url = '/'

class WishDelete(DeleteView):
    model = Wish
    success_url = '/'
