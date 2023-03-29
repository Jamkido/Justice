from django.shortcuts import render
from .models import Reason, FAQ
from attorneys.models import Attorneys


def about_view(request):
    causes = Reason.objects.all()
    questions = FAQ.objects.all()
    team = Attorneys.objects.all()

    context = {
        'causes': causes,
        'questions': questions,
        'team': team
    }

    return render(request, 'about.html', context)
