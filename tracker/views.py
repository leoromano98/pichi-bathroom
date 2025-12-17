from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime
from .models import BathroomVisit

def home(request):
    if request.method == 'POST':
        place = request.POST.get('place')
        deployed_at_str = request.POST.get('deployed_at')

        if place:
            if deployed_at_str:
                deployed_at = timezone.make_aware(datetime.fromisoformat(deployed_at_str))
                new_visit = BathroomVisit.objects.create(place=place, deployed_at=deployed_at)
            else:
                new_visit = BathroomVisit.objects.create(place=place)
            return redirect(f'/?new_id={new_visit.id}')
        return redirect('home')

    visits = BathroomVisit.objects.all()
    new_id = request.GET.get('new_id')
    return render(request, 'tracker/home.html', {'visits': visits, 'new_id': new_id})

def delete_visit(request, visit_id):
    visit = get_object_or_404(BathroomVisit, id=visit_id)
    visit.delete()
    return redirect('home')
