from django.shortcuts import render


def homepage(request):
    return render(request, 'drug_description/base.html')