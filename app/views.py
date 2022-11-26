from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


@login_required
def secret_page(request):
    return render(request, 'secret.html')
