from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import WorksForm, WorkTimeForm
from car.forms import CarForm

from .models import Works


# def priskirti_darbuotoja(request):
#     if request.method == 'POST':
#         form = DarbuotojasPriskyrimasForm(request.POST)
#         if form.is_valid():
#             darbuotojas = form.cleaned_data['darbuotojas']
#             priskirti_darbai = form.cleaned_data['priskirti_darbai']
#             darbo_pavadinimas = form.cleaned_data['darbo_pavadinimas']
#             pareigos = form.cleaned_data['pareigos']
#             darbo_pradzios_laikas = form.cleaned_data['darbo_pradzios_laikas']
#             darbo_pabaigos_laikas = form.cleaned_data['darbo_pabaigos_laikas']
#             valandinis_ikainis = form.cleaned_data['valandinis_ikainis']
#
#
#             # Čia galite vykdyti veiksmus su pasirinktu darbuotoju ir darbais
#             # Pavyzdžiui, sukurti įrašą su priskirtais darbais arba atnaujinti esamą įrašą
#             return render(request, 'priskyrimas_sekmingas.html')
#     else:
#         form = DarbuotojasPriskyrimasForm()
#     return render(request, 'priskirti_darbuotoja.html', {'form': form})

def create_work(request):
    works_form = WorksForm()
    car_form = CarForm()
    if request.method == 'POST':
        if "works-form" in request.POST:
            form = WorksForm(request.POST)
        elif "car-form" in request.POST:
            form = CarForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect( '/works/works/')
    context = {'works_form': works_form, 'car_form': car_form}
    return render(request, 'create_work.html',context)

def works_list(request):
    works = Works.objects.all()
    return render(request, 'works_list.html', {'works': works})

def darbai_darbuotojams(request):
    works_form = WorksForm()

    if request.method == 'POST':
        if "works-form" in request.POST:
            form = WorksForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect( '/works/works/')
    context = {'works_form': works_form,}
    return render(request, 'create_work.html',context)

def darbuotojo_darbai(request):
    works = Works.objects.filter(darbuotojas=request.user)
    # User = get_user_model()
    # try:
    #     user = User.objects.get(pk=request.user.pk)
    # except User.DoesNotExist:
    #     raise Http404("Vartotojas neegzistuoja")
    return render(request, 'darbuotojo_darbai.html', {'works': works})


def darbas(request,id):
    work = Works.objects.get(id=id)
    form = WorkTimeForm(instance=work)
    if request.method == 'POST':
        form = WorkTimeForm(request.POST, instance=work)

        if form.is_valid():
            form.save()
            return redirect( '/works/darbuotojo_darbai/')

    return render(request, 'darbas.html', {'form': form, 'work': work})