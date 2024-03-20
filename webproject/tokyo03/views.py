from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from .models import Special

class Listtokyo03View(ListView):
    template_name = 'tokyo03/index.html'
    model = Special

class RecommendationView(DetailView):  
    template_name = 'tokyo03/recommendation.html'
    model = Special
