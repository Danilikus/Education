from django.shortcuts import render
from django.http import *
from .forms import UserForm
from .models import Person

klientl = Person.objects.get(narne="Bиктop") 
klient2 = Person.objects.get(age=25)
klientЗ = Person.objects.get(name="Bacилий", age=23)
