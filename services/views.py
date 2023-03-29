from django.shortcuts import render
from .models import Works


def services_view(request):
    services = Works.objects.all()

    context = {
        'services_list': services
    }

    return render(request, 'services.html', context)
