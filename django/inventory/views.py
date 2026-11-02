from django.shortcuts import render, get_object_or_404
from .models import Car

def car_list(request):
    return render(request, 'car_list.html', {'cars': Car.objects.all()})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_detail.html', {'car': car})