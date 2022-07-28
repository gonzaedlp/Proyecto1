from django.shortcuts import render
from familyApp.models import FamilyApp
# Create your views here.

def create_people(request):
    new_person= FamilyApp.objects.create(name="Benjamin", age=15)
    context={
        "new_person":new_person
    }
    return render(request, "new_person.html", context=context)

def list_family(request):
    family= FamilyApp.objects.all()
    context={
        "family":family
    }
    return render(request, "family_list.html", context=context)

