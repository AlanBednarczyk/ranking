from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib import messages
from django.shortcuts import render


def person_list(request):
    people = Person.objects.all()
    return render(request, 'myapp/person_list.html', {'people': people})

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'myapp/add_person.html', {'form': form})


def delete_person(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
        person.delete()
        messages.success(request, f'{person.name} has been deleted.')
    except Person.DoesNotExist:
        messages.error(request, f'Person with id {person_id} does not exist.')

    return redirect('person_list')  # Przekieruj na stronę listy osób


@method_decorator(csrf_exempt, name='dispatch')
class UpdateMatchCountView(View):
    def patch(self, request, person_id):
        person = get_object_or_404(Person, id=person_id)
        match_type = request.GET.get('type')
        value = int(request.GET.get('value', 0))

        if match_type == 'won':
            person.matches_won += value
        elif match_type == 'lost':
            person.matches_lost += value

        person.save()

        return JsonResponse({'status': 'success'})