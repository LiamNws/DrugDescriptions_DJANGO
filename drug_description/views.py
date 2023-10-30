from django.shortcuts import render
from django.http import HttpResponse
from .logic import process_description
from .forms import SearchForm

def home(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data["input_data"]
            result = process_description(input_data)
            if result == "No matches found":
                results_found = False
            else:
                results_found = True
            return render(request, 'drug_description/result.html', {'result': result, 'results_found': results_found})
        else:
            # Handle the case where the form is not valid
            error_message = "Invalid input. Please check your input and try again."
            return render(request, 'drug_description/input_form.html', {'form': form, 'error_message': error_message})
    else:
        form = SearchForm()
    
    return render(request, 'drug_description/input_form.html', {'form': form})