from django.shortcuts import render

from django.http import HttpResponse


def about(request):
    return render(request, "aboutpage.html")
# Create your views here.
