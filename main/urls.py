from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_pg, name='home'),
    path('sport', views.sport_pg, name='sport'),
    path('tech', views.tech_pg, name='tech'),
    path('music', views.music_pg, name='music'),
    path('politics', views.politics_pg, name='politics'),
    path('architecture', views.architecture_pg, name='architecture'),
    path('about', views.about_pg, name='about'),
    path('contact', views.contact_pg, name='contact')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
