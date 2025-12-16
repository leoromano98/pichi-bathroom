from django.shortcuts import render, redirect
from .models import BathroomVisit

def home(request):
    if request.method == 'POST':
        place = request.POST.get('place')
        if place:
            BathroomVisit.objects.create(place=place)
        return redirect('home')

    visits = BathroomVisit.objects.all()
    return render(request, 'tracker/home.html', {'visits': visits})
