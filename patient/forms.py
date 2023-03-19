from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name','document')

class SearchForm(forms.Form):
    search = forms.CharField(max_length=255, required=False)