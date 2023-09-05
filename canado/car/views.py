from django.shortcuts import render, redirect
from .forms import CarForm
from .models import Car

def add_car(request):
    Car_form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car:car_list')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

