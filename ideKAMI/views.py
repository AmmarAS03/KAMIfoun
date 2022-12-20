from django.shortcuts import render, redirect
from ideKAMI.models import Aspirasi
from django.http import HttpResponse



# Create your views here.

def show_ide(request):
    data = Aspirasi.objects.all()
    
    context = {
        'data': data
    }

    return render(request, 'show_ide.html', context)

def create_ide(request):
    if request.method == 'POST':
        input = request.POST.get('masukan')
    
        Aspirasi.objects.create(masukan=input)
        return redirect('ideKAMI:show_ide')

    return render(request, 'create_ide.html')