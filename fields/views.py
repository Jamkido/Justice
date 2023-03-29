from django.shortcuts import render
from .models import Practice_Areas


def Fields(request):
    items = Practice_Areas.objects.all()

    context = {
        'object_list': items
    }

    return render(request, 'pareas.html', context)
