from django import forms
from cowsay.models import CowSay


class AddCowSayForm(forms.Form):
    title = forms.CharField(max_length=50)
