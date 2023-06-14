from django.shortcuts import render, redirect
from .models import Member
from .forms import HeaderForm

def home(request):
    members = Member.objects.first()
    return render(request, 'app/home.html', {'members': members})

def admin(request):
    members = Member.objects.first()
    return render(request, 'app/admin.html', {'members': members})

def update(request,id):
    # recup un element a la fois
    members = Member.objects.first()
    # recup un element via l'id
    member = Member.objects.get(id=id)
    # definir l'existance
    form = None
    if request.method == 'POST':
        form = HeaderForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('admin')
        else:
            print('grosse salope')
    else:
        form = HeaderForm(instance=member)
        
    return render(request, 'app/update.html', {'form': form, 'member': member})


