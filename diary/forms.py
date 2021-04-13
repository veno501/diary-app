from django import forms

class EntryCreationForm(forms.Form):
    title = forms.CharField(max_length=100, label='Entry title', initial='An Entry')

class DiaryCreationForm(forms.Form):
    title = forms.CharField(max_length=100, label='Diary title', initial='A Diary')
    color = forms.IntegerField(label='Your theme', initial=0)