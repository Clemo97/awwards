from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import Project, UserUpdateForm, ProfileUpdateForm, SignUpForm, NewProjectForm
from django.contrib import messages
from .models import Profile, Project
from rest_framework import status


@login_required(login)