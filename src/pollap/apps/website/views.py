from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect
from django.urls import reverse

class LandingView(TemplateView):
    template_name = "website/index.html"


class UserCreateView(CreateView):
    template_name = 'website/signup.html'
    form_class = UserCreationForm
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        
        context['message'] = "Welcome"
        return context

    def get_success_url(self):
        return reverse('website:signup')
        
