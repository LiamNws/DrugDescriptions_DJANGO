from django.shortcuts import render
from .forms import SearchForm
from .locationLogic import process_location
# Create your views here.


# def pot_locations(request):
#     return render(request, "drug_description/pot_locations.html")


def pot_locations(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():

            search_term = form.cleaned_data['input_data']
            result = process_location(search_term)

            if result == "No matches found":
                results_found = False
            else:
                results_found = True
            return render(request, 'drug_description/location_result.html', {'result': result, 'results_found': results_found})
        else:
            # Handle the case where the form is not valid, e.g., display an error message.
            error_message = "Invalid input. Please check your input and try again."
            
    else:
        form = SearchForm()
    return render(request, 'drug_description/pot_locations.html', {'form': form})