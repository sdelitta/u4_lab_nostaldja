from django.shortcuts import render

from .models import Decade, Fad

def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostalgia/decade_list.html', {'decades': decades})

def fad_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostalgia/fad_list.html', {'fads': fads})

def decade_details(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nostalgia/decade_details.html', {'decade': decade})

def fad_details(request, pk):
    fad = Fad.objects.get(id=pk)
    return render(request, 'nostalgia/fad_details.html', {'fad': fad})