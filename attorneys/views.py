from django.shortcuts import render
from .models import Attorneys
from fields.models import Practice_Areas


def index(request):
    p_areas = Practice_Areas.objects.all()

    context = {
        'p_areas': p_areas,
    }

    return render(request, 'index.html', context)


def attorneys(request):
    attorneys = Attorneys.objects.all()

    context = {
        'attorney_list': attorneys,
    }

    return render(request, 'attorneys.html', context)


def single(request, pk=None):
    law_object = None
    if law_object is not None:
        law_object = Attorneys.objects.get(id=pk)

    context = {
        'object_single': law_object
    }

    return render(request, 'single.html', context)

