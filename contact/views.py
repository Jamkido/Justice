from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact


def contact_view(request):  # readit 3 '1:7'daqiqaga qara
    form = ContactForm(request.POST or None)  # ( request.POST or None ) postdagi datani ol yoki bo'sh forma ber None
    # bilan
    # if request.method == 'POST':
    #     form = ContactForm(date=request.POST)
    if form.is_valid():
        form.save()
        return redirect('.')  # aynan shu page ga redirect qiladi
    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)

