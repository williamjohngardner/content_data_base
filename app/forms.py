from django import forms
from app.models import File


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
    name = forms.ChoiceField()
    category = forms.ChoiceField()
    tag = forms.ChoiceField()

    class Meta:
        model = File
        fields = ('name', 'category', 'tag')
