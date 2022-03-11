from django.shortcuts import render
from .models import Subscriptions, Profile
from django.views.generic import ListView, DetailView


class subscriptions_user(ListView):
    model = Subscriptions
    template_name = 'subscriptions_list.html'


class Main_page_sub(ListView):
    model = Profile
    template_name = 'profile_list.html'