from django import forms
from .models import Challenge


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = "__all__"

class SearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')