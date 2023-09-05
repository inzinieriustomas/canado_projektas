from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from works.models import Works

def main_page(request):
    return render(request, 'main_page.html')

def vadybininkui(request):
    works = Works.objects.all()
    return render(request, 'vadybininkui.html', {'works': works})

def dazytojui(request):
    return render(request, 'dazytojui.html')

def mechanikui(request):
    return render(request, 'mechanikui.html')

def saltkalviui(request):
    return render(request, 'saltkalviui.html')

def elektrikui(request):
    return render(request, 'elektrikui.html')

def main_page(request):
    # Čia įrašykite savo vaizdo kodą
    return render(request, 'main_page.html')

# Kitos funkcijos jūsų programai
