from django.shortcuts import render
# from noticeboard.models import Home
# from .models import


def index(request):
    return render(request, 'noticeboard/index.html')

def unemployment(request):
    return render(request, 'noticeboard/sample.html')

# def graph_view(request):
#     qs =