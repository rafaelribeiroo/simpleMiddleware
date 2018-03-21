from django.shortcuts import render


def home(request):
    context = {
        'name': 'Rafael'
    }
    return render(request, 'home.html', context)
