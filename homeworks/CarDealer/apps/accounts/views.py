from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import auth, messages
from django.http import HttpResponse


class DemoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello! This is a Demo!'}
        return Response(content)


def logIn(request):
    form = UserLoginForm
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Invalid login. Please try again.')
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

