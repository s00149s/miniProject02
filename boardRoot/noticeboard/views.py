from django.shortcuts import render


def index(request):
    return render(request, 'noticeboard/index.html')

def unemployment(request):
    return render(request, 'noticeboard/unemployment.html')

def race(request):
    return render(request, 'noticeboard/race.html')

def intro(request):
    return render(request, 'noticeboard/intro.html')

def result(request):
    return render(request, 'noticeboard/result.html')

def poverty(request):
    return render(request, 'noticeboard/poverty.html')