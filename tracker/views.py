from django.shortcuts import render, redirect, get_object_or_404
from .models import BathroomVisit

def home(request):
    if request.method == 'POST':
        place = request.POST.get('place')
        if place:
            BathroomVisit.objects.create(place=place)
        return redirect('home')

    visits = BathroomVisit.objects.all()
    return render(request, 'tracker/home.html', {'visits': visits})

def delete_visit(request, visit_id):
    visit = get_object_or_404(BathroomVisit, id=visit_id)
    visit.delete()
    return redirect('home')
