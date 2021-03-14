from django import forms

class UrlForm(forms.Form):
    url = forms.URLField(label="URL", widget=forms.TextInput(attrs={'class': 'mb-3'}))