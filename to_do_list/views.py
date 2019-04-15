from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('New task has been added!'))
            return render(request,'home.html',{'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request,'home.html',{'all_items': all_items})

def about(request):
    return render(request,'about.html',{})
