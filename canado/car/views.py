from django.shortcuts import render, redirect
from .forms import CarForm
from .models import Car

def add_car(request):
    Car_form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')  # Nukreipkite į jūsų sąrašo puslapį

    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})



