from django import forms

class SearchForm(forms.Form):
    # Define a form field named 'input_data' to match the HTML input field
    input_data = forms.CharField(
        label="Enter medicine",
        widget=forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Enter medicine'})
    )