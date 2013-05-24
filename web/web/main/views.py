from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.dispatch import receiver
from django_browserid import signals

def login(request):
    return render(request, 'main/login.html')


def login_failed(request):
    return render(request, 'main/login_failed.html')

@login_required
def home(request):
    return render(request, 'main/home.html')


@receiver(signals.user_created)
def user_created(sender, user, **kwargs):
    user.is_active = False
    user.save()
