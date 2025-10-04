from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal
from .forms import AnimalForm

def home(request):
    animais = Animal.objects.all()
    return render(request, 'index.html', {'animais': animais})

def cadastro_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AnimalForm()
    return render(request, 'cadastro.html', {'form': form})

def editar_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'editar.html', {'form': form, 'animal': animal})

def excluir_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('home')
    return render(request, 'excluir.html', {'animal': animal})

def detalhes_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'detalhes.html', {'animal': animal})