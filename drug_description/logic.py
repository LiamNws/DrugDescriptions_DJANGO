from .models import Drug

def process_description(search_term):
    # Query the database for drugs matching the search term
    matching_drugs = Drug.objects.filter(name__icontains=search_term)

    if not matching_drugs:
        return ["No matches found"]

    # Create a list of formatted drug descriptions
    result = []
    for drug in matching_drugs:
        description = f"{drug.name}: {drug.colour} {drug.shape} {drug.form}, '{drug.imprint}' imprinted. -LN"
        result.append(description)

    return result
