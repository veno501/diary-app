from django import forms
from tinymce.widgets import TinyMCE

class EntryCreationForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=4, label='Entry title',
        widget=forms.TextInput(attrs={
            'placeholder': 'Dear Diary'
        }))
    location = forms.CharField(max_length=200, label='Entry location', required=False)

class EditorForm(forms.Form):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
