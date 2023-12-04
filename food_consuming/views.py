from django.shortcuts import render, redirect
from food_consuming.models import Food, Consume
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse("Hello World")
