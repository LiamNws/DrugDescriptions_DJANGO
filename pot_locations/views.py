from django.shortcuts import render

# Create your views here.


def pot_locations(request):
    return render(request, "drug_description/pot_locations.html")