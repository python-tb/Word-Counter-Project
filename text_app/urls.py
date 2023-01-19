from django.urls import path
from text_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('chars', views.chars, name='char_count'),
    path('vowels', views.vowels, name='vowel_count'),
    path('consonants', views.consonants, name='consonants_count'),
    path('upper', views.upper, name='upper'),
    path('lower', views.lower, name='lower'),
]
