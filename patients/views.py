from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Patients
from .forms import PatientForm


# Create your views here.
def index(request):
    tasks = Patients.objects.all().order_by('-id')
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)


def add(request):
    tasks = Patients.objects.all()
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'tasks': tasks, 'form': form}
    return render(request, 'add.html', context)


def update(request, pk):
    task = Patients.objects.get(id=pk)
    form = PatientForm(instance=task)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'update.html', context)


def delete(request, pk):
    item = Patients.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'delete.html', context)
