from django.shortcuts import render, get_object_or_404
from .models import Banda, Palco, Dia, Concerto


def index_view(request):
    context = {
        'bandas': Banda.objects.all(),
    }
    return render(request, 'festival/index.html', context)


def dias_view(request):
    context = {
        'dias': Dia.objects.all(),
    }
    return render(request, 'festival/dias.html', context)


def concerto_view(request, id):
    concerto = get_object_or_404(Concerto, id=id)
    context = {
        'concerto': concerto,
    }
    return render(request, 'festival/concerto.html', context)


def palcos_view(request):
    context = {
        'palcos': Palco.objects.all(),
    }
    return render(request, 'festival/palcos.html', context)