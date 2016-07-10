from django.shortcuts import render

# Create your views here.

def mainpage_index(request):
    return render(request, "mainpage_index.html")

