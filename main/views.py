from django.shortcuts import render
from .models import Section, Sport, Tech, Music, Politics, Architecture


def main_pg(request):
    sections = Section.objects.all()
    return render(request, 'main/index.html', {'section':sections})

def sport_pg(request):
    articles = Sport.objects.all()
    return render(request, 'main/sport.html', {'i':articles})

def tech_pg(request):
    articles = Tech.objects.all()
    return render(request, 'main/tech.html', {'i':articles})

def music_pg(request):
    articles = Music.objects.all()
    return render(request, 'main/music.html', {'i':articles})

def architecture_pg(request):
    articles = Architecture.objects.all()
    return render(request, 'main/architecture.html', {'i':articles})

def politics_pg(request):
    articles = Politics.objects.all()
    return render(request, 'main/politics.html', {'i':articles})

def about_pg(request):
    return render(request, 'main/about_pg.html')

def contact_pg(request):
    return render(request, 'main/contact.html')